#!/usr/bin/env python3
"""
Basic Usage Example for AI-Powered E-commerce Analytics Hub

This example demonstrates how to use the dashboard components programmatically.
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

import pandas as pd
from config.settings import DATASET_PATH
from utils.data_processing import (
    load_data, 
    clean_data, 
    filter_data, 
    create_demographic_summary,
    analyze_payment_methods,
    analyze_product_categories,
    analyze_ai_tools,
    perform_customer_segmentation,
    generate_insights
)
from utils.chart_helpers import (
    create_gradient_colors,
    apply_chart_theme,
    format_number,
    calculate_trend
)

def main():
    """Main function demonstrating basic usage."""
    
    print("🚀 AI-Powered E-commerce Analytics Hub - Basic Usage Example")
    print("=" * 60)
    
    # 1. Load and clean data
    print("\n1. 📊 Loading and cleaning data...")
    try:
        df = load_data(str(DATASET_PATH))
        df_clean = clean_data(df)
        print(f"   ✅ Loaded {len(df_clean)} records successfully")
    except Exception as e:
        print(f"   ❌ Error loading data: {e}")
        return
    
    # 2. Create demographic summary
    print("\n2. 👥 Creating demographic summary...")
    demo_summary = create_demographic_summary(df_clean)
    print(f"   📈 Total consumers: {demo_summary['total_consumers']:,}")
    print(f"   🛒 Online rate: {demo_summary['online_rate']:.1f}%")
    print(f"   🤖 AI adoption rate: {demo_summary['ai_adoption_rate']:.1f}%")
    
    # 3. Analyze payment methods
    print("\n3. 💳 Analyzing payment methods...")
    payment_analysis = analyze_payment_methods(df_clean)
    if payment_analysis.get('most_popular'):
        method, rate = payment_analysis['most_popular']
        print(f"   🏆 Most popular: {method} ({rate:.1f}%)")
    
    # 4. Analyze product categories
    print("\n4. 🛍️ Analyzing product categories...")
    category_analysis = analyze_product_categories(df_clean)
    if category_analysis.get('most_popular'):
        category, rate = category_analysis['most_popular']
        print(f"   🏆 Most popular: {category} ({rate:.1f}%)")
    
    # 5. Analyze AI tools
    print("\n5. 🤖 Analyzing AI tools...")
    ai_analysis = analyze_ai_tools(df_clean)
    if ai_analysis.get('most_popular'):
        tool, rate = ai_analysis['most_popular']
        print(f"   🏆 Most popular: {tool} ({rate:.1f}%)")
    
    # 6. Customer segmentation
    print("\n6. 👥 Performing customer segmentation...")
    try:
        df_segmented, cluster_analysis = perform_customer_segmentation(df_clean)
        print(f"   ✅ Created {len(cluster_analysis)} customer segments")
        
        # Show segment sizes
        for cluster_name, cluster_info in cluster_analysis.items():
            size = cluster_info['size']
            percentage = cluster_info['percentage']
            ai_rate = cluster_info['ai_adoption']
            print(f"   📊 {cluster_name}: {size} customers ({percentage:.1f}%) - AI adoption: {ai_rate:.1f}%")
    except Exception as e:
        print(f"   ⚠️ Segmentation failed: {e}")
    
    # 7. Generate insights
    print("\n7. 💡 Generating insights...")
    insights = generate_insights(df_clean)
    for insight in insights[:5]:  # Show first 5 insights
        print(f"   {insight}")
    
    # 8. Filter data example
    print("\n8. 🔍 Filtering data example...")
    filters = {
        'Country': 'India',
        'Age': 'Gen Z'
    }
    filtered_df = filter_data(df_clean, filters)
    print(f"   📊 Filtered to {len(filtered_df)} records (India, Gen Z)")
    
    # 9. Utility functions example
    print("\n9. 🛠️ Utility functions example...")
    
    # Color gradient
    colors = create_gradient_colors(5)
    print(f"   🎨 Generated {len(colors)} gradient colors")
    
    # Number formatting
    formatted_number = format_number(1234567.89, "currency")
    print(f"   💰 Formatted number: {formatted_number}")
    
    # Trend calculation
    trend_direction, trend_value, trend_color = calculate_trend(100, 80)
    print(f"   📈 Trend: {trend_direction} {trend_value}")
    
    print("\n✅ Basic usage example completed successfully!")
    print("\n💡 Next steps:")
    print("   - Run the full dashboard: streamlit run app.py")
    print("   - Explore the documentation in docs/")
    print("   - Check out more examples in examples/")

if __name__ == "__main__":
    main() 