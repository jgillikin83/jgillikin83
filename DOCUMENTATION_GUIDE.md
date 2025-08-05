# Documentation Guide

This guide provides a comprehensive framework for documenting APIs, functions, and components in your projects.

## Table of Contents

1. [Documentation Standards](#documentation-standards)
2. [API Documentation](#api-documentation)
3. [Function Documentation](#function-documentation)
4. [Component Documentation](#component-documentation)
5. [Code Examples](#code-examples)
6. [Documentation Tools](#documentation-tools)

## Documentation Standards

### General Principles

- **Clarity**: Write clear, concise descriptions
- **Completeness**: Cover all public interfaces
- **Examples**: Provide practical usage examples
- **Consistency**: Use consistent formatting and terminology
- **Maintenance**: Keep documentation up-to-date with code changes

### Documentation Structure

Each documented item should include:
- **Purpose**: What does it do?
- **Parameters**: Input requirements and types
- **Returns**: Output format and types
- **Examples**: Real-world usage scenarios
- **Notes**: Important considerations, limitations, or warnings

## API Documentation

### REST API Template

```markdown
## API Endpoint: [Method] /path/to/endpoint

**Description**: Brief description of what this endpoint does.

**Method**: GET | POST | PUT | DELETE | PATCH

**URL**: `/api/v1/endpoint`

**Authentication**: Required | Optional | None

### Parameters

#### Path Parameters
- `id` (integer, required): Unique identifier for the resource

#### Query Parameters
- `limit` (integer, optional): Maximum number of results (default: 10, max: 100)
- `offset` (integer, optional): Number of results to skip (default: 0)

#### Request Body
```json
{
  "name": "string (required)",
  "description": "string (optional)",
  "status": "active | inactive (required)"
}
```

### Response

#### Success Response (200 OK)
```json
{
  "id": 123,
  "name": "Example Resource",
  "description": "A sample resource",
  "status": "active",
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-01T00:00:00Z"
}
```

#### Error Responses
- `400 Bad Request`: Invalid request parameters
- `401 Unauthorized`: Authentication required
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

### Example Usage

#### cURL
```bash
curl -X GET \
  'https://api.example.com/v1/resources/123' \
  -H 'Authorization: Bearer YOUR_TOKEN'
```

#### JavaScript
```javascript
const response = await fetch('/api/v1/resources/123', {
  headers: {
    'Authorization': 'Bearer YOUR_TOKEN'
  }
});
const data = await response.json();
```

#### Python
```python
import requests

response = requests.get(
    'https://api.example.com/v1/resources/123',
    headers={'Authorization': 'Bearer YOUR_TOKEN'}
)
data = response.json()
```
```

### GraphQL API Template

```markdown
## GraphQL Query: [QueryName]

**Description**: Brief description of what this query does.

### Schema
```graphql
type Query {
  getUser(id: ID!): User
}

type User {
  id: ID!
  name: String!
  email: String!
  createdAt: DateTime!
}
```

### Example Query
```graphql
query GetUser($userId: ID!) {
  getUser(id: $userId) {
    id
    name
    email
    createdAt
  }
}
```

### Variables
```json
{
  "userId": "123"
}
```

### Response
```json
{
  "data": {
    "getUser": {
      "id": "123",
      "name": "John Doe",
      "email": "john@example.com",
      "createdAt": "2023-01-01T00:00:00Z"
    }
  }
}
```
```

## Function Documentation

### Function Template

```markdown
## Function: functionName

**Description**: Brief description of what the function does.

**Signature**: 
```language
returnType functionName(paramType1 param1, paramType2 param2)
```

### Parameters

- `param1` (paramType1): Description of the first parameter
- `param2` (paramType2): Description of the second parameter

### Returns

- `returnType`: Description of what is returned

### Throws/Exceptions

- `ExceptionType`: When this exception is thrown

### Examples

#### Basic Usage
```language
// Example of basic usage
const result = functionName(value1, value2);
console.log(result);
```

#### Advanced Usage
```language
// Example of advanced usage with error handling
try {
  const result = functionName(complexValue1, complexValue2);
  // Handle success
} catch (error) {
  // Handle error
}
```

### Notes

- Important considerations
- Performance implications
- Version information
```

### Language-Specific Examples

#### JavaScript/TypeScript
```markdown
## Function: calculateTotal

**Description**: Calculates the total price including tax and discounts.

**Signature**: 
```typescript
function calculateTotal(
  basePrice: number, 
  taxRate: number, 
  discount?: number
): number
```

### Parameters

- `basePrice` (number): The base price before tax and discounts
- `taxRate` (number): Tax rate as a decimal (e.g., 0.08 for 8%)
- `discount` (number, optional): Discount amount (default: 0)

### Returns

- `number`: The final total price

### Example
```typescript
// Basic usage
const total = calculateTotal(100, 0.08); // Returns 108

// With discount
const totalWithDiscount = calculateTotal(100, 0.08, 10); // Returns 98
```
```

#### Python
```markdown
## Function: process_data

**Description**: Processes raw data and returns cleaned results.

**Signature**: 
```python
def process_data(data: List[Dict], options: Optional[Dict] = None) -> Dict
```

### Parameters

- `data` (List[Dict]): Raw data to process
- `options` (Dict, optional): Processing options

### Returns

- `Dict`: Processed data with metadata

### Raises

- `ValueError`: If data format is invalid
- `TypeError`: If data types don't match expected format

### Example
```python
# Basic usage
raw_data = [{'id': 1, 'value': 'test'}]
result = process_data(raw_data)

# With options
options = {'strict': True, 'format': 'json'}
result = process_data(raw_data, options)
```
```

## Component Documentation

### React Component Template

```markdown
## Component: ComponentName

**Description**: Brief description of what the component does.

### Props

| Prop | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `prop1` | `string` | Yes | - | Description of prop1 |
| `prop2` | `number` | No | `0` | Description of prop2 |
| `onEvent` | `(value: string) => void` | No | - | Callback function |

### Usage

#### Basic Usage
```jsx
import ComponentName from './ComponentName';

function App() {
  return (
    <ComponentName 
      prop1="value" 
      prop2={10}
    />
  );
}
```

#### Advanced Usage
```jsx
import ComponentName from './ComponentName';

function App() {
  const handleEvent = (value) => {
    console.log('Event received:', value);
  };

  return (
    <ComponentName 
      prop1="value" 
      prop2={10}
      onEvent={handleEvent}
    />
  );
}
```

### Styling

The component accepts the following CSS classes:
- `.component-name`: Main container
- `.component-name__element`: Specific element within component

### Accessibility

- Supports keyboard navigation
- ARIA labels included
- Screen reader compatible

### Notes

- Important usage notes
- Browser compatibility
- Performance considerations
```

### Vue Component Template

```markdown
## Component: ComponentName

**Description**: Brief description of what the component does.

### Props

```typescript
interface Props {
  prop1: string;
  prop2?: number;
  onEvent?: (value: string) => void;
}
```

### Events

- `update`: Emitted when component state changes
- `error`: Emitted when an error occurs

### Slots

- `default`: Main content slot
- `header`: Header content slot

### Usage

#### Template
```vue
<template>
  <ComponentName 
    :prop1="value1" 
    :prop2="value2"
    @update="handleUpdate"
  >
    <template #header>
      Header content
    </template>
    Default slot content
  </ComponentName>
</template>
```

#### Script
```vue
<script setup lang="ts">
import ComponentName from './ComponentName.vue';

const value1 = ref('test');
const value2 = ref(10);

const handleUpdate = (newValue: string) => {
  console.log('Updated:', newValue);
};
</script>
```
```

## Code Examples

### Best Practices for Examples

1. **Start Simple**: Begin with basic usage examples
2. **Build Complexity**: Progress to more advanced scenarios
3. **Real-World Context**: Use realistic data and scenarios
4. **Error Handling**: Show proper error handling
5. **Comments**: Explain non-obvious parts

### Example Template

```markdown
### Example: [Scenario Name]

**Scenario**: Brief description of what this example demonstrates.

**Code**:
```language
// Step 1: Setup
const setup = initializeService();

// Step 2: Process
const result = setup.process(data);

// Step 3: Handle result
if (result.success) {
  console.log('Success:', result.data);
} else {
  console.error('Error:', result.error);
}
```

**Expected Output**:
```
Success: { id: 123, processed: true }
```

**Notes**: Any important notes about this example.
```

## Documentation Tools

### Recommended Tools

#### Automatic Documentation Generation
- **JSDoc** (JavaScript/TypeScript): Generate docs from code comments
- **Sphinx** (Python): Comprehensive documentation generator
- **Rustdoc** (Rust): Built-in documentation tool
- **Godoc** (Go): Standard documentation tool
- **Javadoc** (Java): Standard documentation generator

#### Documentation Platforms
- **GitBook**: Feature-rich documentation platform
- **Docusaurus**: Static site generator for documentation
- **VitePress**: Vue-powered static site generator
- **MkDocs**: Python-based documentation generator
- **GitHub Wiki**: Simple wiki system

#### API Documentation
- **Swagger/OpenAPI**: REST API documentation
- **Postman**: API testing and documentation
- **Insomnia**: API client with documentation features
- **GraphQL Playground**: GraphQL API explorer

### Documentation Automation

#### Pre-commit Hooks
```bash
# Example pre-commit hook to ensure documentation
#!/bin/bash
# Check if documentation is up-to-date
npm run docs:check || exit 1
```

#### CI/CD Integration
```yaml
# Example GitHub Actions workflow
name: Documentation
on: [push, pull_request]
jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Generate Documentation
        run: npm run docs:generate
      - name: Deploy Documentation
        run: npm run docs:deploy
```

## Getting Started

1. **Choose Your Tools**: Select appropriate documentation tools for your stack
2. **Set Up Templates**: Adapt the templates above for your specific needs
3. **Document As You Code**: Write documentation alongside code development
4. **Review and Update**: Regularly review and update documentation
5. **Automate**: Set up automation to keep documentation current

## Maintenance

- **Regular Reviews**: Schedule quarterly documentation reviews
- **Version Control**: Keep documentation in version control with code
- **User Feedback**: Collect and act on user feedback
- **Metrics**: Track documentation usage and effectiveness
- **Updates**: Update documentation with every code change

---

This guide provides a foundation for comprehensive documentation. Adapt these templates and practices to fit your specific project needs and team preferences.