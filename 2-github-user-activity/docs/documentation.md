# Architecture Documentation

## System Overview

The GitHub User Activity CLI is a modular Python application that fetches and displays recent GitHub activity for any user. The system follows a clean architecture pattern with clear separation of concerns.

## Architecture Diagram

```yml
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   CLI Layer     │    │  Business Logic │    │   Data Layer    │
│                 │    │                 │    │                 │
│ ┌─────────────┐ │    │ ┌─────────────┐ │    │ ┌─────────────┐ │
│ │   main.py   │ │───▶│ │github_api.py│ │───▶│ │  cache.py   │ │
│ └─────────────┘ │    │ └─────────────┘ │    │ └─────────────┘ │
│                 │    │                 │    │                 │
│ ┌─────────────┐ │    │ ┌─────────────┐ │    │ ┌─────────────┐ │
│ │   utils.py  │ │    │ │formatter.py │ │    │ │ File System │ │
│ └─────────────┘ │    │ └─────────────┘ │    │ └─────────────┘ │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  User Input     │    │  Data Processing │    │  Cache Storage  │
│  Validation     │    │  & Formatting    │    │  & Retrieval    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Component Architecture

### 1. Presentation Layer (CLI)

#### main.py

- **Responsibility**: Entry point and user interface
- **Functions**:
  - `validate_args()`: Command line argument validation
  - `main()`: Application orchestration
- **Dependencies**: `github_api`, `formatter`, `utils`
- **Design Pattern**: Facade pattern

#### utils.py

- **Responsibility**: Input validation and utilities
- **Functions**:
  - `validate_name()`: Username format validation
  - `rate_limit()`: Rate limit handling
- **Design Pattern**: Utility pattern

### 2. Business Logic Layer

#### github_api.py

- **Responsibility**: GitHub API integration and caching orchestration
- **Functions**:
  - `gh_activity()`: Direct GitHub API calls
  - `get_user_activity()`: Cached API calls
- **Dependencies**: `cache`, `urllib`, `json`
- **Design Pattern**: Strategy pattern (cache vs API)

#### formatter.py

- **Responsibility**: Data formatting and display
- **Functions**:
  - `format_event()`: Individual event formatting
  - `format_activity()`: Activity list formatting
- **Dependencies**: `datetime`
- **Design Pattern**: Template method pattern

### 3. Data Layer

#### cache.py

- **Responsibility**: Cache management and storage
- **Functions**:
  - `save_cache()`: Store API responses
  - `load_cache()`: Retrieve cached data
  - `get_cache_key()`: Generate cache file paths
- **Dependencies**: `json`, `pathlib`, `datetime`
- **Design Pattern**: Repository pattern

## Data Flow Architecture

### Request Flow

```yml
1. User Input → main.py
2. Validation → utils.py
3. API Call → github_api.py
4. Cache Check → cache.py
5. API Request → GitHub API
6. Response Processing → github_api.py
7. Cache Storage → cache.py
8. Data Formatting → formatter.py
9. Output Display → main.py
```

### Cache Flow

```yml
1. Cache Request → cache.py
2. File Existence Check → File System
3. Timestamp Validation → cache.py
4. Data Retrieval → File System
5. Cache Update → cache.py
6. File Storage → File System
```

## Design Patterns Used

### 1. Facade Pattern

- **Location**: `main.py`
- **Purpose**: Simplified interface to complex subsystem
- **Benefits**: Easy-to-use CLI interface

### 2. Strategy Pattern

- **Location**: `github_api.py`
- **Purpose**: Choose between cache and API strategies
- **Benefits**: Flexible data retrieval methods

### 3. Repository Pattern

- **Location**: `cache.py`
- **Purpose**: Abstract cache storage operations
- **Benefits**: Testable and swappable storage

### 4. Template Method Pattern

- **Location**: `formatter.py`
- **Purpose**: Standardized event formatting
- **Benefits**: Consistent output format

### 5. Utility Pattern

- **Location**: `utils.py`
- **Purpose**: Reusable helper functions
- **Benefits**: Code reusability

## SOLID Principles Implementation

### Single Responsibility Principle (SRP)

- Each module has one primary responsibility
- `main.py`: CLI orchestration
- `github_api.py`: API communication
- `cache.py`: Cache management
- `formatter.py`: Data formatting
- `utils.py`: Validation and utilities

### Open/Closed Principle (OCP)

- Cache system is open for extension (new storage types)
- Event formatting is open for extension (new event types)
- Core logic closed for modification

### Liskov Substitution Principle (LSP)

- Cache implementations can be substituted
- Formatter implementations can be substituted

### Interface Segregation Principle (ISP)

- Small, focused interfaces
- No fat interfaces with multiple responsibilities

### Dependency Inversion Principle (DIP)

- High-level modules don't depend on low-level modules
- Both depend on abstractions (functions/interfaces)

## Error Handling Architecture

### Error Types

```yml
┌─────────────────┐
│  Input Errors   │ → Validation Errors
└─────────────────┘

┌─────────────────┐
│ Network Errors  │ → HTTP/URL Errors
└─────────────────┘

┌─────────────────┐
│  Data Errors    │ → JSON Parse Errors
└─────────────────┘

┌─────────────────┐
│ System Errors   │ → File System Errors
└─────────────────┘
```

### Error Handling Strategy

1. **Prevention**: Input validation
2. **Detection**: Try-catch blocks
3. **Recovery**: Graceful degradation
4. **Reporting**: User-friendly messages

## Performance Architecture

### Caching Strategy

- **Cache-Aside Pattern**: Application manages cache
- **Time-Based Expiration**: 5-minute TTL
- **Write-Through**: Immediate cache updates
- **Cache Invalidation**: Automatic expiration

### Memory Management

- **Streaming**: Process data incrementally
- **Minimal Storage**: Only essential data cached
- **Garbage Collection**: Automatic cleanup

### Network Optimization

- **Connection Reuse**: Single connection per request
- **Request Headers**: Proper User-Agent
- **Rate Limiting**: Respect API limits

## Security Architecture

### Input Validation

- **Username Format**: Regex validation
- **Length Limits**: Maximum 39 characters
- **Character Restrictions**: Alphanumeric, hyphens, underscores

### Data Privacy

- **Public Data Only**: No authentication required
- **Local Storage**: Cache stored locally
- **No Sensitive Data**: Only public GitHub events

### Error Information

- **Sanitized Errors**: No sensitive information leaked
- **User-Friendly**: Clear error messages
- **Debug Information**: Separate debug mode

## Scalability Architecture

### Horizontal Scaling

- **Stateless Design**: Each request independent
- **Cache Distribution**: Can be distributed across systems
- **Load Balancing**: Multiple instances possible

### Vertical Scaling

- **Memory Efficiency**: Minimal memory footprint
- **CPU Optimization**: Efficient data processing
- **I/O Optimization**: Async operations possible

## Testing Architecture

### Unit Testing

- **Module Isolation**: Each module tested independently
- **Mock Dependencies**: External dependencies mocked
- **Edge Cases**: Boundary conditions tested

### Integration Testing

- **API Integration**: Real GitHub API testing
- **Cache Integration**: File system testing
- **End-to-End**: Complete workflow testing

### Performance Testing

- **Load Testing**: Multiple concurrent requests
- **Cache Performance**: Hit/miss ratios
- **Memory Testing**: Memory usage patterns

## Deployment Architecture

### Local Deployment

- **Single File**: All code in single directory
- **No Dependencies**: Standard library only
- **Cross-Platform**: Works on Windows, Linux, macOS

### Container Deployment

- **Docker Ready**: Can be containerized
- **Environment Isolated**: Clean runtime environment
- **Scalable**: Multiple containers possible

## Monitoring Architecture

### Logging Strategy

- **Structured Logging**: Consistent log format
- **Log Levels**: Debug, Info, Warning, Error
- **Performance Metrics**: Response times, cache hit ratios

### Health Checks

- **API Availability**: GitHub API status
- **Cache Health**: File system accessibility
- **System Health**: Memory and CPU usage

## Future Architecture Considerations

### Potential Enhancements

- **Database Backend**: Replace file-based cache
- **API Authentication**: Support for private repositories
- **Real-time Updates**: WebSocket integration
- **Web Interface**: Browser-based UI
- **API Rate Limiting**: Advanced rate limit handling

### Architecture Evolution

- **Microservices**: Split into separate services
- **Event-Driven**: Message queue integration
- **Cloud Native**: Kubernetes deployment
- **Serverless**: Function-based deployment
