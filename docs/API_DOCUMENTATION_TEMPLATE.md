# API Documentation Template

This template provides a standardized format for documenting APIs. Copy and customize sections as needed for your specific API.

## API Overview

**Base URL**: `https://api.yourservice.com/v1`  
**Protocol**: HTTPS  
**Authentication**: Bearer Token / API Key / OAuth 2.0  
**Rate Limiting**: 1000 requests per hour per user  
**Response Format**: JSON  

### Supported Operations
- User Management
- Data Processing
- File Operations
- Notifications

---

## Authentication

### Bearer Token Authentication

Include the authorization header with every request:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### Example
```bash
curl -H "Authorization: Bearer abc123def456" \
     https://api.yourservice.com/v1/users/me
```

### Getting an Access Token

**Endpoint**: `POST /auth/login`

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Response**:
```json
{
  "access_token": "abc123def456",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "refresh123token456"
}
```

---

## Error Handling

### Standard Error Response Format

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {
      "field": "Additional error details"
    },
    "timestamp": "2023-01-01T00:00:00Z",
    "request_id": "req_12345"
  }
}
```

### HTTP Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Request successful |
| 201 | Created | Resource created successfully |
| 400 | Bad Request | Invalid request parameters |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource not found |
| 409 | Conflict | Resource already exists |
| 422 | Unprocessable Entity | Validation errors |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error |

---

## Endpoints

### Users

#### Get Current User

**Endpoint**: `GET /users/me`  
**Description**: Retrieves the authenticated user's profile information.  
**Authentication**: Required  

**Response** (200 OK):
```json
{
  "id": "user_123",
  "email": "user@example.com",
  "name": "John Doe",
  "role": "user",
  "created_at": "2023-01-01T00:00:00Z",
  "last_login": "2023-01-15T10:30:00Z",
  "preferences": {
    "timezone": "UTC",
    "language": "en"
  }
}
```

**Example**:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
     https://api.yourservice.com/v1/users/me
```

#### Update User Profile

**Endpoint**: `PUT /users/me`  
**Description**: Updates the authenticated user's profile information.  
**Authentication**: Required  

**Request Body**:
```json
{
  "name": "Jane Doe",
  "preferences": {
    "timezone": "America/New_York",
    "language": "en"
  }
}
```

**Response** (200 OK):
```json
{
  "id": "user_123",
  "email": "user@example.com",
  "name": "Jane Doe",
  "role": "user",
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-16T14:20:00Z",
  "preferences": {
    "timezone": "America/New_York",
    "language": "en"
  }
}
```

**Example**:
```bash
curl -X PUT \
     -H "Authorization: Bearer YOUR_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"name": "Jane Doe"}' \
     https://api.yourservice.com/v1/users/me
```

### Resources

#### List Resources

**Endpoint**: `GET /resources`  
**Description**: Retrieves a paginated list of resources.  
**Authentication**: Required  

**Query Parameters**:
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `page` | integer | No | 1 | Page number (1-based) |
| `limit` | integer | No | 20 | Items per page (max: 100) |
| `sort` | string | No | created_at | Sort field (created_at, name, updated_at) |
| `order` | string | No | desc | Sort order (asc, desc) |
| `filter` | string | No | - | Filter by name or description |
| `status` | string | No | - | Filter by status (active, inactive, draft) |

**Response** (200 OK):
```json
{
  "data": [
    {
      "id": "res_123",
      "name": "Sample Resource",
      "description": "A sample resource for testing",
      "status": "active",
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-15T10:30:00Z",
      "owner": {
        "id": "user_123",
        "name": "John Doe"
      }
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "pages": 8,
    "has_next": true,
    "has_prev": false
  }
}
```

**Example**:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
     "https://api.yourservice.com/v1/resources?page=1&limit=10&status=active"
```

#### Create Resource

**Endpoint**: `POST /resources`  
**Description**: Creates a new resource.  
**Authentication**: Required  

**Request Body**:
```json
{
  "name": "New Resource",
  "description": "Description of the new resource",
  "status": "draft",
  "metadata": {
    "category": "example",
    "tags": ["tag1", "tag2"]
  }
}
```

**Response** (201 Created):
```json
{
  "id": "res_456",
  "name": "New Resource",
  "description": "Description of the new resource",
  "status": "draft",
  "created_at": "2023-01-16T15:00:00Z",
  "updated_at": "2023-01-16T15:00:00Z",
  "owner": {
    "id": "user_123",
    "name": "John Doe"
  },
  "metadata": {
    "category": "example",
    "tags": ["tag1", "tag2"]
  }
}
```

**Validation Rules**:
- `name`: Required, 1-255 characters
- `description`: Optional, max 1000 characters
- `status`: Must be one of: draft, active, inactive
- `metadata.tags`: Optional array, max 10 tags

**Example**:
```bash
curl -X POST \
     -H "Authorization: Bearer YOUR_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "New Resource",
       "description": "Description of the new resource",
       "status": "draft"
     }' \
     https://api.yourservice.com/v1/resources
```

#### Get Resource

**Endpoint**: `GET /resources/{id}`  
**Description**: Retrieves a specific resource by ID.  
**Authentication**: Required  

**Path Parameters**:
- `id` (string, required): The unique identifier of the resource

**Response** (200 OK):
```json
{
  "id": "res_123",
  "name": "Sample Resource",
  "description": "A sample resource for testing",
  "status": "active",
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-15T10:30:00Z",
  "owner": {
    "id": "user_123",
    "name": "John Doe",
    "email": "john@example.com"
  },
  "metadata": {
    "category": "example",
    "tags": ["tag1", "tag2"],
    "version": "1.0.0"
  },
  "permissions": {
    "can_edit": true,
    "can_delete": true,
    "can_share": true
  }
}
```

**Example**:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
     https://api.yourservice.com/v1/resources/res_123
```

#### Update Resource

**Endpoint**: `PUT /resources/{id}`  
**Description**: Updates an existing resource.  
**Authentication**: Required  

**Path Parameters**:
- `id` (string, required): The unique identifier of the resource

**Request Body**:
```json
{
  "name": "Updated Resource Name",
  "description": "Updated description",
  "status": "active",
  "metadata": {
    "category": "updated",
    "tags": ["updated-tag"]
  }
}
```

**Response** (200 OK):
```json
{
  "id": "res_123",
  "name": "Updated Resource Name",
  "description": "Updated description",
  "status": "active",
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-16T16:00:00Z",
  "owner": {
    "id": "user_123",
    "name": "John Doe"
  },
  "metadata": {
    "category": "updated",
    "tags": ["updated-tag"]
  }
}
```

**Example**:
```bash
curl -X PUT \
     -H "Authorization: Bearer YOUR_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Updated Resource Name",
       "status": "active"
     }' \
     https://api.yourservice.com/v1/resources/res_123
```

#### Delete Resource

**Endpoint**: `DELETE /resources/{id}`  
**Description**: Deletes a resource.  
**Authentication**: Required  

**Path Parameters**:
- `id` (string, required): The unique identifier of the resource

**Response** (204 No Content):
No response body.

**Example**:
```bash
curl -X DELETE \
     -H "Authorization: Bearer YOUR_TOKEN" \
     https://api.yourservice.com/v1/resources/res_123
```

---

## SDK Examples

### JavaScript/Node.js

```javascript
const ApiClient = require('./api-client');

const client = new ApiClient({
  baseURL: 'https://api.yourservice.com/v1',
  accessToken: 'YOUR_ACCESS_TOKEN'
});

// Get current user
const user = await client.users.me();
console.log('Current user:', user);

// List resources
const resources = await client.resources.list({
  page: 1,
  limit: 10,
  status: 'active'
});
console.log('Resources:', resources);

// Create a resource
const newResource = await client.resources.create({
  name: 'My Resource',
  description: 'Created via SDK',
  status: 'draft'
});
console.log('Created resource:', newResource);
```

### Python

```python
import requests
from typing import Dict, List, Optional

class APIClient:
    def __init__(self, base_url: str, access_token: str):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
    
    def get_user(self) -> Dict:
        response = requests.get(
            f'{self.base_url}/users/me',
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
    
    def list_resources(self, page: int = 1, limit: int = 20, 
                      status: Optional[str] = None) -> Dict:
        params = {'page': page, 'limit': limit}
        if status:
            params['status'] = status
        
        response = requests.get(
            f'{self.base_url}/resources',
            headers=self.headers,
            params=params
        )
        response.raise_for_status()
        return response.json()

# Usage
client = APIClient(
    'https://api.yourservice.com/v1',
    'YOUR_ACCESS_TOKEN'
)

user = client.get_user()
print(f"Current user: {user}")

resources = client.list_resources(status='active')
print(f"Active resources: {resources}")
```

---

## Rate Limiting

**Limits**:
- **Standard users**: 1,000 requests per hour
- **Premium users**: 10,000 requests per hour
- **Enterprise users**: 100,000 requests per hour

**Headers**:
Every response includes rate limiting headers:
```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1674745200
```

**Rate Limit Exceeded Response** (429):
```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Try again later.",
    "details": {
      "limit": 1000,
      "remaining": 0,
      "reset": 1674745200
    }
  }
}
```

---

## Webhooks

### Setup

**Endpoint**: `POST /webhooks`  
**Description**: Creates a webhook subscription.

**Request Body**:
```json
{
  "url": "https://your-app.com/webhooks",
  "events": ["resource.created", "resource.updated", "resource.deleted"],
  "secret": "your_webhook_secret"
}
```

### Event Types

| Event | Description |
|-------|-------------|
| `resource.created` | Triggered when a resource is created |
| `resource.updated` | Triggered when a resource is updated |
| `resource.deleted` | Triggered when a resource is deleted |
| `user.registered` | Triggered when a user registers |

### Webhook Payload

```json
{
  "event": "resource.created",
  "timestamp": "2023-01-16T16:00:00Z",
  "data": {
    "id": "res_456",
    "name": "New Resource",
    "status": "draft",
    "owner": {
      "id": "user_123",
      "name": "John Doe"
    }
  }
}
```

### Webhook Verification

Verify webhook authenticity using HMAC-SHA256:

```javascript
const crypto = require('crypto');

function verifyWebhook(payload, signature, secret) {
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');
  
  return `sha256=${expectedSignature}` === signature;
}
```

---

## Testing

### Postman Collection

Download our [Postman collection](./postman_collection.json) for easy API testing.

### Example Test Scripts

```javascript
// Test authentication
pm.test("Authentication successful", function () {
    pm.response.to.have.status(200);
    pm.expect(pm.response.json()).to.have.property('access_token');
});

// Test resource creation
pm.test("Resource created successfully", function () {
    pm.response.to.have.status(201);
    const response = pm.response.json();
    pm.expect(response).to.have.property('id');
    pm.expect(response.name).to.equal('New Resource');
});
```

### cURL Test Suite

```bash
#!/bin/bash

# Set your access token
ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
BASE_URL="https://api.yourservice.com/v1"

# Test authentication
echo "Testing authentication..."
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" \
     "$BASE_URL/users/me" | jq '.'

# Test resource listing
echo "Testing resource listing..."
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" \
     "$BASE_URL/resources?limit=5" | jq '.data | length'

# Test resource creation
echo "Testing resource creation..."
curl -s -X POST \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"name": "Test Resource", "status": "draft"}' \
     "$BASE_URL/resources" | jq '.id'
```

---

## Changelog

### Version 1.2.0 (2023-01-16)
- Added webhook support
- Enhanced error responses with request IDs
- Improved rate limiting headers

### Version 1.1.0 (2023-01-01)
- Added resource metadata support
- Improved pagination
- Added filtering and sorting options

### Version 1.0.0 (2022-12-01)
- Initial API release
- Basic CRUD operations for users and resources
- Authentication with Bearer tokens

---

## Support

**Documentation**: [https://docs.yourservice.com](https://docs.yourservice.com)  
**API Status**: [https://status.yourservice.com](https://status.yourservice.com)  
**Support Email**: api-support@yourservice.com  
**Developer Forum**: [https://forum.yourservice.com](https://forum.yourservice.com)  

For bug reports and feature requests, please use our [GitHub Issues](https://github.com/yourorg/api/issues).