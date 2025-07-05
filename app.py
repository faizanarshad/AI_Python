#!/usr/bin/env python3
"""
AI-Powered E-commerce Analytics Hub
Main Application Entry Point

A comprehensive business intelligence dashboard for analyzing e-commerce consumer behavior
and AI adoption patterns using advanced visualizations and machine learning insights.
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Import and run the dashboard
from dashboard import main

if __name__ == "__main__":
    main() 