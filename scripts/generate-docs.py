#!/usr/bin/env python3
"""
Documentation Generator Script

This script automatically scans source code files and generates documentation
templates based on the code structure. It supports multiple programming languages
and can create API, function, and component documentation.

Usage:
    python generate-docs.py [options]

Options:
    --source-dir: Source directory to scan (default: current directory)
    --output-dir: Output directory for documentation (default: ./docs)
    --format: Output format (markdown, html, json) (default: markdown)
    --language: Programming language to scan (auto-detect if not specified)
    --include-private: Include private functions/methods (default: False)
    --template-type: Type of template (api, function, component) (default: auto)
"""

import os
import re
import json
import argparse
import ast
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class FunctionInfo:
    name: str
    docstring: Optional[str]
    parameters: List[Dict[str, Any]]
    return_type: Optional[str]
    decorators: List[str]
    line_number: int
    is_private: bool
    is_async: bool
    file_path: str


@dataclass
class ClassInfo:
    name: str
    docstring: Optional[str]
    methods: List[FunctionInfo]
    properties: List[Dict[str, Any]]
    base_classes: List[str]
    line_number: int
    is_private: bool
    file_path: str


@dataclass
class ModuleInfo:
    name: str
    docstring: Optional[str]
    functions: List[FunctionInfo]
    classes: List[ClassInfo]
    imports: List[str]
    file_path: str


class CodeAnalyzer:
    """Analyzes source code to extract documentation information."""
    
    def __init__(self, include_private: bool = False):
        self.include_private = include_private
        self.supported_extensions = {
            '.py': self._analyze_python,
            '.js': self._analyze_javascript,
            '.ts': self._analyze_typescript,
            '.jsx': self._analyze_jsx,
            '.tsx': self._analyze_tsx,
        }
    
    def analyze_file(self, file_path: Path) -> Optional[ModuleInfo]:
        """Analyze a single source code file."""
        if file_path.suffix not in self.supported_extensions:
            return None
        
        try:
            analyzer = self.supported_extensions[file_path.suffix]
            return analyzer(file_path)
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
            return None
    
    def analyze_directory(self, directory: Path) -> List[ModuleInfo]:
        """Analyze all source files in a directory recursively."""
        modules = []
        
        for file_path in directory.rglob('*'):
            if file_path.is_file() and file_path.suffix in self.supported_extensions:
                # Skip common ignored directories
                if any(part.startswith('.') or part in ['node_modules', '__pycache__', 'dist', 'build'] 
                       for part in file_path.parts):
                    continue
                
                module_info = self.analyze_file(file_path)
                if module_info:
                    modules.append(module_info)
        
        return modules
    
    def _analyze_python(self, file_path: Path) -> ModuleInfo:
        """Analyze Python source code."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        module_docstring = ast.get_docstring(tree)
        functions = []
        classes = []
        imports = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if self.include_private or not node.name.startswith('_'):
                    func_info = self._extract_python_function(node, file_path)
                    functions.append(func_info)
            
            elif isinstance(node, ast.AsyncFunctionDef):
                if self.include_private or not node.name.startswith('_'):
                    func_info = self._extract_python_function(node, file_path, is_async=True)
                    functions.append(func_info)
            
            elif isinstance(node, ast.ClassDef):
                if self.include_private or not node.name.startswith('_'):
                    class_info = self._extract_python_class(node, file_path)
                    classes.append(class_info)
            
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                imports.extend(self._extract_python_imports(node))
        
        return ModuleInfo(
            name=file_path.stem,
            docstring=module_docstring,
            functions=functions,
            classes=classes,
            imports=imports,
            file_path=str(file_path)
        )
    
    def _extract_python_function(self, node, file_path: Path, is_async: bool = False) -> FunctionInfo:
        """Extract function information from Python AST node."""
        parameters = []
        
        for arg in node.args.args:
            param_info = {
                'name': arg.arg,
                'type': self._get_annotation_string(arg.annotation) if arg.annotation else None,
                'default': None,
                'required': True
            }
            parameters.append(param_info)
        
        # Handle default values
        defaults_offset = len(node.args.args) - len(node.args.defaults)
        for i, default in enumerate(node.args.defaults):
            parameters[defaults_offset + i]['default'] = ast.unparse(default)
            parameters[defaults_offset + i]['required'] = False
        
        return FunctionInfo(
            name=node.name,
            docstring=ast.get_docstring(node),
            parameters=parameters,
            return_type=self._get_annotation_string(node.returns) if node.returns else None,
            decorators=[ast.unparse(dec) for dec in node.decorator_list],
            line_number=node.lineno,
            is_private=node.name.startswith('_'),
            is_async=is_async,
            file_path=str(file_path)
        )
    
    def _extract_python_class(self, node, file_path: Path) -> ClassInfo:
        """Extract class information from Python AST node."""
        methods = []
        properties = []
        
        for item in node.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if self.include_private or not item.name.startswith('_'):
                    method_info = self._extract_python_function(
                        item, file_path, isinstance(item, ast.AsyncFunctionDef)
                    )
                    methods.append(method_info)
            
            elif isinstance(item, ast.Assign):
                # Extract class properties
                for target in item.targets:
                    if isinstance(target, ast.Name):
                        prop_info = {
                            'name': target.id,
                            'type': None,
                            'value': ast.unparse(item.value) if item.value else None
                        }
                        properties.append(prop_info)
        
        return ClassInfo(
            name=node.name,
            docstring=ast.get_docstring(node),
            methods=methods,
            properties=properties,
            base_classes=[ast.unparse(base) for base in node.bases],
            line_number=node.lineno,
            is_private=node.name.startswith('_'),
            file_path=str(file_path)
        )
    
    def _extract_python_imports(self, node) -> List[str]:
        """Extract import statements."""
        imports = []
        
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ''
            for alias in node.names:
                imports.append(f"{module}.{alias.name}" if module else alias.name)
        
        return imports
    
    def _get_annotation_string(self, annotation) -> Optional[str]:
        """Convert AST annotation to string."""
        if annotation:
            try:
                return ast.unparse(annotation)
            except:
                return str(annotation)
        return None
    
    def _analyze_javascript(self, file_path: Path) -> ModuleInfo:
        """Analyze JavaScript source code."""
        # Basic JavaScript analysis using regex patterns
        # For production use, consider using a proper JS parser like Babel
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        functions = self._extract_js_functions(content, file_path)
        classes = self._extract_js_classes(content, file_path)
        imports = self._extract_js_imports(content)
        
        return ModuleInfo(
            name=file_path.stem,
            docstring=self._extract_js_module_comment(content),
            functions=functions,
            classes=classes,
            imports=imports,
            file_path=str(file_path)
        )
    
    def _extract_js_functions(self, content: str, file_path: Path) -> List[FunctionInfo]:
        """Extract JavaScript functions using regex."""
        functions = []
        
        # Match function declarations and expressions
        patterns = [
            r'(?:export\s+)?(?:async\s+)?function\s+(\w+)\s*\(([^)]*)\)\s*\{',
            r'(?:export\s+)?const\s+(\w+)\s*=\s*(?:async\s+)?\([^)]*\)\s*=>\s*\{',
            r'(?:export\s+)?const\s+(\w+)\s*=\s*(?:async\s+)?function\s*\([^)]*\)\s*\{'
        ]
        
        for pattern in patterns:
            for match in re.finditer(pattern, content, re.MULTILINE):
                func_name = match.group(1)
                if self.include_private or not func_name.startswith('_'):
                    # Extract JSDoc comment if present
                    docstring = self._extract_jsdoc_before_line(content, match.start())
                    
                    functions.append(FunctionInfo(
                        name=func_name,
                        docstring=docstring,
                        parameters=self._parse_js_parameters(match.group(2) if len(match.groups()) > 1 else ''),
                        return_type=None,  # Extract from JSDoc or TypeScript annotations
                        decorators=[],
                        line_number=content[:match.start()].count('\n') + 1,
                        is_private=func_name.startswith('_'),
                        is_async='async' in match.group(0),
                        file_path=str(file_path)
                    ))
        
        return functions
    
    def _extract_js_classes(self, content: str, file_path: Path) -> List[ClassInfo]:
        """Extract JavaScript classes using regex."""
        classes = []
        
        class_pattern = r'(?:export\s+)?class\s+(\w+)(?:\s+extends\s+(\w+))?\s*\{'
        
        for match in re.finditer(class_pattern, content, re.MULTILINE):
            class_name = match.group(1)
            if self.include_private or not class_name.startswith('_'):
                base_class = match.group(2) if match.group(2) else None
                
                # Extract class body to find methods
                class_start = match.end()
                brace_count = 1
                pos = class_start
                
                while pos < len(content) and brace_count > 0:
                    if content[pos] == '{':
                        brace_count += 1
                    elif content[pos] == '}':
                        brace_count -= 1
                    pos += 1
                
                class_body = content[class_start:pos-1]
                methods = self._extract_js_methods(class_body, file_path, class_start)
                
                classes.append(ClassInfo(
                    name=class_name,
                    docstring=self._extract_jsdoc_before_line(content, match.start()),
                    methods=methods,
                    properties=[],  # Could be extracted from constructor or property declarations
                    base_classes=[base_class] if base_class else [],
                    line_number=content[:match.start()].count('\n') + 1,
                    is_private=class_name.startswith('_'),
                    file_path=str(file_path)
                ))
        
        return classes
    
    def _extract_js_methods(self, class_body: str, file_path: Path, offset: int) -> List[FunctionInfo]:
        """Extract methods from JavaScript class body."""
        methods = []
        
        # Match method declarations
        method_pattern = r'(?:async\s+)?(\w+)\s*\(([^)]*)\)\s*\{'
        
        for match in re.finditer(method_pattern, class_body, re.MULTILINE):
            method_name = match.group(1)
            if method_name not in ['constructor'] and (self.include_private or not method_name.startswith('_')):
                methods.append(FunctionInfo(
                    name=method_name,
                    docstring=self._extract_jsdoc_before_line(class_body, match.start()),
                    parameters=self._parse_js_parameters(match.group(2)),
                    return_type=None,
                    decorators=[],
                    line_number=class_body[:match.start()].count('\n') + 1,
                    is_private=method_name.startswith('_'),
                    is_async='async' in match.group(0),
                    file_path=str(file_path)
                ))
        
        return methods
    
    def _extract_js_imports(self, content: str) -> List[str]:
        """Extract JavaScript import statements."""
        imports = []
        
        # Match ES6 imports
        import_patterns = [
            r'import\s+(?:\*\s+as\s+(\w+)|{([^}]+)}|\w+)\s+from\s+[\'"]([^\'"]+)[\'"]',
            r'const\s+(?:\w+|{[^}]+})\s*=\s*require\([\'"]([^\'"]+)[\'"]\)'
        ]
        
        for pattern in import_patterns:
            for match in re.finditer(pattern, content, re.MULTILINE):
                # Extract the module name (last group in the patterns)
                module_name = match.groups()[-1]
                imports.append(module_name)
        
        return imports
    
    def _extract_jsdoc_before_line(self, content: str, position: int) -> Optional[str]:
        """Extract JSDoc comment before a given position."""
        lines_before = content[:position].split('\n')
        
        # Look for JSDoc comment ending just before the function
        for i in range(len(lines_before) - 1, -1, -1):
            line = lines_before[i].strip()
            if line.endswith('*/'):
                # Found end of comment, now find the start
                comment_lines = []
                for j in range(i, -1, -1):
                    comment_line = lines_before[j].strip()
                    if comment_line.startswith('/**'):
                        # Found start of JSDoc comment
                        comment_lines.reverse()
                        return '\n'.join(comment_lines)
                    comment_lines.append(comment_line)
                break
            elif line and not line.startswith('*') and not line.startswith('//'):
                # Hit non-comment line
                break
        
        return None
    
    def _extract_js_module_comment(self, content: str) -> Optional[str]:
        """Extract module-level comment at the beginning of the file."""
        lines = content.strip().split('\n')
        
        if lines and lines[0].strip().startswith('/**'):
            comment_lines = []
            for line in lines:
                stripped = line.strip()
                if stripped.endswith('*/'):
                    comment_lines.append(stripped)
                    break
                comment_lines.append(stripped)
            
            if comment_lines:
                return '\n'.join(comment_lines)
        
        return None
    
    def _parse_js_parameters(self, params_str: str) -> List[Dict[str, Any]]:
        """Parse JavaScript function parameters."""
        if not params_str.strip():
            return []
        
        parameters = []
        param_parts = [p.strip() for p in params_str.split(',')]
        
        for param in param_parts:
            if '=' in param:
                # Has default value
                name, default = param.split('=', 1)
                parameters.append({
                    'name': name.strip(),
                    'type': None,
                    'default': default.strip(),
                    'required': False
                })
            else:
                parameters.append({
                    'name': param.strip(),
                    'type': None,
                    'default': None,
                    'required': True
                })
        
        return parameters
    
    def _analyze_typescript(self, file_path: Path) -> ModuleInfo:
        """Analyze TypeScript source code."""
        # For now, use JavaScript analysis with some TS-specific enhancements
        return self._analyze_javascript(file_path)
    
    def _analyze_jsx(self, file_path: Path) -> ModuleInfo:
        """Analyze JSX/React component files."""
        return self._analyze_javascript(file_path)
    
    def _analyze_tsx(self, file_path: Path) -> ModuleInfo:
        """Analyze TSX/TypeScript React component files."""
        return self._analyze_javascript(file_path)


class DocumentationGenerator:
    """Generates documentation from analyzed code."""
    
    def __init__(self, output_format: str = 'markdown'):
        self.output_format = output_format
        self.templates = {
            'function': self._generate_function_doc,
            'class': self._generate_class_doc,
            'module': self._generate_module_doc,
            'api': self._generate_api_doc
        }
    
    def generate_documentation(self, modules: List[ModuleInfo], output_dir: Path) -> None:
        """Generate documentation for all modules."""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate index file
        self._generate_index(modules, output_dir)
        
        # Generate documentation for each module
        for module in modules:
            self._generate_module_documentation(module, output_dir)
    
    def _generate_index(self, modules: List[ModuleInfo], output_dir: Path) -> None:
        """Generate index documentation file."""
        content = f"""# API Documentation

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview

This documentation was automatically generated from the source code analysis.

## Modules

"""
        
        for module in modules:
            rel_path = Path(module.file_path).relative_to(Path.cwd())
            content += f"- [{module.name}](./{module.name}.md) - `{rel_path}`\n"
            
            if module.docstring:
                # Add first line of docstring as description
                first_line = module.docstring.split('\n')[0].strip('"""').strip()
                content += f"  - {first_line}\n"
        
        content += f"\n## Statistics\n\n"
        content += f"- Total modules: {len(modules)}\n"
        content += f"- Total functions: {sum(len(m.functions) for m in modules)}\n"
        content += f"- Total classes: {sum(len(m.classes) for m in modules)}\n"
        
        with open(output_dir / 'index.md', 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _generate_module_documentation(self, module: ModuleInfo, output_dir: Path) -> None:
        """Generate documentation for a single module."""
        content = f"# {module.name}\n\n"
        
        if module.docstring:
            content += f"{module.docstring}\n\n"
        
        content += f"**File**: `{module.file_path}`\n\n"
        
        if module.imports:
            content += "## Imports\n\n"
            for imp in module.imports:
                content += f"- `{imp}`\n"
            content += "\n"
        
        # Generate function documentation
        if module.functions:
            content += "## Functions\n\n"
            for func in module.functions:
                content += self._generate_function_doc(func) + "\n"
        
        # Generate class documentation
        if module.classes:
            content += "## Classes\n\n"
            for cls in module.classes:
                content += self._generate_class_doc(cls) + "\n"
        
        filename = f"{module.name}.md"
        with open(output_dir / filename, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _generate_function_doc(self, func: FunctionInfo) -> str:
        """Generate documentation for a function."""
        content = f"### {func.name}\n\n"
        
        if func.docstring:
            content += f"{func.docstring}\n\n"
        
        # Signature
        signature = f"{'async ' if func.is_async else ''}{func.name}("
        param_strs = []
        for param in func.parameters:
            param_str = param['name']
            if param['type']:
                param_str += f": {param['type']}"
            if param['default']:
                param_str += f" = {param['default']}"
            param_strs.append(param_str)
        signature += ", ".join(param_strs) + ")"
        
        if func.return_type:
            signature += f" -> {func.return_type}"
        
        content += f"**Signature**: `{signature}`\n\n"
        
        # Parameters
        if func.parameters:
            content += "**Parameters**:\n\n"
            for param in func.parameters:
                required = "required" if param['required'] else "optional"
                param_type = param['type'] or 'any'
                default_info = f", default: `{param['default']}`" if param['default'] else ""
                content += f"- `{param['name']}` ({param_type}, {required}{default_info})\n"
            content += "\n"
        
        # Return type
        if func.return_type:
            content += f"**Returns**: `{func.return_type}`\n\n"
        
        # Decorators
        if func.decorators:
            content += f"**Decorators**: {', '.join(f'`{d}`' for d in func.decorators)}\n\n"
        
        # Location
        content += f"**Location**: Line {func.line_number} in `{func.file_path}`\n\n"
        
        return content
    
    def _generate_class_doc(self, cls: ClassInfo) -> str:
        """Generate documentation for a class."""
        content = f"### {cls.name}\n\n"
        
        if cls.docstring:
            content += f"{cls.docstring}\n\n"
        
        # Inheritance
        if cls.base_classes:
            content += f"**Inherits from**: {', '.join(f'`{base}`' for base in cls.base_classes)}\n\n"
        
        # Properties
        if cls.properties:
            content += "**Properties**:\n\n"
            for prop in cls.properties:
                prop_type = prop['type'] or 'any'
                content += f"- `{prop['name']}`: {prop_type}\n"
            content += "\n"
        
        # Methods
        if cls.methods:
            content += "**Methods**:\n\n"
            for method in cls.methods:
                content += self._generate_function_doc(method)
        
        # Location
        content += f"**Location**: Line {cls.line_number} in `{cls.file_path}`\n\n"
        
        return content
    
    def _generate_module_doc(self, module: ModuleInfo) -> str:
        """Generate documentation for a module."""
        return self._generate_module_documentation(module, Path('/tmp'))
    
    def _generate_api_doc(self, modules: List[ModuleInfo]) -> str:
        """Generate API overview documentation."""
        content = "# API Documentation\n\n"
        
        all_functions = []
        all_classes = []
        
        for module in modules:
            all_functions.extend(module.functions)
            all_classes.extend(module.classes)
        
        # Public functions
        public_functions = [f for f in all_functions if not f.is_private]
        if public_functions:
            content += "## Public Functions\n\n"
            for func in sorted(public_functions, key=lambda x: x.name):
                content += f"- [`{func.name}`](./{Path(func.file_path).stem}.md#{func.name.lower()})\n"
            content += "\n"
        
        # Public classes
        public_classes = [c for c in all_classes if not c.is_private]
        if public_classes:
            content += "## Public Classes\n\n"
            for cls in sorted(public_classes, key=lambda x: x.name):
                content += f"- [`{cls.name}`](./{Path(cls.file_path).stem}.md#{cls.name.lower()})\n"
            content += "\n"
        
        return content


def main():
    """Main entry point for the documentation generator."""
    parser = argparse.ArgumentParser(description='Generate documentation from source code')
    parser.add_argument('--source-dir', default='.', help='Source directory to scan')
    parser.add_argument('--output-dir', default='./docs/generated', help='Output directory for documentation')
    parser.add_argument('--format', default='markdown', choices=['markdown', 'html', 'json'], help='Output format')
    parser.add_argument('--language', help='Programming language to scan (auto-detect if not specified)')
    parser.add_argument('--include-private', action='store_true', help='Include private functions/methods')
    parser.add_argument('--template-type', default='auto', choices=['api', 'function', 'component', 'auto'], help='Type of template')
    
    args = parser.parse_args()
    
    source_dir = Path(args.source_dir).resolve()
    output_dir = Path(args.output_dir).resolve()
    
    print(f"Scanning source directory: {source_dir}")
    print(f"Output directory: {output_dir}")
    
    # Initialize analyzer and generator
    analyzer = CodeAnalyzer(include_private=args.include_private)
    generator = DocumentationGenerator(output_format=args.format)
    
    # Analyze source code
    print("Analyzing source code...")
    modules = analyzer.analyze_directory(source_dir)
    
    if not modules:
        print("No source files found or analyzed.")
        return
    
    print(f"Found {len(modules)} modules with:")
    total_functions = sum(len(m.functions) for m in modules)
    total_classes = sum(len(m.classes) for m in modules)
    print(f"  - {total_functions} functions")
    print(f"  - {total_classes} classes")
    
    # Generate documentation
    print("Generating documentation...")
    generator.generate_documentation(modules, output_dir)
    
    print(f"Documentation generated in: {output_dir}")
    print("Files created:")
    for file_path in output_dir.glob('*.md'):
        print(f"  - {file_path.name}")


if __name__ == '__main__':
    main()