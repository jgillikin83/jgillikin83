# Function Documentation Template

This template provides standardized formats for documenting functions across different programming languages.

## General Function Documentation Structure

### Basic Template

```markdown
## Function: functionName

**Description**: Brief description of what the function does and its purpose.

**Signature**: 
```language
returnType functionName(paramType1 param1, paramType2 param2, ...options)
```

### Parameters

- `param1` (paramType1, required): Description of the first parameter
- `param2` (paramType2, optional): Description of the second parameter, default: value
- `...options` (object, optional): Additional configuration options

### Returns

- `returnType`: Description of what is returned, including possible values or structure

### Throws/Exceptions

- `ExceptionType`: When this exception is thrown and why

### Examples

#### Basic Usage
```language
// Example of basic usage
const result = functionName(value1, value2);
console.log(result);
```

#### Advanced Usage
```language
// Example with all parameters and error handling
try {
  const result = functionName(value1, value2, { option: true });
  // Handle success
} catch (error) {
  // Handle error
}
```

### Performance Notes

- Time complexity: O(n)
- Space complexity: O(1)
- Performance considerations or optimizations

### Notes

- Important considerations
- Edge cases
- Browser/environment compatibility
- Version information
```

---

## Language-Specific Templates

### JavaScript/TypeScript

```markdown
## Function: processUserData

**Description**: Processes and validates user data, returning a normalized user object with computed fields.

**Signature**: 
```typescript
function processUserData(
  userData: UserInput, 
  options?: ProcessingOptions
): Promise<ProcessedUser>
```

### Parameters

- `userData` (UserInput, required): Raw user data object containing:
  - `name` (string): User's full name
  - `email` (string): User's email address
  - `age` (number): User's age in years
  - `preferences` (object, optional): User preferences
- `options` (ProcessingOptions, optional): Processing configuration:
  - `validateEmail` (boolean): Whether to validate email format (default: true)
  - `computeMetadata` (boolean): Whether to compute additional metadata (default: false)
  - `strictMode` (boolean): Enable strict validation (default: false)

### Returns

- `Promise<ProcessedUser>`: Promise that resolves to a processed user object:
  ```typescript
  {
    id: string;
    name: string;
    email: string;
    age: number;
    isAdult: boolean;
    preferences: UserPreferences;
    metadata?: UserMetadata;
    processedAt: Date;
  }
  ```

### Throws

- `ValidationError`: When user data fails validation
- `TypeError`: When parameter types are incorrect
- `Error`: When processing fails due to system issues

### Examples

#### Basic Usage
```typescript
const userData = {
  name: 'John Doe',
  email: 'john@example.com',
  age: 25
};

const processedUser = await processUserData(userData);
console.log(processedUser.isAdult); // true
```

#### With Options
```typescript
const userData = {
  name: 'Jane Smith',
  email: 'jane@example.com',
  age: 30,
  preferences: { theme: 'dark' }
};

const options = {
  validateEmail: true,
  computeMetadata: true,
  strictMode: false
};

try {
  const processedUser = await processUserData(userData, options);
  console.log('Processing successful:', processedUser);
} catch (error) {
  if (error instanceof ValidationError) {
    console.error('Validation failed:', error.message);
  } else {
    console.error('Processing failed:', error);
  }
}
```

#### Error Handling
```typescript
try {
  const result = await processUserData(invalidData);
} catch (error) {
  switch (error.constructor) {
    case ValidationError:
      // Handle validation errors
      console.error('Invalid data:', error.details);
      break;
    case TypeError:
      // Handle type errors
      console.error('Wrong data type:', error.message);
      break;
    default:
      // Handle other errors
      console.error('Unexpected error:', error);
  }
}
```

### Performance Notes

- Time complexity: O(1) for basic processing, O(n) when computeMetadata is enabled
- Space complexity: O(1)
- Uses async/await for non-blocking operation
- Email validation adds ~5ms processing time

### Notes

- Requires Node.js 14+ or modern browser environment
- Email validation uses RFC 5322 standard
- Metadata computation includes timezone detection and locale inference
- Function is pure except for Date generation
```

### Python

```markdown
## Function: calculate_statistics

**Description**: Calculates descriptive statistics for a dataset including mean, median, mode, and standard deviation.

**Signature**: 
```python
def calculate_statistics(
    data: List[Union[int, float]], 
    precision: int = 2,
    include_mode: bool = True
) -> Dict[str, Union[float, List[float]]]
```

### Parameters

- `data` (List[Union[int, float]], required): List of numeric values to analyze
- `precision` (int, optional): Number of decimal places for results (default: 2)
- `include_mode` (bool, optional): Whether to calculate mode (default: True)

### Returns

- `Dict[str, Union[float, List[float]]]`: Dictionary containing statistical measures:
  ```python
  {
      'mean': float,
      'median': float,
      'mode': List[float],  # if include_mode is True
      'std_dev': float,
      'variance': float,
      'min': float,
      'max': float,
      'count': int
  }
  ```

### Raises

- `ValueError`: When data list is empty or contains non-numeric values
- `TypeError`: When parameters are of incorrect type
- `OverflowError`: When numbers are too large for calculation

### Examples

#### Basic Usage
```python
data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
stats = calculate_statistics(data)
print(f"Mean: {stats['mean']}")  # Mean: 5.0
print(f"Median: {stats['median']}")  # Median: 5.5
```

#### With Custom Precision
```python
data = [1.123, 2.456, 3.789, 4.012]
stats = calculate_statistics(data, precision=3)
print(f"Mean: {stats['mean']}")  # Mean: 2.845
```

#### Without Mode Calculation
```python
large_dataset = list(range(10000))
stats = calculate_statistics(large_dataset, include_mode=False)
# Faster processing when mode is not needed
```

#### Error Handling
```python
try:
    stats = calculate_statistics([])
except ValueError as e:
    print(f"Error: {e}")  # Error: Data list cannot be empty

try:
    stats = calculate_statistics(['a', 'b', 'c'])
except ValueError as e:
    print(f"Error: {e}")  # Error: All values must be numeric
```

### Performance Notes

- Time complexity: O(n log n) due to sorting for median calculation
- Space complexity: O(n) for mode calculation, O(1) otherwise
- Mode calculation can be disabled for better performance on large datasets
- Uses NumPy-compatible algorithms for numerical stability

### Notes

- Function handles both integers and floating-point numbers
- Mode returns a list as there can be multiple modal values
- Uses Bessel's correction (n-1) for sample standard deviation
- Handles edge cases like single-value datasets gracefully
- Compatible with Python 3.7+
```

### Java

```markdown
## Method: validateAndParseUser

**Description**: Validates user input data and parses it into a User object with proper type conversion and validation.

**Signature**: 
```java
public static User validateAndParseUser(
    Map<String, Object> userData, 
    ValidationConfig config
) throws ValidationException, ParseException
```

### Parameters

- `userData` (Map<String, Object>, required): Raw user data containing:
  - `"name"`: String representing user's full name
  - `"email"`: String containing email address
  - `"age"`: Integer or String representing age
  - `"active"`: Boolean or String representing account status
- `config` (ValidationConfig, required): Validation configuration object:
  - `strictEmailValidation`: boolean flag for email validation
  - `minAge`: minimum allowed age
  - `maxAge`: maximum allowed age
  - `requiredFields`: Set<String> of required field names

### Returns

- `User`: Validated and parsed User object with properties:
  - `name`: String (trimmed and validated)
  - `email`: String (normalized and validated)
  - `age`: int (parsed and range-checked)
  - `active`: boolean (parsed from various input types)
  - `createdAt`: LocalDateTime (automatically set)

### Throws

- `ValidationException`: When validation rules are violated
- `ParseException`: When data cannot be parsed to expected types
- `IllegalArgumentException`: When required parameters are null

### Examples

#### Basic Usage
```java
Map<String, Object> userData = new HashMap<>();
userData.put("name", "John Doe");
userData.put("email", "john@example.com");
userData.put("age", "25");
userData.put("active", true);

ValidationConfig config = new ValidationConfig.Builder()
    .withStrictEmailValidation(true)
    .withAgeRange(18, 100)
    .withRequiredFields(Set.of("name", "email"))
    .build();

try {
    User user = UserValidator.validateAndParseUser(userData, config);
    System.out.println("User created: " + user.getName());
} catch (ValidationException e) {
    System.err.println("Validation failed: " + e.getMessage());
}
```

#### With Custom Configuration
```java
ValidationConfig relaxedConfig = new ValidationConfig.Builder()
    .withStrictEmailValidation(false)
    .withAgeRange(0, 150)
    .withRequiredFields(Set.of("name"))
    .build();

User user = UserValidator.validateAndParseUser(userData, relaxedConfig);
```

#### Error Handling
```java
try {
    User user = UserValidator.validateAndParseUser(userData, config);
    // Process successful validation
} catch (ValidationException e) {
    // Handle validation errors
    for (String error : e.getValidationErrors()) {
        System.err.println("Validation error: " + error);
    }
} catch (ParseException e) {
    // Handle parsing errors
    System.err.println("Parse error: " + e.getMessage());
} catch (IllegalArgumentException e) {
    // Handle null parameters
    System.err.println("Invalid arguments: " + e.getMessage());
}
```

### Performance Notes

- Time complexity: O(1) for most validations, O(n) for email regex validation
- Space complexity: O(1)
- Email validation regex compilation is cached for better performance
- Type conversion uses efficient parsing methods

### Notes

- Method is thread-safe and can be used concurrently
- Email validation supports international domain names when strict mode is disabled
- Age parsing accepts both integer and string inputs
- Boolean parsing recognizes "true", "false", "1", "0", "yes", "no" (case-insensitive)
- Requires Java 8+ for LocalDateTime support
```

### Go

```markdown
## Function: ProcessPayment

**Description**: Processes a payment transaction with validation, fraud detection, and external payment gateway integration.

**Signature**: 
```go
func ProcessPayment(
    ctx context.Context, 
    payment *Payment, 
    options *ProcessingOptions
) (*PaymentResult, error)
```

### Parameters

- `ctx` (context.Context, required): Context for request cancellation and timeout
- `payment` (*Payment, required): Payment information struct containing:
  - `Amount`: int64 (amount in cents)
  - `Currency`: string (3-letter currency code)
  - `CardToken`: string (tokenized card information)
  - `CustomerID`: string (unique customer identifier)
  - `Description`: string (payment description)
- `options` (*ProcessingOptions, optional): Processing configuration:
  - `FraudCheck`: bool (enable fraud detection, default: true)
  - `Gateway`: string (payment gateway to use, default: "stripe")
  - `Idempotent`: bool (ensure idempotent processing, default: true)
  - `Metadata`: map[string]string (additional metadata)

### Returns

- `*PaymentResult`: Successful payment result containing:
  - `TransactionID`: string (unique transaction identifier)
  - `Status`: PaymentStatus (SUCCESS, PENDING, FAILED)
  - `GatewayResponse`: *GatewayResponse (raw gateway response)
  - `ProcessedAt`: time.Time (processing timestamp)
  - `Fees`: int64 (processing fees in cents)
- `error`: Error information if processing fails

### Errors

- `ErrInvalidPayment`: When payment data is invalid
- `ErrFraudDetected`: When fraud detection triggers
- `ErrGatewayTimeout`: When payment gateway times out
- `ErrInsufficientFunds`: When payment method has insufficient funds
- `context.Canceled`: When context is canceled
- `context.DeadlineExceeded`: When context timeout is reached

### Examples

#### Basic Usage
```go
ctx := context.Background()
payment := &Payment{
    Amount:     10000, // $100.00
    Currency:   "USD",
    CardToken:  "tok_1234567890",
    CustomerID: "cust_abcdefgh",
    Description: "Order #12345",
}

result, err := ProcessPayment(ctx, payment, nil)
if err != nil {
    log.Printf("Payment failed: %v", err)
    return
}

fmt.Printf("Payment successful: %s\n", result.TransactionID)
```

#### With Custom Options
```go
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()

options := &ProcessingOptions{
    FraudCheck: true,
    Gateway:    "paypal",
    Idempotent: true,
    Metadata: map[string]string{
        "order_id": "12345",
        "source":   "mobile_app",
    },
}

result, err := ProcessPayment(ctx, payment, options)
if err != nil {
    switch {
    case errors.Is(err, ErrFraudDetected):
        // Handle fraud detection
        log.Printf("Fraud detected: %v", err)
    case errors.Is(err, ErrGatewayTimeout):
        // Handle timeout
        log.Printf("Gateway timeout: %v", err)
    case errors.Is(err, context.DeadlineExceeded):
        // Handle context timeout
        log.Printf("Request timeout: %v", err)
    default:
        // Handle other errors
        log.Printf("Payment error: %v", err)
    }
    return
}
```

#### Error Handling with Type Assertion
```go
result, err := ProcessPayment(ctx, payment, options)
if err != nil {
    var paymentErr *PaymentError
    if errors.As(err, &paymentErr) {
        // Handle typed payment error
        fmt.Printf("Payment failed: %s (code: %s)\n", 
            paymentErr.Message, paymentErr.Code)
    } else {
        // Handle generic error
        fmt.Printf("Unexpected error: %v\n", err)
    }
    return
}
```

### Performance Notes

- Time complexity: O(1) for processing, O(n) for fraud detection rules
- Space complexity: O(1)
- Typical processing time: 200-500ms depending on gateway
- Fraud detection adds ~50ms overhead
- Uses connection pooling for gateway requests

### Notes

- Function is goroutine-safe and can handle concurrent requests
- Context timeout should be set appropriately (recommended: 30s)
- Payment amounts are handled in cents to avoid floating-point precision issues
- Idempotent processing prevents duplicate charges using payment fingerprinting
- Supports multiple payment gateways through adapter pattern
- Requires Go 1.16+ for context improvements
```

---

## Async/Promise Documentation

### JavaScript Async Function

```markdown
## Function: fetchUserData

**Description**: Asynchronously fetches user data from multiple sources and combines them into a unified user profile.

**Signature**: 
```typescript
async function fetchUserData(
    userId: string, 
    sources: DataSource[] = ['profile', 'preferences', 'activity'],
    options?: FetchOptions
): Promise<CombinedUserData>
```

### Parameters

- `userId` (string, required): Unique identifier for the user
- `sources` (DataSource[], optional): Array of data sources to fetch from:
  - `'profile'`: Basic profile information
  - `'preferences'`: User preferences and settings  
  - `'activity'`: Recent activity data
  - `'social'`: Social connections and data
- `options` (FetchOptions, optional): Request configuration:
  - `timeout`: number (request timeout in ms, default: 5000)
  - `retries`: number (retry attempts, default: 3)
  - `cache`: boolean (use cached data if available, default: true)
  - `parallel`: boolean (fetch sources in parallel, default: true)

### Returns

- `Promise<CombinedUserData>`: Promise resolving to combined user data:
  ```typescript
  {
    userId: string;
    profile?: UserProfile;
    preferences?: UserPreferences;
    activity?: ActivityData;
    social?: SocialData;
    fetchedAt: Date;
    sources: DataSource[];
    cached: boolean;
  }
  ```

### Rejects

- `UserNotFoundError`: When user ID doesn't exist
- `TimeoutError`: When request exceeds timeout limit
- `NetworkError`: When network request fails
- `ValidationError`: When user ID format is invalid
- `RateLimitError`: When rate limit is exceeded

### Examples

#### Basic Usage
```typescript
try {
  const userData = await fetchUserData('user_123');
  console.log('User profile:', userData.profile);
} catch (error) {
  console.error('Failed to fetch user data:', error);
}
```

#### Selective Data Sources
```typescript
const userData = await fetchUserData(
  'user_123', 
  ['profile', 'preferences']
);
// Only fetches profile and preferences, skipping activity and social
```

#### With Configuration Options
```typescript
const options = {
  timeout: 10000,     // 10 second timeout
  retries: 5,         // 5 retry attempts
  cache: false,       // Always fetch fresh data
  parallel: false     // Fetch sources sequentially
};

try {
  const userData = await fetchUserData('user_123', undefined, options);
  console.log('Fresh user data:', userData);
} catch (error) {
  if (error instanceof TimeoutError) {
    console.error('Request timed out after 10 seconds');
  } else if (error instanceof UserNotFoundError) {
    console.error('User not found');
  }
}
```

#### Parallel Processing with Error Handling
```typescript
const userIds = ['user_1', 'user_2', 'user_3'];

const results = await Promise.allSettled(
  userIds.map(id => fetchUserData(id))
);

results.forEach((result, index) => {
  if (result.status === 'fulfilled') {
    console.log(`User ${userIds[index]}:`, result.value);
  } else {
    console.error(`Failed to fetch ${userIds[index]}:`, result.reason);
  }
});
```

### Performance Notes

- Parallel fetching reduces total time by ~60% compared to sequential
- Caching reduces subsequent requests by ~90%
- Each data source adds ~100-300ms to total fetch time
- Network requests are automatically retried with exponential backoff

### Notes

- Function uses AbortController for timeout handling
- Cached data expires after 5 minutes by default
- Rate limiting applies per user (100 requests/hour)
- Compatible with Node.js 14+ and modern browsers
- Uses fetch API with automatic JSON parsing
```

---

## Class Method Documentation

### Python Class Method

```markdown
## Method: DataProcessor.transform

**Description**: Transforms raw data through a pipeline of configurable processing steps with validation and error recovery.

**Signature**: 
```python
def transform(
    self,
    data: Union[Dict, List[Dict]], 
    pipeline: Optional[List[str]] = None,
    **kwargs
) -> TransformResult
```

### Parameters

- `self`: DataProcessor instance with configured transformers
- `data` (Union[Dict, List[Dict]], required): Raw data to transform
  - Single dict: transforms one record
  - List of dicts: transforms multiple records
- `pipeline` (Optional[List[str]], optional): Ordered list of transformation steps
  - If None, uses default pipeline from constructor
  - Available steps: 'validate', 'clean', 'normalize', 'enrich', 'format'
- `**kwargs`: Additional options:
  - `strict` (bool): Stop on first error (default: False)
  - `max_errors` (int): Maximum errors before stopping (default: 100)
  - `skip_invalid` (bool): Skip invalid records (default: True)
  - `batch_size` (int): Processing batch size (default: 1000)

### Returns

- `TransformResult`: Transformation result object:
  ```python
  {
      'data': List[Dict],           # Transformed data
      'errors': List[TransformError], # Processing errors
      'stats': {
          'processed': int,         # Records processed
          'successful': int,        # Successfully transformed
          'failed': int,           # Failed transformations
          'duration': float        # Processing time in seconds
      },
      'pipeline': List[str],       # Pipeline steps used
      'metadata': Dict[str, Any]   # Additional metadata
  }
  ```

### Raises

- `ValidationError`: When data fails initial validation
- `PipelineError`: When pipeline configuration is invalid
- `TransformError`: When transformation step fails critically
- `MemoryError`: When data exceeds available memory

### Examples

#### Basic Single Record Transform
```python
processor = DataProcessor()
raw_data = {
    'name': '  John Doe  ',
    'email': 'JOHN@EXAMPLE.COM',
    'age': '25'
}

result = processor.transform(raw_data)
print(result.data[0])
# Output: {'name': 'John Doe', 'email': 'john@example.com', 'age': 25}
```

#### Batch Processing with Custom Pipeline
```python
processor = DataProcessor()
raw_records = [
    {'name': 'John', 'email': 'john@test.com'},
    {'name': 'Jane', 'email': 'invalid-email'},
    {'name': 'Bob', 'email': 'bob@test.com'}
]

custom_pipeline = ['validate', 'clean', 'normalize']
result = processor.transform(
    raw_records, 
    pipeline=custom_pipeline,
    strict=False,
    skip_invalid=True
)

print(f"Processed: {result.stats['processed']}")
print(f"Successful: {result.stats['successful']}")
print(f"Errors: {len(result.errors)}")
```

#### Error Handling and Recovery
```python
try:
    result = processor.transform(
        large_dataset,
        max_errors=50,
        batch_size=500
    )
    
    if result.errors:
        # Log errors but continue with successful records
        for error in result.errors:
            logger.warning(f"Transform error: {error}")
    
    # Process successful transformations
    for record in result.data:
        save_to_database(record)
        
except ValidationError as e:
    logger.error(f"Data validation failed: {e}")
except MemoryError:
    logger.error("Dataset too large, try smaller batch_size")
except TransformError as e:
    logger.error(f"Critical transform error: {e}")
```

#### Custom Pipeline with Monitoring
```python
import time

def monitor_transform(data, pipeline_steps):
    start_time = time.time()
    
    result = processor.transform(
        data,
        pipeline=pipeline_steps,
        strict=False
    )
    
    duration = time.time() - start_time
    throughput = len(data) / duration
    
    print(f"Transformation Summary:")
    print(f"  Records: {len(data)}")
    print(f"  Duration: {duration:.2f}s")
    print(f"  Throughput: {throughput:.0f} records/sec")
    print(f"  Success Rate: {result.stats['successful'] / result.stats['processed'] * 100:.1f}%")
    
    return result

# Usage
result = monitor_transform(my_data, ['clean', 'normalize', 'enrich'])
```

### Performance Notes

- Time complexity: O(n × m) where n=records, m=pipeline steps
- Space complexity: O(n) for storing transformed data
- Batch processing recommended for datasets > 10,000 records
- Memory usage scales linearly with data size
- Pipeline optimization can improve performance by 40-60%

### Notes

- Method modifies processor state (error counts, statistics)
- Thread-safe for read operations, not for concurrent transforms
- Large datasets automatically use streaming processing
- Custom transformers can be added via `add_transformer()` method
- Supports pandas DataFrames when pandas extra is installed
- Requires Python 3.8+ for typing support
```

---

This template provides comprehensive coverage for documenting functions across different programming paradigms and languages. Adapt the sections and examples to match your specific use case and coding standards.