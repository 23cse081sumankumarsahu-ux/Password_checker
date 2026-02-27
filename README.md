# Password_checker
A beginner-friendly Python project that evaluates password strength using regex-based rules, scoring, and actionable feedback.

## Features

- **Comprehensive Password Analysis**: Checks passwords against multiple criteria including length, uppercase/lowercase letters, digits, special characters, and common password detection
- **Scoring System**: Provides a 0-100 score for password strength
- **Strength Categories**: Classifies passwords as Weak, Fair, Good, Strong, or Very Strong
- **Actionable Feedback**: Gives specific suggestions on how to improve password strength
- **Easy to Use**: Simple API with both class-based and functional interfaces

## Installation

No external dependencies required! This project uses only Python standard library.

```bash
git clone https://github.com/23cse081sumankumarsahu-ux/Password_checker.git
cd Password_checker
```

## Usage

### Basic Usage

```python
from password_checker import check_password

# Check a password
result = check_password("MyP@ssw0rd")

print(f"Score: {result['score']}/100")
print(f"Strength: {result['strength']}")

# Show feedback if password is weak
if result['feedback']:
    print("\nSuggestions:")
    for suggestion in result['feedback']:
        print(f"  - {suggestion}")
```

### Using the PasswordChecker Class

```python
from password_checker import PasswordChecker

# Create a checker with custom minimum length
checker = PasswordChecker(min_length=12)

# Check password strength
result = checker.check_strength("MyP@ssw0rd123")

# Check if password meets minimum strength requirement
if checker.is_strong("MyP@ssw0rd123", min_score=70):
    print("Password is strong enough!")
```

### Running the Interactive Demo

```bash
python demo.py
```

This will:
1. Show example password analyses
2. Launch an interactive mode where you can test your own passwords

### Running the Example Script

```bash
python password_checker.py
```

This will demonstrate the password checker with several example passwords.

## Password Strength Criteria

The password checker evaluates passwords based on the following criteria:

1. **Length** (20 points): Must be at least 8 characters (customizable)
2. **Uppercase Letters** (15 points): Contains A-Z
3. **Lowercase Letters** (15 points): Contains a-z
4. **Digits** (15 points): Contains 0-9
5. **Special Characters** (20 points): Contains symbols like !@#$%^&*
6. **Not Common** (15 points): Not in the list of common weak passwords

### Strength Categories

- **Weak** (0-29): Very insecure, easily guessable
- **Fair** (30-49): Somewhat insecure, needs improvement
- **Good** (50-69): Moderate security, acceptable for low-risk accounts
- **Strong** (70-89): Good security, suitable for most accounts
- **Very Strong** (90-100): Excellent security, suitable for high-security accounts

## Testing

Run the test suite to verify everything works correctly:

```bash
python -m unittest test_password_checker.py -v
```

## Examples

### Weak Password
```python
>>> result = check_password("weak")
>>> print(result['strength'])
Fair
>>> print(result['score'])
30
```

### Strong Password
```python
>>> result = check_password("V3ry$tr0ng!P@ssw0rd")
>>> print(result['strength'])
Very Strong
>>> print(result['score'])
100
```

## API Reference

### `check_password(password, min_length=8)`
Convenience function to check password strength.

**Parameters:**
- `password` (str): The password to check
- `min_length` (int): Minimum required length (default: 8)

**Returns:**
- Dictionary with keys: `score`, `strength`, `passed_criteria`, `failed_criteria`, `feedback`

### `PasswordChecker(min_length=8)`
Class for checking password strength.

**Methods:**
- `check_strength(password)`: Returns detailed password analysis
- `is_strong(password, min_score=70)`: Returns True if password meets minimum score

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available for educational purposes.

