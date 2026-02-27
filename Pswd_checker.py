import re

# Precompile regex patterns for performance
patterns = {
    "uppercase": re.compile(r"[A-Z]"),
    "lowercase": re.compile(r"[a-z]"),
    "digit": re.compile(r"[0-9]"),
    "special": re.compile(r"[!@#$%^&*(),.?\":{}|<>]"),
}

def check_password_strength(password: str) -> tuple:
    """Return a score (0–5) and feedback message for password strength."""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    if patterns["uppercase"].search(password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if patterns["lowercase"].search(password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if patterns["digit"].search(password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if patterns["special"].search(password):
        score += 1
    else:
        feedback.append("Use at least one special character (!@#$...).")

    return score, feedback


def strength_category(score: int) -> str:
    """Map score to strength category."""
    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"


def main():
    print("🔐 Password Strength Checker")
    password = input("Enter a password: ")

    score, feedback = check_password_strength(password)
    category = strength_category(score)

    print(f"\nStrength: {category} ({score}/5)")
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(" - " + f)


if __name__ == "__main__":
    main()
