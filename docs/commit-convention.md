# Developer Conventions and Documentation

## Commit Messages Convention

### Summary: Golden Rules

1. **One change per commit:** If you fixed a bug and also changed a button color, make **two** separate commits.
2. **Use English:** All commit messages must be in English and start with lowercase.
3. **Use imperative mood:** Write "add method" instead of "added" or "adding". It's like giving a command to the code.
4. **Fixed structure:** Always use the format `type: description`.

---

### Message Structure

All your commits must follow this format:

`type: short description in lowercase`

*Example: `feat: add validation to registration form`*

---

### Commit Types

| Type | When to use |
| :--- | :--- |
| **feat** | A new feature (e.g., new endpoint, new component). |
| **fix** | Bug fix or error resolution. |
| **docs** | Documentation only changes (README, comments, docs). |
| **style** | Visual or formatting changes (spaces, commas) that don't affect logic. |
| **refactor** | Code changes that neither fix a bug nor add a feature. |
| **test** | Add or modify unit/integration tests. |
| **chore** | Maintenance tasks, dependency updates, build process changes. |
| **perf** | Performance improvements. |
| **ci** | CI/CD configuration changes. |

---

### Detailed Commit Message Format

For complex changes, use this extended format:

```text
type: short description (50 chars max)

More detailed explanatory text, wrapped to 72 characters. Explain
what and why, not how. Reference issue numbers.

- Use bullet points for breaking changes
- Reference related issues: Closes #123, Fixes #456
- Co-authored-by: Name <email@example.com>
```

---

### Examples

**❌ Bad (Avoid these):**

* fix: it works now (Vague and doesn't describe the solution)
* changes (Missing type and in Spanish)
* feat: fix login and change footer and delete logo (Too many responsibilities)

**✅ Good:**

* feat: connect products api
* fix: resolve typo in username field
* docs: update installation instructions in README.md
* style: fix indentation in auth controller
* refactor: extract user validation logic to service layer
* test: add unit tests for payment processing
* perf: optimize database query for user listings

---

## Pull Request Convention

### PR Title Format

`type: short description in lowercase`

Follow the same commit message type convention for PR titles.

**Examples:**

* `feat: implement user authentication system`
* `fix: resolve memory leak in data processing`
* `docs: update API documentation with new endpoints`

### PR Description Template

```markdown
## Description
Brief description of what this PR accomplishes and why it's needed.

## Features Added

- **User Authentication System**: Implemented JWT-based authentication with login/logout functionality
- **Role-Based Access Control**: Added admin/user roles with permission middleware
- **Profile Management**: Created user profile CRUD operations with avatar upload
- `POST /api/auth/login` - User authentication
- `POST /api/auth/logout` - Session termination  
- `GET /api/users/profile` - Retrieve user profile
- `PUT /api/users/profile` - Update user profile
- `POST /api/users/avatar` - Upload profile picture
- Added `users` table with authentication fields
- Created `user_roles` junction table for permissions
- Added indexes for improved query performance

## Type of Change
- Bug fix (non-breaking change that fixes an issue)
- New feature (non-breaking change that adds functionality)
- Breaking change (fix or feature that would cause existing functionality to not work as expected)
- Documentation update
- Refactoring (code improvement without functional changes)
- Performance improvement
- Other (please describe)
```

---

## Branch Naming Convention

Use descriptive branch names following this pattern:

`type/description`

**Examples:**

* `feat/user-authentication`
* `fix/login-validation-error`
* `docs/api-endpoint-documentation`
* `refactor/database-connection-pool`
* `hotfix/critical-security-patch`

---
