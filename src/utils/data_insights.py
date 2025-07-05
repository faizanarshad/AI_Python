#!/usr/bin/env python3
"""
Quick Data Insights Script
Demonstrates key findings from the E-commerce AI Behavior Dataset
"""

import pandas as pd
import numpy as np

def load_and_analyze_data():
    """Load data and perform quick analysis"""
    print("🛒 E-commerce AI Behavior Dataset - Quick Insights")
    print("=" * 60)
    
    # Load data with encoding handling
    try:
        df = pd.read_csv('Dataset.csv')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv('Dataset.csv', encoding='latin-1')
        except:
            df = pd.read_csv('Dataset.csv', encoding='cp1252')
    print(f"📊 Dataset loaded: {len(df)} records, {len(df.columns)} columns")
    
    # Basic statistics
    print("\n📈 Key Metrics:")
    print(f"   • Total Consumers: {len(df):,}")
    print(f"   • Online Consumers: {len(df[df['Online_Consumer'] == 'YES']):,} ({(df['Online_Consumer'] == 'YES').mean()*100:.1f}%)")
    print(f"   • AI Endorsers: {len(df[df['AI_Endorsement'] == 'YES']):,} ({(df['AI_Endorsement'] == 'YES').mean()*100:.1f}%)")
    print(f"   • AI Satisfied: {len(df[df['AI_Satisfication'] == 'Satisfied']):,} ({(df['AI_Satisfication'] == 'Satisfied').mean()*100:.1f}%)")
    
    # Country distribution
    print("\n🌍 Geographic Distribution:")
    country_counts = df['Country'].value_counts()
    for country, count in country_counts.items():
        percentage = (count / len(df)) * 100
        print(f"   • {country}: {count:,} ({percentage:.1f}%)")
    
    # Age distribution
    print("\n👥 Age Distribution:")
    age_counts = df['Age'].value_counts()
    for age, count in age_counts.items():
        percentage = (count / len(df)) * 100
        print(f"   • {age}: {count:,} ({percentage:.1f}%)")
    
    # AI adoption by age
    print("\n🤖 AI Adoption by Age:")
    ai_by_age = df.groupby('Age')['AI_Endorsement'].apply(lambda x: (x == 'YES').mean() * 100)
    for age, rate in ai_by_age.items():
        print(f"   • {age}: {rate:.1f}%")
    
    # Most popular AI tools
    print("\n🛠️ AI Tools Usage:")
    ai_tools = ['AI_Tools_Used _Chatbots', 'AI_Tools_Used_Virtual_Assistant', 'AI_Tools_Used_Voice&Photo_Search']
    for tool in ai_tools:
        usage_rate = (df[tool] == 'YES').mean() * 100
        tool_name = tool.replace('AI_Tools_Used_', '')
        print(f"   • {tool_name}: {usage_rate:.1f}%")
    
    # Payment methods
    print("\n💳 Payment Method Preferences:")
    payment_methods = ['Payment_Method_Credit/Debit', 'Payment_Method_COD', 'Payment_Method_Ewallet']
    for method in payment_methods:
        usage_rate = (df[method] == 'YES').mean() * 100
        method_name = method.replace('Payment_Method_', '')
        print(f"   • {method_name}: {usage_rate:.1f}%")
    
    # Product categories
    print("\n🛍️ Product Category Preferences:")
    product_categories = [
        'Product_Category_Appliances', 'Product_Category_Electronics',
        'Product_Category_Groceries', 'Product_Category_Personal_Care',
        'Product_Category_Clothing'
    ]
    for category in product_categories:
        purchase_rate = (df[category] == 'YES').mean() * 100
        category_name = category.replace('Product_Category_', '')
        print(f"   • {category_name}: {purchase_rate:.1f}%")
    
    # Key insights
    print("\n💡 Key Insights:")
    
    # Highest AI adoption age
    highest_ai_age = ai_by_age.idxmax()
    print(f"   • Highest AI adoption: {highest_ai_age} ({ai_by_age[highest_ai_age]:.1f}%)")
    
    # Most popular AI tool
    tool_usage = {}
    for tool in ai_tools:
        tool_name = tool.replace('AI_Tools_Used_', '')
        tool_usage[tool_name] = (df[tool] == 'YES').mean() * 100
    most_popular_tool = max(tool_usage, key=tool_usage.get)
    print(f"   • Most popular AI tool: {most_popular_tool} ({tool_usage[most_popular_tool]:.1f}%)")
    
    # Most popular payment method
    payment_usage = {}
    for method in payment_methods:
        method_name = method.replace('Payment_Method_', '')
        payment_usage[method_name] = (df[method] == 'YES').mean() * 100
    most_popular_payment = max(payment_usage, key=payment_usage.get)
    print(f"   • Most popular payment: {most_popular_payment} ({payment_usage[most_popular_payment]:.1f}%)")
    
    # Most popular product category
    category_usage = {}
    for category in product_categories:
        category_name = category.replace('Product_Category_', '')
        category_usage[category_name] = (df[category] == 'YES').mean() * 100
    most_popular_category = max(category_usage, key=category_usage.get)
    print(f"   • Most popular category: {most_popular_category} ({category_usage[most_popular_category]:.1f}%)")
    
    # AI satisfaction vs endorsement
    ai_endorsers = df[df['AI_Endorsement'] == 'YES']
    ai_satisfaction_rate = (ai_endorsers['AI_Satisfication'] == 'Satisfied').mean() * 100
    print(f"   • AI satisfaction among endorsers: {ai_satisfaction_rate:.1f}%")
    
    print("\n" + "=" * 60)
    print("🎯 For interactive analysis, run: streamlit run dashboard.py")
    print("=" * 60)

if __name__ == "__main__":
    load_and_analyze_data() 