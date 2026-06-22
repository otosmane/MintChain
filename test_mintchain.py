# test_mintchain.py
"""
Tests for MintChain module.
"""

import unittest
from mintchain import MintChain

class TestMintChain(unittest.TestCase):
    """Test cases for MintChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MintChain()
        self.assertIsInstance(instance, MintChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MintChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
