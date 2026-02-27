"""
Interactive Password Strength Checker Demo
"""

from password_checker import PasswordChecker


def print_separator():
    """Print a visual separator."""
    print("=" * 60)


def display_result(password: str, result: dict, show_password: bool = False):
    """
    Display password strength check result in a user-friendly format.
    
    Args:
        password: The password that was checked
        result: Result dictionary from password checker
        show_password: Whether to show the actual password (default: False)
    """
    print_separator()
    
    if show_password:
        print(f"Password: {password}")
    else:
        print(f"Password: {'*' * len(password)}")
    
    print(f"\nStrength: {result['strength']}")
    print(f"Score: {result['score']}/100")
    
    # Visual strength bar
    bar_length = 30
    filled = int((result['score'] / 100) * bar_length)
    bar = '█' * filled + '░' * (bar_length - filled)
    print(f"[{bar}]")
    
    # Show passed criteria
    if result['passed_criteria']:
        print(f"\n✓ Passed criteria ({len(result['passed_criteria'])}):")
        for criterion in result['passed_criteria']:
            print(f"  • {criterion}")
    
    # Show failed criteria and feedback
    if result['failed_criteria']:
        print(f"\n✗ Failed criteria ({len(result['failed_criteria'])}):")
        for criterion in result['failed_criteria']:
            print(f"  • {criterion}")
    
    if result['feedback']:
        print(f"\n💡 Suggestions for improvement:")
        for suggestion in result['feedback']:
            print(f"  • {suggestion}")
    
    print_separator()


def main():
    """Run the interactive password strength checker demo."""
    checker = PasswordChecker()
    
    print("\n" + "=" * 60)
    print("          PASSWORD STRENGTH CHECKER")
    print("=" * 60)
    print("\nThis tool evaluates password strength based on:")
    print("  • Length (minimum 8 characters)")
    print("  • Uppercase letters (A-Z)")
    print("  • Lowercase letters (a-z)")
    print("  • Digits (0-9)")
    print("  • Special characters (!@#$%^&* etc.)")
    print("  • Not a common weak password")
    print("\n" + "=" * 60)
    
    # Demo with example passwords
    print("\n📋 Example Password Analysis:\n")
    
    examples = [
        ("weak", "Very weak password"),
        ("password123", "Common weak password"),
        ("MyPassword1", "Moderate password"),
        ("MyP@ssw0rd", "Good password"),
        ("V3ry$tr0ng!P@ssw0rd", "Very strong password")
    ]
    
    for pwd, description in examples:
        result = checker.check_strength(pwd)
        print(f"\n{description}:")
        display_result(pwd, result, show_password=True)
    
    # Interactive mode
    print("\n\n" + "=" * 60)
    print("          INTERACTIVE MODE")
    print("=" * 60)
    print("\nEnter passwords to check their strength.")
    print("Type 'quit' or 'exit' to end.\n")
    
    while True:
        try:
            password = input("\nEnter password to check (or 'quit' to exit): ").strip()
            
            if password.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using Password Strength Checker!")
                break
            
            if not password:
                print("Please enter a password.")
                continue
            
            result = checker.check_strength(password)
            display_result(password, result, show_password=False)
            
        except KeyboardInterrupt:
            print("\n\nThank you for using Password Strength Checker!")
            break
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
