# Documentation Usage Examples

This guide shows how to use the comprehensive documentation framework provided in this repository.

## Quick Start

### 1. Using the Documentation Generator Script

For projects with existing code, use the automated documentation generator:

```bash
# Basic usage - scan current directory
python scripts/generate-docs.py

# Scan specific directory
python scripts/generate-docs.py --source-dir ./src --output-dir ./docs/auto-generated

# Include private functions and methods
python scripts/generate-docs.py --include-private --source-dir ./src

# Generate only for specific file types
python scripts/generate-docs.py --source-dir ./src --language python
```

### 2. Using Documentation Templates Manually

For new projects or custom documentation, copy and customize the templates:

```bash
# Copy API documentation template
cp docs/API_DOCUMENTATION_TEMPLATE.md docs/my-api.md

# Copy function documentation template  
cp docs/FUNCTION_DOCUMENTATION_TEMPLATE.md docs/my-functions.md

# Copy component documentation template
cp docs/COMPONENT_DOCUMENTATION_TEMPLATE.md docs/my-components.md
```

## Detailed Examples

### API Documentation Example

Here's how to document a REST API using the template:

```markdown
# User Management API

**Base URL**: `https://api.myapp.com/v1`
**Authentication**: Bearer Token
**Rate Limiting**: 1000 requests per hour

## Authentication

Include the authorization header with every request:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Endpoints

### Get User Profile

**Endpoint**: `GET /users/{id}`
**Description**: Retrieves user profile information

**Path Parameters**:
- `id` (string, required): User unique identifier

**Response** (200 OK):
```json
{
  "id": "user_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2023-01-01T00:00:00Z"
}
```

**Example**:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
     https://api.myapp.com/v1/users/user_123
```
```

### Function Documentation Example

Here's how to document a Python function:

```markdown
## Function: calculate_user_score

**Description**: Calculates a user's score based on their activity metrics and engagement patterns.

**Signature**: 
```python
def calculate_user_score(
    user_data: Dict[str, Any], 
    weights: Optional[Dict[str, float]] = None,
    normalize: bool = True
) -> float
```

### Parameters

- `user_data` (Dict[str, Any], required): User activity data containing:
  - `posts`: number of posts created
  - `likes`: number of likes received  
  - `comments`: number of comments made
  - `login_days`: number of active days
- `weights` (Dict[str, float], optional): Scoring weights for each metric (default: equal weights)
- `normalize` (bool, optional): Whether to normalize score to 0-100 range (default: True)

### Returns

- `float`: Calculated user score (0-100 if normalized, otherwise raw score)

### Raises

- `ValueError`: When user_data is missing required fields
- `TypeError`: When weights contain non-numeric values

### Examples

#### Basic Usage
```python
user_data = {
    'posts': 25,
    'likes': 150,
    'comments': 45,
    'login_days': 30
}

score = calculate_user_score(user_data)
print(f"User score: {score}")  # User score: 78.5
```

#### With Custom Weights
```python
custom_weights = {
    'posts': 0.4,
    'likes': 0.3,
    'comments': 0.2,
    'login_days': 0.1
}

score = calculate_user_score(user_data, weights=custom_weights)
```

### Performance Notes

- Time complexity: O(1)
- Space complexity: O(1)
- Typical execution time: < 1ms

### Notes

- Score calculation uses weighted average of normalized metrics
- Missing metrics are treated as zero values
- Compatible with Python 3.7+
```

### React Component Documentation Example

Here's how to document a React component:

```markdown
## Component: SearchInput

**Description**: A reusable search input component with debounced search, suggestions, and keyboard navigation.

**Type**: Form Component

### Props

```typescript
interface SearchInputProps {
  placeholder?: string;
  value?: string;
  suggestions?: string[];
  debounceMs?: number;
  onSearch: (query: string) => void;
  onSelect?: (suggestion: string) => void;
  loading?: boolean;
  disabled?: boolean;
  className?: string;
}
```

| Prop | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `placeholder` | `string` | No | `"Search..."` | Input placeholder text |
| `value` | `string` | No | `""` | Controlled input value |
| `suggestions` | `string[]` | No | `[]` | Array of search suggestions |
| `debounceMs` | `number` | No | `300` | Debounce delay in milliseconds |
| `onSearch` | `function` | Yes | - | Callback fired when search is performed |
| `onSelect` | `function` | No | - | Callback fired when suggestion is selected |
| `loading` | `boolean` | No | `false` | Show loading indicator |
| `disabled` | `boolean` | No | `false` | Disable the input |

### Events

- `onSearch`: Triggered when user types (debounced)
- `onSelect`: Triggered when user selects a suggestion

### Usage Examples

#### Basic Usage
```jsx
import { SearchInput } from './components/SearchInput';

function App() {
  const handleSearch = (query) => {
    console.log('Searching for:', query);
    // Perform search
  };

  return (
    <SearchInput 
      placeholder="Search products..."
      onSearch={handleSearch}
    />
  );
}
```

#### With Suggestions
```jsx
function SearchPage() {
  const [suggestions, setSuggestions] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (query) => {
    setLoading(true);
    try {
      const results = await fetchSuggestions(query);
      setSuggestions(results);
    } finally {
      setLoading(false);
    }
  };

  const handleSelect = (suggestion) => {
    // Navigate to selected item
    router.push(`/products/${suggestion}`);
  };

  return (
    <SearchInput 
      placeholder="Search products..."
      suggestions={suggestions}
      loading={loading}
      onSearch={handleSearch}
      onSelect={handleSelect}
      debounceMs={500}
    />
  );
}
```

### Styling

#### CSS Classes
- `.search-input`: Main container
- `.search-input__field`: Input field
- `.search-input__suggestions`: Suggestions dropdown
- `.search-input__suggestion`: Individual suggestion item
- `.search-input--loading`: Loading state modifier

### Accessibility

- **ARIA Labels**: Input has proper labeling
- **Keyboard Navigation**: Arrow keys for suggestion navigation
- **Screen Reader**: Announces suggestion count and selection
- **Focus Management**: Proper focus handling for dropdown
```

## Documentation Automation

### Setting Up CI/CD Documentation

Add this to your GitHub Actions workflow:

```yaml
name: Generate Documentation

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  docs:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Generate Documentation
      run: |
        python scripts/generate-docs.py --source-dir ./src --output-dir ./docs/auto
    
    - name: Deploy to GitHub Pages
      if: github.ref == 'refs/heads/main'
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./docs
```

### Pre-commit Hook for Documentation

Add this to `.git/hooks/pre-commit`:

```bash
#!/bin/bash

# Check if documentation is up to date
echo "Checking documentation..."

# Generate documentation
python scripts/generate-docs.py --source-dir ./src --output-dir ./docs/temp

# Compare with existing docs
if ! diff -r ./docs/auto ./docs/temp > /dev/null; then
  echo "Documentation is out of date. Updating..."
  rm -rf ./docs/auto
  mv ./docs/temp ./docs/auto
  git add ./docs/auto
else
  rm -rf ./docs/temp
  echo "Documentation is up to date."
fi
```

### Package.json Scripts

For Node.js projects, add these scripts:

```json
{
  "scripts": {
    "docs:generate": "python scripts/generate-docs.py --source-dir ./src",
    "docs:serve": "npx http-server docs -p 8080",
    "docs:build": "npm run docs:generate && npx @11ty/eleventy",
    "docs:watch": "npm run docs:generate && npx @11ty/eleventy --serve"
  }
}
```

## Best Practices

### 1. Documentation Structure

Organize your documentation following this structure:

```
docs/
├── index.md                 # Main documentation index
├── api/                     # API documentation
│   ├── overview.md
│   ├── authentication.md
│   └── endpoints/
├── guides/                  # User guides
│   ├── getting-started.md
│   ├── tutorials/
│   └── examples/
├── reference/               # Technical reference
│   ├── functions/
│   ├── components/
│   └── classes/
├── templates/               # Documentation templates
└── auto-generated/          # Generated documentation
```

### 2. Writing Guidelines

- **Be Clear**: Use simple, direct language
- **Be Complete**: Cover all public interfaces
- **Be Consistent**: Use the same format throughout
- **Include Examples**: Always provide usage examples
- **Keep Updated**: Update docs with code changes

### 3. Code Documentation Standards

#### Python
```python
def process_data(data: List[Dict], options: Optional[Dict] = None) -> Dict:
    """
    Process raw data through validation and transformation pipeline.
    
    Args:
        data: List of data dictionaries to process
        options: Optional processing configuration
        
    Returns:
        Dictionary containing processed data and metadata
        
    Raises:
        ValueError: When data format is invalid
        
    Example:
        >>> data = [{'id': 1, 'name': 'test'}]
        >>> result = process_data(data)
        >>> print(result['processed_count'])
        1
    """
    pass
```

#### JavaScript/TypeScript
```javascript
/**
 * Calculate user engagement score based on activity metrics
 * 
 * @param {Object} userMetrics - User activity data
 * @param {number} userMetrics.posts - Number of posts created
 * @param {number} userMetrics.likes - Number of likes received
 * @param {Object} [options] - Calculation options
 * @param {boolean} [options.normalize=true] - Normalize to 0-100 scale
 * @returns {number} Calculated engagement score
 * 
 * @example
 * const score = calculateEngagement({ posts: 10, likes: 50 });
 * console.log(score); // 75.5
 */
function calculateEngagement(userMetrics, options = {}) {
    // Implementation
}
```

### 4. Testing Documentation

#### Documentation Tests
```python
# test_docs.py
import doctest
import my_module

def test_docstring_examples():
    """Test that all docstring examples work correctly."""
    failures, tests = doctest.testmod(my_module)
    assert failures == 0, f"{failures} docstring examples failed"
```

#### Link Checking
```bash
# Check for broken links in documentation
find docs -name "*.md" -exec markdown-link-check {} \;
```

## Tools and Integrations

### Documentation Generators

1. **Python**: Sphinx, pdoc3, mkdocs
2. **JavaScript**: JSDoc, TypeDoc, Docusaurus
3. **Multi-language**: GitBook, Notion, Confluence

### IDE Extensions

- **VS Code**: Markdown All in One, Docs Authoring Pack
- **JetBrains**: Markdown Navigator, Documentation Tool
- **Sublime Text**: MarkdownEditing, Markdown Preview

### Deployment Options

1. **GitHub Pages**: Free hosting for open source
2. **Netlify**: Continuous deployment with previews
3. **Vercel**: Fast static site deployment
4. **Read the Docs**: Python-focused documentation hosting

## Maintenance

### Regular Reviews

Schedule quarterly documentation reviews:

1. **Accuracy**: Verify examples still work
2. **Completeness**: Check for missing documentation
3. **Relevance**: Remove outdated information
4. **Usability**: Get feedback from users

### Metrics to Track

- Documentation coverage percentage
- User engagement with docs
- Support ticket reduction
- Time to onboard new developers

### Version Control

- Keep documentation in same repository as code
- Use semantic versioning for major doc changes
- Tag documentation releases
- Maintain changelog for documentation updates

---

This comprehensive documentation framework provides everything you need to create and maintain high-quality documentation for your projects. Adapt the templates and examples to fit your specific needs and technology stack.