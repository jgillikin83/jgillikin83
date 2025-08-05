# Wiki Best Practices 🏆

Building an effective personal wiki requires thoughtful organization and consistent practices. Here's a comprehensive guide to help you create and maintain a valuable knowledge base.

## Page Organization

### Naming Conventions

- **Use clear, descriptive names**: `project-setup` instead of `proj1`
- **Be consistent with naming style**: Choose between `kebab-case`, `snake_case`, or `CamelCase` and stick with it
- **Include context when needed**: `docker-troubleshooting` is better than just `troubleshooting`
- **Avoid special characters**: Stick to letters, numbers, hyphens, and underscores

### Page Structure

#### Start with a Clear Title
Every page should begin with a descriptive H1 header that matches the page name:

```markdown
# Docker Troubleshooting Guide
```

#### Use Consistent Headers
Create a logical hierarchy with your headers:

```markdown
# Main Topic
## Major Section
### Subsection
#### Details
```

#### Include Navigation Elements
- Link to related pages
- Create "See also" sections
- Add breadcrumbs for complex topics

## Content Guidelines

### Write for Your Future Self

Remember that you'll be reading this content weeks or months later:

- **Provide context**: Explain why something matters
- **Include examples**: Show real code, commands, or scenarios
- **Add timestamps**: Note when information was last updated
- **Explain assumptions**: State prerequisites and dependencies

### Keep Information Current

- **Date-stamp important information**: Especially for technical content
- **Review and update regularly**: Set reminders to revisit key pages
- **Mark outdated content**: Use clear indicators when information becomes obsolete
- **Archive old versions**: Keep historical context when needed

### Use Rich Formatting

- **Code blocks** for commands and scripts
- **Lists** for steps and requirements
- **Tables** for structured data
- **Blockquotes** for important notes or warnings
- **Bold/italic** for emphasis

## Linking Strategy

### Internal Links

Create connections between related pages:

```markdown
See also: [Markdown Guide](/page/markdown-guide)
Related: [Project Setup](/page/project-setup)
```

### Build Topic Clusters

Group related pages and cross-link them:

- **Development** → Setup, Troubleshooting, Best Practices
- **Personal** → Notes, Goals, Learning
- **Projects** → Documentation, Requirements, Progress

## Search Optimization

### Use Searchable Keywords

Include terms you'll likely search for:

- **Alternate names**: Include synonyms and abbreviations
- **Problem descriptions**: Add common error messages
- **Context keywords**: Include project names, technologies, etc.

### Create Index Pages

Build hub pages that link to related content:

```markdown
# Development Hub

## Quick Links
- [Environment Setup](/page/dev-setup)
- [Common Commands](/page/dev-commands)
- [Troubleshooting](/page/dev-troubleshooting)

## Current Projects
- [Project Alpha](/page/project-alpha)
- [Project Beta](/page/project-beta)
```

## Maintenance Routines

### Weekly Reviews

- **Check recent pages**: Ensure new content follows standards
- **Update status**: Mark completed tasks and outdated information
- **Fix broken links**: Verify internal and external links work

### Monthly Cleanups

- **Archive old content**: Move outdated pages to an archive section
- **Consolidate duplicates**: Merge similar pages when appropriate
- **Update indexes**: Refresh hub pages and navigation

### Quarterly Audits

- **Review organization**: Assess if the current structure still makes sense
- **Update templates**: Refine your standard page formats
- **Backup content**: Ensure your wiki data is properly backed up

## Page Templates

### Standard Page Template

```markdown
# Page Title

Brief description of what this page covers.

## Overview
- Key point 1
- Key point 2
- Key point 3

## Main Content
Detailed information here...

## Examples
Practical examples and code samples...

## Related Pages
- [Related Page 1](/page/related-1)
- [Related Page 2](/page/related-2)

## Last Updated
[Date] - [Brief description of changes]
```

### Project Page Template

```markdown
# Project Name

## Status
Current status and progress...

## Overview
What this project is about...

## Requirements
- Requirement 1
- Requirement 2

## Setup Instructions
Step-by-step setup...

## Documentation
Links to relevant docs...

## Notes
Ongoing thoughts and updates...
```

## Common Pitfalls to Avoid

### Organization Issues

- **Too many top-level pages**: Create categories and sub-pages
- **Inconsistent naming**: Establish and follow naming conventions
- **Orphaned pages**: Ensure every page is linked from somewhere
- **Deep nesting**: Keep navigation within 2-3 levels when possible

### Content Problems

- **Duplicate information**: Consolidate or link to canonical sources
- **Outdated content**: Regular reviews prevent stale information
- **Missing context**: Always explain the "why" behind information
- **Poor formatting**: Use Markdown features to improve readability

### Technical Issues

- **Broken links**: Regular link checking prevents dead ends
- **Large pages**: Split content into focused, digestible pages
- **No search strategy**: Include searchable keywords and synonyms

## Advanced Techniques

### Tagging System

Create a pseudo-tagging system using consistent naming:

```markdown
# Development-Docker-Setup
# Development-Docker-Troubleshooting
# Personal-Learning-JavaScript
```

### Version Control

Track important changes in your content:

```markdown
## Change Log
- 2024-01-15: Added new troubleshooting section
- 2024-01-10: Updated setup instructions for v2.0
- 2024-01-05: Initial version
```

### Cross-References

Build a web of knowledge with strategic cross-linking:

```markdown
> **Note**: This relates to the [Database Setup](/page/db-setup) process.
> See [Security Guidelines](/page/security) for authentication details.
```

## Success Metrics

A well-organized wiki should be:

- **Findable**: You can locate information quickly
- **Current**: Information is up-to-date and relevant
- **Connected**: Related information links together logically
- **Consistent**: Formatting and organization follow patterns
- **Valuable**: Content helps you accomplish goals efficiently

Remember: The best wiki is the one you actually use and maintain. Start simple and evolve your practices as your needs grow!