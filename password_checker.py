"""
Password Strength Checker
A module to evaluate password strength using regex-based rules, scoring, and actionable feedback.
"""

import re
from typing import Tuple, List, Dict


class PasswordChecker:
    """
    A class to check the strength of passwords based on various criteria.
    """
    
    # Password strength criteria weights
    WEIGHTS = {
        'length': 20,
        'uppercase': 15,
        'lowercase': 15,
        'digits': 15,
        'special_chars': 20,
        'no_common': 15
    }
    
    # Common weak passwords to avoid
    COMMON_PASSWORDS = [
        'password', '12345678', 'qwerty', 'abc123', 'letmein',
        'welcome', 'monkey', 'dragon', 'master', 'password123',
        '123456', '123456789', 'admin', 'root', 'user'
    ]
    
    def __init__(self, min_length: int = 8):
        """
        Initialize the password checker.
        
        Args:
            min_length: Minimum required password length (default: 8)
        """
        self.min_length = min_length
    
    def check_strength(self, password: str) -> Dict[str, any]:
        """
        Check the strength of a password and return detailed results.
        
        Args:
            password: The password to check
            
        Returns:
            Dictionary containing:
                - score: Password strength score (0-100)
                - strength: Strength category (Weak/Fair/Good/Strong/Very Strong)
                - passed_criteria: List of criteria that passed
                - failed_criteria: List of criteria that failed
                - feedback: List of actionable feedback messages
        """
        score = 0
        passed_criteria = []
        failed_criteria = []
        feedback = []
        
        # Check length
        if len(password) >= self.min_length:
            score += self.WEIGHTS['length']
            passed_criteria.append(f"Length >= {self.min_length} characters")
        else:
            failed_criteria.append(f"Length < {self.min_length} characters")
            feedback.append(f"Use at least {self.min_length} characters")
        
        # Check for uppercase letters
        if re.search(r'[A-Z]', password):
            score += self.WEIGHTS['uppercase']
            passed_criteria.append("Contains uppercase letters")
        else:
            failed_criteria.append("No uppercase letters")
            feedback.append("Add uppercase letters (A-Z)")
        
        # Check for lowercase letters
        if re.search(r'[a-z]', password):
            score += self.WEIGHTS['lowercase']
            passed_criteria.append("Contains lowercase letters")
        else:
            failed_criteria.append("No lowercase letters")
            feedback.append("Add lowercase letters (a-z)")
        
        # Check for digits
        if re.search(r'\d', password):
            score += self.WEIGHTS['digits']
            passed_criteria.append("Contains digits")
        else:
            failed_criteria.append("No digits")
            feedback.append("Add numbers (0-9)")
        
        # Check for special characters
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
            score += self.WEIGHTS['special_chars']
            passed_criteria.append("Contains special characters")
        else:
            failed_criteria.append("No special characters")
            feedback.append("Add special characters (!@#$%^&* etc.)")
        
        # Check if password is not a common weak password
        if password.lower() not in self.COMMON_PASSWORDS:
            score += self.WEIGHTS['no_common']
            passed_criteria.append("Not a common password")
        else:
            failed_criteria.append("Common weak password")
            feedback.append("Avoid common passwords like 'password', '123456', etc.")
        
        # Determine strength category
        strength = self._get_strength_category(score)
        
        return {
            'score': score,
            'strength': strength,
            'passed_criteria': passed_criteria,
            'failed_criteria': failed_criteria,
            'feedback': feedback
        }
    
    def _get_strength_category(self, score: int) -> str:
        """
        Convert numerical score to strength category.
        
        Args:
            score: Password strength score (0-100)
            
        Returns:
            Strength category string
        """
        if score >= 90:
            return "Very Strong"
        elif score >= 70:
            return "Strong"
        elif score >= 50:
            return "Good"
        elif score >= 30:
            return "Fair"
        else:
            return "Weak"
    
    def is_strong(self, password: str, min_score: int = 70) -> bool:
        """
        Check if a password meets the minimum strength requirement.
        
        Args:
            password: The password to check
            min_score: Minimum required score (default: 70)
            
        Returns:
            True if password is strong enough, False otherwise
        """
        result = self.check_strength(password)
        return result['score'] >= min_score


def check_password(password: str, min_length: int = 8) -> Dict[str, any]:
    """
    Convenience function to check password strength.
    
    Args:
        password: The password to check
        min_length: Minimum required password length (default: 8)
        
    Returns:
        Dictionary with password strength analysis
    """
    checker = PasswordChecker(min_length=min_length)
    return checker.check_strength(password)


if __name__ == "__main__":
    # Example usage
    test_passwords = [
        "weak",
        "password123",
        "MyPassword1",
        "MyP@ssw0rd",
        "V3ry$tr0ng!P@ssw0rd"
    ]
    
    print("Password Strength Checker Demo\n" + "=" * 50)
    
    for pwd in test_passwords:
        print(f"\nPassword: {'*' * len(pwd)}")
        result = check_password(pwd)
        print(f"Score: {result['score']}/100")
        print(f"Strength: {result['strength']}")
        
        if result['feedback']:
            print("\nSuggestions for improvement:")
            for suggestion in result['feedback']:
                print(f"  - {suggestion}")
