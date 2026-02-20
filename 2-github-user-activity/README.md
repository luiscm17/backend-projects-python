# GitHub User Activity CLI - Project Two

A command-line tool to fetch and display recent GitHub activity for any user.

## Features

- 🚀 **Fast**: Uses intelligent caching to reduce API calls
- 📊 **Comprehensive**: Shows pushes, stars, forks, pull requests, and more
- 🔧 **Robust**: Input validation and error handling
- 📝 **Readable**: Clean, formatted output
- ⚡ **Performance**: 5-minute cache to avoid rate limits

## Installation

### Prerequisites

- Python 3.8+
- `uv` package manager (recommended)

### Setup

```bash
# Clone the repository
git clone <repository-url>
cd backend-learn/2-github-user-activity

# Install dependencies
uv install

# Or using pip
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
# Get activity for a user
uv run src/main.py <username>

# Examples
uv run src/main.py octocat
```

### Output Example

```bash
GitHub User Activity CLI
Usage: python src/main.py <username>
Searching for user: <username>
User: <username>
Pushed commits to <username>/<repository> - <date>
Starred <username>/<repository> - <date>
Created <username>/<repository> - <date>
Pull Request in <username>/<repository> - <date>
```

## Supported Event Types

- **PushEvent**: Code commits pushed to repositories
- **WatchEvent**: Repositories starred by the user
- **CreateEvent**: New repositories or branches created
- **PullRequestEvent**: Pull requests opened/closed/merged
- **IssuesEvent**: Issues opened or closed
- **DeleteEvent**: Repositories or branches deleted
- **ForkEvent**: Repositories forked

## Architecture

```mermaid
src/
├── main.py          # Entry point and CLI interface
├── github_api.py    # GitHub API integration with caching
├── cache.py         # Intelligent caching system
├── formatter.py     # Output formatting and display
└── utils.py         # Validation and utility functions
```

## Caching

The tool implements a 5-minute cache system:

- **First request**: Fetches from GitHub API and stores locally
- **Subsequent requests**: Uses cached data (much faster)
- **Cache expiration**: Automatically refreshes after 5 minutes

Cache files are stored in `src/cache/` directory.

## Error Handling

- **Invalid usernames**: Validates GitHub username format
- **Network errors**: Handles connection issues gracefully
- **Rate limiting**: Respects GitHub API limits
- **Not found**: Clear messages for non-existent users

## Development

### Project Structure

- **Modular design**: Each component has a single responsibility
- **Clean architecture**: Clear separation of concerns
- **Type hints**: Full type annotation support
- **Documentation**: Comprehensive docstrings

### Running Tests

```bash
# Run the tool
uv run src/main.py <username>

# Test with different users
uv run src/main.py <username>
uv run src/main.py <username>
```

## API Limits

- **Rate limit**: 60 requests per hour (unauthenticated)
- **Cache duration**: 5 minutes (configurable)
- **User-Agent**: Custom user agent for proper identification

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Troubleshooting

### Common Issues

**"Username is required"**

- Ensure you provide a username as argument
- Example: `uv run src/main.py username`

**"Username can only contain letters, numbers and underscores"**

- GitHub usernames have specific format requirements
- Check the username format and try again

**"No activity found"**

- The user exists but has no public activity
- Try with a more active user

**Rate limit errors**

- Wait a few minutes before trying again
- The cache helps minimize this issue

### Getting Help

For more information:

- Check the documentation in `docs/`
- Review the source code comments
- Open an issue for bugs or feature requests
