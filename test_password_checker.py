"""
Unit tests for Password Strength Checker
"""

import unittest
from password_checker import PasswordChecker, check_password


class TestPasswordChecker(unittest.TestCase):
    """Test cases for PasswordChecker class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.checker = PasswordChecker()
    
    def test_very_weak_password(self):
        """Test very weak password."""
        result = self.checker.check_strength("weak")
        self.assertIn(result['strength'], ["Weak", "Fair"])
        self.assertLess(result['score'], 50)
        self.assertGreater(len(result['feedback']), 0)
    
    def test_common_password(self):
        """Test that common passwords are detected."""
        result = self.checker.check_strength("password")
        self.assertIn("Common weak password", result['failed_criteria'])
        self.assertIn(result['strength'], ["Weak", "Fair"])
    
    def test_password_with_numbers(self):
        """Test password with numbers."""
        result = self.checker.check_strength("password123")
        self.assertIn("Contains digits", result['passed_criteria'])
    
    def test_moderate_password(self):
        """Test moderate strength password."""
        result = self.checker.check_strength("MyPassword1")
        self.assertIn(result['strength'], ["Fair", "Good", "Strong"])
        self.assertGreaterEqual(result['score'], 30)
    
    def test_good_password(self):
        """Test good strength password."""
        result = self.checker.check_strength("MyP@ssw0rd")
        self.assertIn(result['strength'], ["Good", "Strong", "Very Strong"])
        self.assertGreaterEqual(result['score'], 50)
    
    def test_very_strong_password(self):
        """Test very strong password."""
        result = self.checker.check_strength("V3ry$tr0ng!P@ssw0rd")
        self.assertIn(result['strength'], ["Strong", "Very Strong"])
        self.assertGreaterEqual(result['score'], 70)
    
    def test_length_requirement(self):
        """Test minimum length requirement."""
        # Too short
        result = self.checker.check_strength("Ab1!")
        self.assertIn("Length < 8 characters", result['failed_criteria'])
        
        # Meets minimum
        result = self.checker.check_strength("Abcd1234!")
        self.assertIn("Length >= 8 characters", result['passed_criteria'])
    
    def test_uppercase_detection(self):
        """Test uppercase letter detection."""
        # No uppercase
        result = self.checker.check_strength("password123!")
        self.assertIn("No uppercase letters", result['failed_criteria'])
        
        # With uppercase
        result = self.checker.check_strength("Password123!")
        self.assertIn("Contains uppercase letters", result['passed_criteria'])
    
    def test_lowercase_detection(self):
        """Test lowercase letter detection."""
        # No lowercase
        result = self.checker.check_strength("PASSWORD123!")
        self.assertIn("No lowercase letters", result['failed_criteria'])
        
        # With lowercase
        result = self.checker.check_strength("Password123!")
        self.assertIn("Contains lowercase letters", result['passed_criteria'])
    
    def test_digit_detection(self):
        """Test digit detection."""
        # No digits
        result = self.checker.check_strength("Password!@#")
        self.assertIn("No digits", result['failed_criteria'])
        
        # With digits
        result = self.checker.check_strength("Password123!")
        self.assertIn("Contains digits", result['passed_criteria'])
    
    def test_special_char_detection(self):
        """Test special character detection."""
        # No special chars
        result = self.checker.check_strength("Password123")
        self.assertIn("No special characters", result['failed_criteria'])
        
        # With special chars
        result = self.checker.check_strength("Password123!")
        self.assertIn("Contains special characters", result['passed_criteria'])
    
    def test_is_strong_method(self):
        """Test is_strong method."""
        # Weak password
        self.assertFalse(self.checker.is_strong("weak"))
        
        # Strong password
        self.assertTrue(self.checker.is_strong("V3ry$tr0ng!P@ssw0rd"))
    
    def test_custom_min_length(self):
        """Test custom minimum length."""
        checker = PasswordChecker(min_length=12)
        
        # Too short for custom requirement
        result = checker.check_strength("Pass123!")
        self.assertIn("Length < 12 characters", result['failed_criteria'])
        
        # Meets custom requirement
        result = checker.check_strength("Password123!")
        self.assertIn("Length >= 12 characters", result['passed_criteria'])
    
    def test_all_criteria_met(self):
        """Test password that meets all criteria."""
        result = self.checker.check_strength("Str0ng!P@ssw0rd")
        
        # Should have 6 passed criteria (all checks)
        self.assertEqual(len(result['passed_criteria']), 6)
        self.assertEqual(len(result['failed_criteria']), 0)
        self.assertEqual(len(result['feedback']), 0)
        self.assertEqual(result['score'], 100)
    
    def test_convenience_function(self):
        """Test the convenience function check_password."""
        result = check_password("Test123!")
        self.assertIn('score', result)
        self.assertIn('strength', result)
        self.assertIn('passed_criteria', result)
        self.assertIn('failed_criteria', result)
        self.assertIn('feedback', result)
    
    def test_empty_password(self):
        """Test empty password."""
        result = self.checker.check_strength("")
        self.assertEqual(result['strength'], "Weak")
        self.assertEqual(result['score'], 15)  # Only passes the "not common" check
    
    def test_numeric_only_password(self):
        """Test numeric-only password."""
        result = self.checker.check_strength("12345678")
        self.assertIn("No uppercase letters", result['failed_criteria'])
        self.assertIn("No lowercase letters", result['failed_criteria'])
        self.assertIn("No special characters", result['failed_criteria'])
    
    def test_special_chars_variety(self):
        """Test various special characters."""
        special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/`~\\"
        for char in special_chars:
            password = f"Test123{char}"
            result = self.checker.check_strength(password)
            self.assertIn("Contains special characters", result['passed_criteria'],
                         f"Failed to detect special char: {char}")


class TestPasswordStrengthCategories(unittest.TestCase):
    """Test strength categorization."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.checker = PasswordChecker()
    
    def test_strength_categories(self):
        """Test all strength categories."""
        # Test score ranges
        self.assertEqual(self.checker._get_strength_category(95), "Very Strong")
        self.assertEqual(self.checker._get_strength_category(90), "Very Strong")
        self.assertEqual(self.checker._get_strength_category(80), "Strong")
        self.assertEqual(self.checker._get_strength_category(70), "Strong")
        self.assertEqual(self.checker._get_strength_category(60), "Good")
        self.assertEqual(self.checker._get_strength_category(50), "Good")
        self.assertEqual(self.checker._get_strength_category(40), "Fair")
        self.assertEqual(self.checker._get_strength_category(30), "Fair")
        self.assertEqual(self.checker._get_strength_category(20), "Weak")
        self.assertEqual(self.checker._get_strength_category(0), "Weak")


if __name__ == '__main__':
    unittest.main()
