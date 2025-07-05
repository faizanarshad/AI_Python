"""
Setup script for AI-Powered E-commerce Analytics Hub
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Read requirements
requirements = (this_directory / "requirements.txt").read_text().splitlines()

setup(
    name="ai-ecommerce-analytics",
    version="1.0.0",
    author="AI Analytics Team",
    author_email="contact@aianalytics.com",
    description="A comprehensive business intelligence dashboard for e-commerce consumer behavior analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-repo/ai-ecommerce-analytics",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Business/Financial",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ai-ecommerce-dashboard=app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.csv", "*.json", "*.yaml", "*.yml"],
    },
    keywords=[
        "e-commerce",
        "analytics",
        "dashboard",
        "business-intelligence",
        "ai",
        "machine-learning",
        "data-visualization",
        "streamlit",
        "plotly",
    ],
    project_urls={
        "Bug Reports": "https://github.com/your-repo/ai-ecommerce-analytics/issues",
        "Source": "https://github.com/your-repo/ai-ecommerce-analytics",
        "Documentation": "https://ai-ecommerce-analytics.readthedocs.io/",
    },
) 