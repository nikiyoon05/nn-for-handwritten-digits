#!/usr/bin/env python3
"""
Simple wrapper to import the Flask app from backend directory
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the Flask app from backend
from backend.app import app

if __name__ == '__main__':
    app.run() 