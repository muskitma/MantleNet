# test_mantlenet.py
"""
Tests for MantleNet module.
"""

import unittest
from mantlenet import MantleNet

class TestMantleNet(unittest.TestCase):
    """Test cases for MantleNet class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MantleNet()
        self.assertIsInstance(instance, MantleNet)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MantleNet()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
