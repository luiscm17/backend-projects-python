# API Documentation

## GitHub Events API Integration

This document describes how the GitHub User Activity CLI integrates with the GitHub API.

## API Endpoint

### Events API

- **URL**: `https://api.github.com/users/{username}/events`
- **Method**: GET
- **Authentication**: None (public events only)
- **Rate Limit**: 60 requests/hour for unauthenticated requests

## Response Format

```json
[
  {
    "id": "1234567890",
    "type": "PushEvent",
    "actor": {
      "id": 123456,
      "login": "username",
      "display_login": "username",
      "gravatar_id": "",
      "url": "https://api.github.com/users/username",
      "avatar_url": "https://avatars.githubusercontent.com/u/123456?"
    },
    "repo": {
      "id": 123456789,
      "name": "username/repository",
      "url": "https://api.github.com/repos/username/repository"
    },
    "payload": {
      "repository_id": 123456789,
      "push_id": 123456789,
      "ref": "refs/heads/main",
      "head": "commit_sha",
      "before": "previous_commit_sha"
    },
    "public": true,
    "created_at": "2026-02-19T23:00:59Z"
  }
]
```

## Event Types Supported

### PushEvent

- **Description**: User pushed commits to a repository
- **Payload**: Contains commit information, branch, and repository details
- **Display**: "Pushed commits to {repo}"

### WatchEvent

- **Description**: User starred a repository
- **Payload**: Contains action ("started")
- **Display**: "Starred {repo}"

### CreateEvent

- **Description**: User created a repository or branch
- **Payload**: Contains ref_type ("branch", "repository")
- **Display**: "Created {repo}"

### PullRequestEvent

- **Description**: User opened, closed, or merged a pull request
- **Payload**: Contains action ("opened", "closed", "merged")
- **Display**: "Pull Request in {repo}"

### IssuesEvent

- **Description**: User opened or closed an issue
- **Payload**: Contains action ("opened", "closed")
- **Display**: "Opened/Closed issue in {repo}"

### DeleteEvent

- **Description**: User deleted a repository or branch
- **Payload**: Contains ref_type and deleted object
- **Display**: "Deleted from {repo}"

### ForkEvent

- **Description**: User forked a repository
- **Payload**: Contains forkee repository information
- **Display**: "Forked {repo}"

## Error Handling

### HTTP Error Codes

| Code | Description | Handling |
|------|-------------|----------|
| 200 | Success | Process response normally |
| 404 | User not found | Return "User not found" message |
| 403 | Rate limit exceeded | Show rate limit information |
| 500 | Server error | Return server error message |

### Network Errors

| Error Type | Description | Handling |
|------------|-------------|----------|
| HTTPError | HTTP protocol error | Return error with code and reason |
| URLError | Network connection error | Return network error message |
| JSONDecodeError | Invalid JSON response | Return parsing error message |

## Caching Strategy

### Cache Implementation

- **Location**: `src/cache/{username}.activity.json`
- **Format**: JSON with timestamp and data
- **Duration**: 5 minutes (configurable)
- **Expiration**: Automatic cleanup of expired cache

### Cache Structure

```json
{
  "timestamp": "2026-02-20T01:05:42.182394",
  "data": [
    {
      "id": "1234567890",
      "type": "PushEvent",
      "actor": {...},
      "repo": {...},
      "payload": {...},
      "public": true,
      "created_at": "2026-02-19T23:00:59Z"
    }
  ]
}
```

### Cache Flow

1. **Check cache**: Look for valid cache file
2. **Validate timestamp**: Ensure cache is not expired
3. **Use cache**: Return cached data if valid
4. **Fetch fresh**: Call GitHub API if no valid cache
5. **Store cache**: Save response with timestamp
6. **Return data**: Provide data to caller

## Rate Limiting

### GitHub API Limits

- **Unauthenticated**: 60 requests per hour
- **Authenticated**: 5000 requests per hour
- **Reset**: Hourly based on UTC time

### Rate Limit Headers

```http
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 59
X-RateLimit-Reset: 1642692000
```

### Rate Limit Handling

- **Detection**: Check response headers for rate limit info
- **Waiting**: Automatic wait time calculation if limit exceeded
- **Fallback**: Use cached data during rate limit periods

## Request Headers

### Required Headers

```http
User-Agent: Github-Activity-CLI
Accept: application/vnd.github.v3+json
```

### Optional Headers

```http
Authorization: token YOUR_TOKEN (for higher limits)
If-None-Match: ETAG_VALUE (for conditional requests)
```

## Data Processing

### Event Filtering

- **Public events only**: Private events are excluded
- **Recent first**: Sorted by creation date (newest first)
- **Limit**: Default 10 events (configurable)

### Date Formatting

- **Input**: ISO 8601 format (`2026-02-19T23:00:59Z`)
- **Processing**: Convert to local timezone
- **Output**: `YYYY-MM-DD HH:MM` format

### Repository Name Formatting

- **Input**: `username/repository-name`
- **Processing**: No modification needed
- **Output**: Displayed as-is

## Security Considerations

### Data Privacy

- **Public data only**: No authentication required
- **No sensitive data**: Only public GitHub events
- **Local storage**: Cache stored locally, not shared

### Input Validation

- **Username format**: Regex validation for GitHub usernames
- **Length limits**: Maximum 39 characters
- **Character restrictions**: Alphanumeric, hyphens, underscores

## Performance Optimization

### Caching Benefits

- **Reduced API calls**: 5-minute cache window
- **Faster responses**: Local file access vs network request
- **Rate limit protection**: Fewer API hits per hour

### Memory Efficiency

- **Streaming**: Process response incrementally
- **Minimal storage**: Only essential data cached
- **Cleanup**: Automatic expired cache removal

## Troubleshooting

### Common API Issues

**404 User Not Found**

- Verify username spelling
- Check if user exists and has public activity
- Try with a known active user

**403 Rate Limit Exceeded**

- Wait for rate limit reset (check headers)
- Use cached data if available
- Consider authentication for higher limits

**Network Connection Errors**

- Check internet connectivity
- Verify GitHub API status
- Retry after a short delay

### Debug Information

Enable debug mode by modifying the code to show:

- Request URLs and headers
- Response status codes
- Cache hit/miss information
- Error details and stack traces
