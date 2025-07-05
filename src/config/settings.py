"""
Configuration settings for the AI-Powered E-commerce Analytics Hub
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Data paths
DATA_DIR = PROJECT_ROOT / "assets" / "data"
DATASET_PATH = DATA_DIR / "Dataset.csv"
MBA_DATASET_PATH = DATA_DIR / "mba_decision_dataset.csv"

# Assets paths
ASSETS_DIR = PROJECT_ROOT / "assets"
IMAGES_DIR = ASSETS_DIR / "images"

# Documentation paths
DOCS_DIR = PROJECT_ROOT / "docs"
API_DOCS_DIR = DOCS_DIR / "api"
USER_GUIDE_DIR = DOCS_DIR / "user_guide"

# Dashboard configuration
DASHBOARD_CONFIG = {
    "page_title": "AI-Powered E-commerce Analytics Hub",
    "page_icon": "🚀",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "menu_items": {
        "Get help": "https://github.com/your-repo/issues",
        "Report a bug": "https://github.com/your-repo/issues",
        "About": "AI-Powered E-commerce Analytics Hub - Professional Business Intelligence Dashboard"
    }
}

# Chart configuration
CHART_CONFIG = {
    "template": "plotly_white",
    "color_scale": "viridis",
    "height": 600,
    "margin": {"l": 50, "r": 50, "t": 50, "b": 50}
}

# Styling configuration
STYLE_CONFIG = {
    "primary_color": "#1f77b4",
    "secondary_color": "#ff7f0e",
    "success_color": "#2ca02c",
    "warning_color": "#d62728",
    "info_color": "#17a2b8",
    "light_color": "#f8f9fa",
    "dark_color": "#343a40"
}

# Cache configuration
CACHE_CONFIG = {
    "ttl": 3600,  # 1 hour
    "max_entries": 100
}

# Feature flags
FEATURES = {
    "enable_3d_charts": True,
    "enable_animations": True,
    "enable_export": True,
    "enable_clustering": True,
    "enable_trendlines": True
}

# Performance settings
PERFORMANCE = {
    "max_data_points": 10000,
    "chart_timeout": 30,
    "enable_lazy_loading": True
} 