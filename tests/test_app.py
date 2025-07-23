"""
Test suite for Multiple Disease Prediction System
"""
import os
import sys
import unittest

# Add the parent directory to the path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class TestModelLoading(unittest.TestCase):
    """Test model loading functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.model_dir = os.path.join(os.path.dirname(__file__), '..', 'system')
    
    def test_diabetes_model_exists(self):
        """Test if diabetes model file exists"""
        model_path = os.path.join(self.model_dir, 'diabetes_trained_model.sav')
        self.assertTrue(os.path.exists(model_path), "Diabetes model file not found")
    
    def test_heart_model_exists(self):
        """Test if heart disease model file exists"""
        model_path = os.path.join(self.model_dir, 'heart_trained_model.sav')
        self.assertTrue(os.path.exists(model_path), "Heart disease model file not found")
    
    def test_parkinson_model_exists(self):
        """Test if Parkinson's model file exists"""
        model_path = os.path.join(self.model_dir, 'parkinson_trained_model.sav')
        self.assertTrue(os.path.exists(model_path), "Parkinson's model file not found")

class TestAppStructure(unittest.TestCase):
    """Test application structure and components"""
    
    def test_main_app_exists(self):
        """Test if main application file exists"""
        app_path = os.path.join(os.path.dirname(__file__), '..', 'system', 'app.py')
        self.assertTrue(os.path.exists(app_path), "Main app.py file not found")
    
    def test_requirements_file_exists(self):
        """Test if requirements.txt exists"""
        req_path = os.path.join(os.path.dirname(__file__), '..', 'requirements.txt')
        self.assertTrue(os.path.exists(req_path), "requirements.txt file not found")
    
    def test_readme_exists(self):
        """Test if README.md exists"""
        readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
        self.assertTrue(os.path.exists(readme_path), "README.md file not found")

class TestInputValidation(unittest.TestCase):
    """Test input validation functionality"""
    
    def test_numeric_input_validation(self):
        """Test numeric input validation"""
        # Test valid numeric inputs
        valid_inputs = ["123", "45.67", "0", "100.0"]
        for input_val in valid_inputs:
            try:
                float(input_val)
                self.assertTrue(True, f"Valid input {input_val} should be convertible to float")
            except ValueError:
                self.fail(f"Valid input {input_val} failed to convert to float")
        
        # Test invalid inputs
        invalid_inputs = ["abc", "", "12.34.56", "not_a_number"]
        for input_val in invalid_inputs:
            with self.assertRaises(ValueError):
                float(input_val)

if __name__ == '__main__':
    unittest.main()
