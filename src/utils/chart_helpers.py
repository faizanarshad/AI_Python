"""
Chart helper functions for creating consistent and attractive visualizations
"""

import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple, Any
import streamlit as st

def create_gradient_colors(n_colors: int, start_color: str = "#1f77b4", end_color: str = "#ff7f0e") -> List[str]:
    """
    Create a gradient color palette
    
    Args:
        n_colors: Number of colors to generate
        start_color: Starting color in hex format
        end_color: Ending color in hex format
    
    Returns:
        List of hex color strings
    """
    import colorsys
    
    # Convert hex to RGB
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    # Convert RGB to hex
    def rgb_to_hex(rgb):
        return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))
    
    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)
    
    colors = []
    for i in range(n_colors):
        ratio = i / (n_colors - 1) if n_colors > 1 else 0
        rgb = tuple(start + ratio * (end - start) for start, end in zip(start_rgb, end_rgb))
        colors.append(rgb_to_hex(rgb))
    
    return colors

def apply_chart_theme(fig: go.Figure, theme: str = "professional") -> go.Figure:
    """
    Apply consistent theme to charts
    
    Args:
        fig: Plotly figure object
        theme: Theme name ('professional', 'modern', 'minimal')
    
    Returns:
        Updated figure object
    """
    themes = {
        "professional": {
            "template": "plotly_white",
            "font_family": "Arial, sans-serif",
            "font_size": 12,
            "title_font_size": 16,
            "paper_bgcolor": "rgba(0,0,0,0)",
            "plot_bgcolor": "rgba(0,0,0,0)",
            "margin": {"l": 60, "r": 40, "t": 60, "b": 60}
        },
        "modern": {
            "template": "plotly_dark",
            "font_family": "Segoe UI, sans-serif",
            "font_size": 11,
            "title_font_size": 18,
            "paper_bgcolor": "#1a1a1a",
            "plot_bgcolor": "#1a1a1a",
            "margin": {"l": 50, "r": 30, "t": 50, "b": 50}
        },
        "minimal": {
            "template": "simple_white",
            "font_family": "Helvetica, sans-serif",
            "font_size": 10,
            "title_font_size": 14,
            "paper_bgcolor": "white",
            "plot_bgcolor": "white",
            "margin": {"l": 40, "r": 20, "t": 40, "b": 40}
        }
    }
    
    config = themes.get(theme, themes["professional"])
    
    fig.update_layout(
        template=config["template"],
        font=dict(
            family=config["font_family"],
            size=config["font_size"]
        ),
        title=dict(
            font=dict(size=config["title_font_size"])
        ),
        paper_bgcolor=config["paper_bgcolor"],
        plot_bgcolor=config["plot_bgcolor"],
        margin=config["margin"],
        hovermode="closest",
        showlegend=True
    )
    
    return fig

def add_annotations(fig: go.Figure, annotations: List[Dict[str, Any]]) -> go.Figure:
    """
    Add custom annotations to charts
    
    Args:
        fig: Plotly figure object
        annotations: List of annotation dictionaries
    
    Returns:
        Updated figure object
    """
    for annotation in annotations:
        fig.add_annotation(
            x=annotation.get("x"),
            y=annotation.get("y"),
            text=annotation.get("text", ""),
            showarrow=annotation.get("showarrow", True),
            arrowhead=annotation.get("arrowhead", 2),
            arrowsize=annotation.get("arrowsize", 1),
            arrowwidth=annotation.get("arrowwidth", 2),
            arrowcolor=annotation.get("arrowcolor", "black"),
            ax=annotation.get("ax", 0),
            ay=annotation.get("ay", -40),
            bgcolor=annotation.get("bgcolor", "rgba(255,255,255,0.8)"),
            bordercolor=annotation.get("bordercolor", "black"),
            borderwidth=annotation.get("borderwidth", 1),
            font=dict(
                size=annotation.get("font_size", 12),
                color=annotation.get("font_color", "black")
            )
        )
    
    return fig

def create_metric_card(title: str, value: str, delta: Optional[str] = None, 
                      delta_color: str = "normal") -> str:
    """
    Create HTML for a metric card
    
    Args:
        title: Card title
        value: Main value to display
        delta: Change value (optional)
        delta_color: Color of delta ('normal', 'inverse')
    
    Returns:
        HTML string for the metric card
    """
    delta_html = ""
    if delta:
        delta_class = "delta-inverse" if delta_color == "inverse" else "delta"
        delta_html = f'<div class="{delta_class}">{delta}</div>'
    
    return f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
        {delta_html}
    </div>
    """

def create_info_card(title: str, content: str, icon: str = "ℹ️") -> str:
    """
    Create HTML for an info card
    
    Args:
        title: Card title
        content: Card content
        icon: Icon emoji
    
    Returns:
        HTML string for the info card
    """
    return f"""
    <div class="info-card">
        <div class="info-header">
            <span class="info-icon">{icon}</span>
            <span class="info-title">{title}</span>
        </div>
        <div class="info-content">{content}</div>
    </div>
    """

def format_number(value: float, format_type: str = "number") -> str:
    """
    Format numbers for display
    
    Args:
        value: Number to format
        format_type: Format type ('number', 'percentage', 'currency', 'decimal')
    
    Returns:
        Formatted string
    """
    if pd.isna(value):
        return "N/A"
    
    if format_type == "percentage":
        return f"{value:.1f}%"
    elif format_type == "currency":
        return f"${value:,.0f}"
    elif format_type == "decimal":
        return f"{value:.2f}"
    else:
        return f"{value:,.0f}"

def calculate_trend(current: float, previous: float) -> Tuple[str, str]:
    """
    Calculate trend between two values
    
    Args:
        current: Current value
        previous: Previous value
    
    Returns:
        Tuple of (trend_direction, trend_value)
    """
    if previous == 0:
        return "neutral", "0%"
    
    change = ((current - previous) / previous) * 100
    
    if change > 0:
        direction = "up"
        color = "normal"
    elif change < 0:
        direction = "down"
        color = "inverse"
    else:
        direction = "neutral"
        color = "normal"
    
    return direction, f"{change:+.1f}%", color

def create_summary_stats(df: pd.DataFrame, numeric_columns: List[str]) -> Dict[str, Any]:
    """
    Create summary statistics for numeric columns
    
    Args:
        df: DataFrame to analyze
        numeric_columns: List of numeric column names
    
    Returns:
        Dictionary of summary statistics
    """
    stats = {}
    
    for col in numeric_columns:
        if col in df.columns:
            col_stats = df[col].describe()
            stats[col] = {
                "count": col_stats["count"],
                "mean": col_stats["mean"],
                "std": col_stats["std"],
                "min": col_stats["min"],
                "25%": col_stats["25%"],
                "50%": col_stats["50%"],
                "75%": col_stats["75%"],
                "max": col_stats["max"]
            }
    
    return stats 