# Markdown Guide 📝

Markdown is a lightweight markup language that allows you to format text using simple syntax. This guide covers all the Markdown features supported in this wiki.

## Basic Formatting

### Headers

Create headers using the `#` symbol:

```markdown
# Header 1 (Main title)
## Header 2 (Section)
### Header 3 (Subsection)
#### Header 4 (Sub-subsection)
##### Header 5 (Minor section)
###### Header 6 (Smallest header)
```

### Text Formatting

- **Bold text**: Use `**bold**` or `__bold__`
- *Italic text*: Use `*italic*` or `_italic_`
- ***Bold and italic***: Use `***text***`
- ~~Strikethrough~~: Use `~~strikethrough~~`
- `Inline code`: Use backticks `` `code` ``

### Paragraphs and Line Breaks

- Separate paragraphs with an empty line
- For a line break within a paragraph, end the line with two spaces

## Lists

### Unordered Lists

Use `-`, `*`, or `+` for bullet points:

```markdown
- First item
- Second item
  - Nested item
  - Another nested item
- Third item
```

Result:
- First item
- Second item
  - Nested item
  - Another nested item
- Third item

### Ordered Lists

Use numbers followed by periods:

```markdown
1. First step
2. Second step
3. Third step
   1. Sub-step A
   2. Sub-step B
```

Result:
1. First step
2. Second step
3. Third step
   1. Sub-step A
   2. Sub-step B

## Links and Images

### Links

```markdown
[Link text](https://example.com)
[Link to another page](/page/welcome)
[Link with title](https://example.com "Link title")
```

### Images

```markdown
![Alt text](image-url.jpg)
![Alt text](image-url.jpg "Image title")
```

## Code

### Inline Code

Use single backticks for inline code: `` `code` ``

### Code Blocks

Use triple backticks for code blocks:

````markdown
```
Plain code block
```

```javascript
// JavaScript code with syntax highlighting
function hello() {
    console.log("Hello, world!");
}
```
````

## Quotes

Use `>` for blockquotes:

```markdown
> This is a blockquote.
> It can span multiple lines.
>
> You can even have multiple paragraphs.
```

Result:
> This is a blockquote.
> It can span multiple lines.
>
> You can even have multiple paragraphs.

## Tables

Create tables using pipes `|`:

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

Result:
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

### Table Alignment

```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| L1   |   C1   |    R1 |
| L2   |   C2   |    R2 |
```

## Horizontal Rules

Create horizontal lines using three or more hyphens, asterisks, or underscores:

```markdown
---
***
___
```

---

## Escape Characters

Use backslash `\` to escape special characters:

```markdown
\* This asterisk is literal, not italic
\# This is not a header
\`This is not code\`
```

## Advanced Tips

### Task Lists

Create checkboxes using `- [ ]` and `- [x]`:

```markdown
- [x] Completed task
- [ ] Incomplete task
- [ ] Another task
```

Result:
- [x] Completed task
- [ ] Incomplete task
- [ ] Another task

### Nested Elements

You can nest most elements within lists:

```markdown
1. First item
   
   This is a paragraph under the first item.
   
   ```code
   Code block under first item
   ```
   
2. Second item with **bold text**
```

## Best Practices

1. **Use descriptive headers** to create a clear structure
2. **Keep paragraphs short** for better readability
3. **Use lists** to break down complex information
4. **Add code blocks** for technical content
5. **Use tables** for structured data
6. **Include links** to connect related information

## Common Mistakes

- Forgetting to add empty lines around headers, lists, and code blocks
- Not escaping special characters when you want them to be literal
- Using inconsistent list markers (mixing `-`, `*`, and `+`)
- Forgetting the language specification in code blocks for syntax highlighting

Remember: Markdown is designed to be readable even in its raw form, so keep it simple and clean!