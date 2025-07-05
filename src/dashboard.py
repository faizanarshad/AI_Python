import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="E-commerce AI Behavior Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    /* Global Background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    /* Main Content Background */
    .main .block-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
    }
    
    /* Sidebar Background */
    .css-1d391kg {
        background: linear-gradient(180deg, rgba(102, 126, 234, 0.9) 0%, rgba(118, 75, 162, 0.9) 100%);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Main Header with Animation */
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #ffffff, #f8f9fa, #e9ecef, #ffffff);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 3s ease infinite;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Subtitle */
    .subtitle {
        font-size: 1.2rem;
        color: #6c757d;
        text-align: center;
        margin-bottom: 2rem;
        font-style: italic;
        font-weight: 300;
    }
    
    /* Dashboard Info Card */
    .dashboard-info {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.9) 0%, rgba(118, 75, 162, 0.9) 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.2);
        border: 1px solid rgba(255,255,255,0.3);
        backdrop-filter: blur(20px);
        position: relative;
        overflow: hidden;
    }
    
    .dashboard-info::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    .dashboard-info h3 {
        color: white;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .dashboard-info p {
        color: rgba(255,255,255,0.9);
        text-align: center;
        line-height: 1.6;
    }
    
    /* Enhanced Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    /* Enhanced Section Headers */
    .section-header {
        font-size: 2rem;
        background: linear-gradient(90deg, #2c3e50, #3498db);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        font-weight: bold;
        text-align: center;
        position: relative;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 2px;
    }
    
    /* Enhanced Chart Containers */
    .chart-container {
        background: rgba(255,255,255,0.15);
        border-radius: 1.5rem;
        padding: 2rem;
        border: 1px solid rgba(255,255,255,0.3);
        backdrop-filter: blur(15px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        margin-bottom: 1.5rem;
    }
    
    .chart-container:hover {
        box-shadow: 0 15px 45px rgba(0,0,0,0.2);
        transform: translateY(-5px);
        background: rgba(255,255,255,0.2);
    }
    
    /* Enhanced Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Enhanced Select Boxes */
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.1);
        border-radius: 0.5rem;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Status Badge */
    .status-badge {
        display: inline-block;
        background: linear-gradient(45deg, #00ff88, #00cc6a);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 2rem;
        font-size: 0.9rem;
        font-weight: bold;
        margin: 0.5rem;
        box-shadow: 0 2px 10px rgba(0,255,136,0.3);
    }
    
    /* Feature Icons */
    .feature-icon {
        font-size: 2rem;
        margin: 0 0.5rem;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and preprocess the dataset"""
    try:
        # Try to load from the new assets/data directory
        df = pd.read_csv('assets/data/Dataset.csv')
    except FileNotFoundError:
        try:
            # Fallback to root directory
            df = pd.read_csv('Dataset.csv')
        except FileNotFoundError:
            st.error("❌ Dataset.csv not found! Please ensure the file is in assets/data/ directory.")
            return pd.DataFrame()
    except UnicodeDecodeError:
        try:
            df = pd.read_csv('assets/data/Dataset.csv', encoding='latin-1')
        except:
            df = pd.read_csv('assets/data/Dataset.csv', encoding='cp1252')
    
    # Clean column names
    df.columns = df.columns.str.strip()
    
    # Handle missing values
    df = df.fillna('Unknown')
    
    return df

@st.cache_data
def preprocess_data(df):
    """Preprocess data for analysis"""
    # Create age group mapping
    age_mapping = {
        'Gen Z': '18-25',
        'Millennials': '26-40', 
        'Gen X': '41-56',
        'Baby Boomers': '57-75'
    }
    df['Age_Group'] = df['Age'].map(age_mapping)
    
    # Create salary categories
    salary_mapping = {
        'Low': 'Low (<$50K)',
        'Medium': 'Medium ($50K-$100K)',
        'Medium High': 'Medium High ($100K-$150K)',
        'High': 'High (>$150K)'
    }
    df['Salary_Category'] = df['Annual_Salary'].map(salary_mapping)
    
    return df

def create_advanced_demographics(df):
    """Create advanced demographics section with interactive charts"""
    st.markdown('<h2 class="section-header">📊 Advanced Demographics Analysis</h2>', unsafe_allow_html=True)
    
    # Key metrics with enhanced styling
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_consumers = len(df)
        st.markdown(f"""
        <div class="metric-card">
            <h3>👥 Total Consumers</h3>
            <h2>{total_consumers:,}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        online_consumers = len(df[df['Online_Consumer'] == 'YES'])
        online_percentage = float(online_consumers / total_consumers * 100)
        st.markdown(f"""
        <div class="metric-card">
            <h3>🛒 Online Consumers</h3>
            <h2>{online_consumers:,}</h2>
            <p>{online_percentage:.1f}%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        ai_endorsers = len(df[df['AI_Endorsement'] == 'YES'])
        ai_percentage = float(ai_endorsers / total_consumers * 100)
        st.markdown(f"""
        <div class="metric-card">
            <h3>🤖 AI Endorsers</h3>
            <h2>{ai_endorsers:,}</h2>
            <p>{ai_percentage:.1f}%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        satisfied_ai = len(df[df['AI_Satisfication'] == 'Satisfied'])
        satisfied_percentage = float(satisfied_ai / total_consumers * 100)
        st.markdown(f"""
        <div class="metric-card">
            <h3>😊 AI Satisfied</h3>
            <h2>{satisfied_ai:,}</h2>
            <p>{satisfied_percentage:.1f}%</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Advanced demographics charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Interactive Sunburst Chart for Demographics
        # Create a numerical column for coloring
        df_sunburst = df.copy()
        df_sunburst['AI_Endorsement_Numeric'] = (df_sunburst['AI_Endorsement'] == 'YES').astype(int)
        
        fig_sunburst = px.sunburst(
            df_sunburst, 
            path=['Country', 'Age', 'Gender'], 
            title="🌍 Demographics Sunburst Chart",
            color='AI_Endorsement_Numeric',
            color_continuous_scale='viridis',
            hover_data=['Education', 'Annual_Salary']
        )
        fig_sunburst.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=500
        )
        st.plotly_chart(fig_sunburst, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Interactive Treemap for Age and Education
        # Create a numerical column for coloring
        df_treemap = df.copy()
        df_treemap['AI_Endorsement_Numeric'] = (df_treemap['AI_Endorsement'] == 'YES').astype(int)
        
        fig_treemap = px.treemap(
            df_treemap,
            path=['Age', 'Education', 'Gender'],
            values='AI_Endorsement_Numeric',
            color='AI_Endorsement_Numeric',
            color_continuous_scale='viridis',
            title="🎓 Education & Age Treemap"
        )
        fig_treemap.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=500
        )
        st.plotly_chart(fig_treemap, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 3D Scatter Plot for Demographics
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    # Create numeric mapping for 3D plot
    le_country = LabelEncoder()
    le_age = LabelEncoder()
    le_gender = LabelEncoder()
    
    df_3d = df.copy()
    df_3d['Country_encoded'] = le_country.fit_transform(df_3d['Country'])
    df_3d['Age_encoded'] = le_age.fit_transform(df_3d['Age'])
    df_3d['Gender_encoded'] = le_gender.fit_transform(df_3d['Gender'])
    df_3d['AI_Endorsement_encoded'] = (df_3d['AI_Endorsement'] == 'YES').astype(int)
    
    fig_3d = px.scatter_3d(
        df_3d,
        x='Country_encoded',
        y='Age_encoded', 
        z='Gender_encoded',
        color='AI_Endorsement',
        size='AI_Endorsement_encoded',
        hover_data=['Country', 'Age', 'Gender', 'Education'],
        title="🌐 3D Demographics Scatter Plot",
        color_discrete_map={'YES': '#00ff88', 'NO': '#ff4444'}
    )
    fig_3d.update_layout(
        title_font_size=20,
        title_x=0.5,
        height=600,
        scene=dict(
            xaxis_title="Country",
            yaxis_title="Age Group",
            zaxis_title="Gender"
        )
    )
    st.plotly_chart(fig_3d, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def create_advanced_ai_analysis(df):
    """Create advanced AI adoption analysis with interactive charts"""
    st.markdown('<h2 class="section-header">🤖 Advanced AI Adoption Analysis</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Animated Bar Chart for AI Endorsement by Age
        ai_age_data = df.groupby('Age')['AI_Endorsement'].apply(lambda x: (x == 'YES').mean() * 100).reset_index()
        fig_ai_age = px.bar(
            ai_age_data, 
            x='Age', 
            y='AI_Endorsement',
            title="📈 AI Endorsement by Age Group",
            color='AI_Endorsement',
            color_continuous_scale='viridis',
            animation_frame='Age',
            range_y=[0, 100]
        )
        fig_ai_age.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=400,
            xaxis_title="Age Group",
            yaxis_title="AI Endorsement Rate (%)"
        )
        st.plotly_chart(fig_ai_age, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Interactive Donut Chart for AI Tools Usage
        ai_tools = ['AI_Tools_Used _Chatbots', 'AI_Tools_Used_Virtual_Assistant', 'AI_Tools_Used_Voice&Photo_Search']
        tool_usage = []
        
        for tool in ai_tools:
            usage_rate = (df[tool] == 'YES').mean() * 100
            tool_usage.append({'Tool': tool.replace('AI_Tools_Used_', ''), 'Usage_Rate': usage_rate})
        
        tool_df = pd.DataFrame(tool_usage)
        
        fig_donut = px.pie(
            tool_df, 
            values='Usage_Rate', 
            names='Tool',
            title="🛠️ AI Tools Usage Distribution",
            hole=0.6
        )
        fig_donut.update_traces(
            textposition='inside', 
            textinfo='percent+label',
            hovertemplate="<b>%{label}</b><br>Usage Rate: %{value:.1f}%<extra></extra>"
        )
        fig_donut.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=400
        )
        st.plotly_chart(fig_donut, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Advanced AI Analysis with Parallel Categories
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    # Prepare data for parallel categories
    ai_analysis_data = df[['Age', 'Education', 'Country', 'AI_Endorsement', 'AI_Satisfication']].copy()
    
    # Convert AI_Endorsement to numerical for coloring
    ai_analysis_data['AI_Endorsement_Numeric'] = (ai_analysis_data['AI_Endorsement'] == 'YES').astype(int)
    
    fig_parallel = px.parallel_categories(
        ai_analysis_data,
        dimensions=['Age', 'Education', 'Country', 'AI_Endorsement', 'AI_Satisfication'],
        color='AI_Endorsement_Numeric',
        color_continuous_scale='viridis',
        title="🔄 AI Adoption Journey Analysis"
    )
    fig_parallel.update_layout(
        title_font_size=20,
        title_x=0.5,
        height=500
    )
    st.plotly_chart(fig_parallel, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # AI Tools Usage Heatmap
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # AI Tools Usage by Age Heatmap
        ai_tools_age_data = []
        for tool in ai_tools:
            for age in df['Age'].unique():
                subset = df[df['Age'] == age]
                usage_rate = (subset[tool] == 'YES').mean() * 100
                ai_tools_age_data.append({
                    'Tool': tool.replace('AI_Tools_Used_', ''),
                    'Age': age,
                    'Usage_Rate': usage_rate
                })
        
        ai_tools_age_df = pd.DataFrame(ai_tools_age_data)
        ai_tools_pivot = ai_tools_age_df.pivot(index='Age', columns='Tool', values='Usage_Rate')
        
        fig_ai_heatmap = go.Figure(data=go.Heatmap(
            z=ai_tools_pivot.values,
            x=ai_tools_pivot.columns,
            y=ai_tools_pivot.index,
            colorscale='Viridis',
            colorbar=dict(title='Usage Rate (%)')
        ))
        fig_ai_heatmap.update_layout(
            title="🔥 AI Tools Usage by Age Heatmap",
            xaxis_title="AI Tools",
            yaxis_title="Age Group",
            title_font_size=20,
            title_x=0.5,
            height=400
        )
        st.plotly_chart(fig_ai_heatmap, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # AI Satisfaction vs Endorsement Scatter
        ai_satisfaction_data = df.groupby(['Age', 'Country'])['AI_Satisfication'].apply(
            lambda x: (x == 'Satisfied').mean() * 100).reset_index()
        ai_endorsement_data = df.groupby(['Age', 'Country'])['AI_Endorsement'].apply(
            lambda x: (x == 'YES').mean() * 100).reset_index()
        
        ai_combined = ai_satisfaction_data.merge(ai_endorsement_data, on=['Age', 'Country'])
        
        fig_scatter = px.scatter(
            ai_combined,
            x='AI_Endorsement',
            y='AI_Satisfication',
            color='Country',
            size='AI_Endorsement',
            hover_data=['Age'],
            title="📊 AI Satisfaction vs Endorsement",
            trendline="ols"
        )
        fig_scatter.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=400,
            xaxis_title="AI Endorsement Rate (%)",
            yaxis_title="AI Satisfaction Rate (%)"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

def create_advanced_payment_analysis(df):
    """Create advanced payment method analysis"""
    st.markdown('<h2 class="section-header">💳 Advanced Payment Method Analysis</h2>', unsafe_allow_html=True)
    
    payment_methods = ['Payment_Method_Credit/Debit', 'Payment_Method_COD', 'Payment_Method_Ewallet']
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Stacked Bar Chart for Payment Methods by Age
        payment_age_data = []
        for method in payment_methods:
            for age in df['Age'].unique():
                subset = df[df['Age'] == age]
                usage_rate = (subset[method] == 'YES').mean() * 100
                payment_age_data.append({
                    'Method': method.replace('Payment_Method_', ''),
                    'Age': age,
                    'Usage_Rate': usage_rate
                })
        
        payment_age_df = pd.DataFrame(payment_age_data)
        
        fig_stacked = px.bar(
            payment_age_df,
            x='Age',
            y='Usage_Rate',
            color='Method',
            title="📊 Payment Method Preferences by Age",
            barmode='stack'
        )
        fig_stacked.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=400,
            xaxis_title="Age Group",
            yaxis_title="Usage Rate (%)"
        )
        st.plotly_chart(fig_stacked, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Interactive Radar Chart for Payment Methods
        payment_radar_data = []
        for method in payment_methods:
            usage_rate = (df[method] == 'YES').mean() * 100
            payment_radar_data.append({
                'Method': method.replace('Payment_Method_', ''),
                'Usage_Rate': usage_rate
            })
        
        payment_radar_df = pd.DataFrame(payment_radar_data)
        
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=payment_radar_df['Usage_Rate'],
            theta=payment_radar_df['Method'],
            fill='toself',
            name='Payment Methods',
            line_color='#ff7f0e'
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=False,
            title="🎯 Payment Methods Radar Chart",
            title_font_size=20,
            title_x=0.5,
            height=400
        )
        st.plotly_chart(fig_radar, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Payment Methods by Country and Region
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    payment_geo_data = []
    for method in payment_methods:
        for country in df['Country'].unique():
            for region in df['Living_Region'].unique():
                subset = df[(df['Country'] == country) & (df['Living_Region'] == region)]
                if len(subset) > 0:
                    usage_rate = (subset[method] == 'YES').mean() * 100
                    payment_geo_data.append({
                        'Method': method.replace('Payment_Method_', ''),
                        'Country': country,
                        'Region': region,
                        'Usage_Rate': usage_rate
                    })
    
    payment_geo_df = pd.DataFrame(payment_geo_data)
    
    fig_geo_payment = px.scatter(
        payment_geo_df,
        x='Country',
        y='Usage_Rate',
        color='Method',
        size='Usage_Rate',
        hover_data=['Region'],
        title="🌍 Payment Methods by Geography",
        animation_frame='Method'
    )
    fig_geo_payment.update_layout(
        title_font_size=20,
        title_x=0.5,
        height=500,
        xaxis_title="Country",
        yaxis_title="Usage Rate (%)"
    )
    st.plotly_chart(fig_geo_payment, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def create_advanced_product_analysis(df):
    """Create advanced product category analysis"""
    st.markdown('<h2 class="section-header">🛍️ Advanced Product Category Analysis</h2>', unsafe_allow_html=True)
    
    product_categories = [
        'Product_Category_Appliances', 'Product_Category_Electronics',
        'Product_Category_Groceries', 'Product_Category_Personal_Care',
        'Product_Category_Clothing'
    ]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Interactive Bubble Chart for Product Categories
        category_data = []
        for category in product_categories:
            purchase_rate = (df[category] == 'YES').mean() * 100
            category_data.append({
                'Category': category.replace('Product_Category_', ''),
                'Purchase_Rate': purchase_rate,
                'Size': purchase_rate * 2  # For bubble size
            })
        
        category_df = pd.DataFrame(category_data)
        
        fig_bubble = px.scatter(
            category_df,
            x='Category',
            y='Purchase_Rate',
            size='Size',
            color='Purchase_Rate',
            color_continuous_scale='viridis',
            title="🫧 Product Category Purchase Rates",
            hover_data=['Purchase_Rate']
        )
        fig_bubble.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=400,
            xaxis_title="Product Category",
            yaxis_title="Purchase Rate (%)"
        )
        st.plotly_chart(fig_bubble, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Product Categories by AI Endorsement
        category_ai_data = []
        for category in product_categories:
            ai_endorsers = df[df['AI_Endorsement'] == 'YES']
            non_ai_endorsers = df[df['AI_Endorsement'] == 'NO']
            
            ai_rate = (ai_endorsers[category] == 'YES').mean() * 100
            non_ai_rate = (non_ai_endorsers[category] == 'YES').mean() * 100
            
            category_ai_data.extend([
                {'Category': category.replace('Product_Category_', ''), 'Group': 'AI Endorsers', 'Rate': ai_rate},
                {'Category': category.replace('Product_Category_', ''), 'Group': 'Non-AI Endorsers', 'Rate': non_ai_rate}
            ])
        
        category_ai_df = pd.DataFrame(category_ai_data)
        
        fig_category_ai = px.bar(
            category_ai_df,
            x='Category',
            y='Rate',
            color='Group',
            title="🤖 Category Preferences by AI Endorsement",
            barmode='group'
        )
        fig_category_ai.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=400,
            xaxis_title="Product Category",
            yaxis_title="Purchase Rate (%)"
        )
        st.plotly_chart(fig_category_ai, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Advanced Product Analysis with Parallel Categories
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    # Prepare data for product analysis
    product_analysis_data = df[['Age', 'Country', 'AI_Endorsement'] + product_categories].copy()
    
    # Convert product categories to single column
    product_melted = []
    for _, row in product_analysis_data.iterrows():
        for category in product_categories:
            if row[category] == 'YES':
                product_melted.append({
                    'Age': row['Age'],
                    'Country': row['Country'],
                    'AI_Endorsement': row['AI_Endorsement'],
                    'Product_Category': category.replace('Product_Category_', ''),
                    'Purchased': 'Yes'
                })
    
    product_melted_df = pd.DataFrame(product_melted)
    
    if len(product_melted_df) > 0:
        # Convert AI_Endorsement to numerical for coloring
        product_melted_df['AI_Endorsement_Numeric'] = (product_melted_df['AI_Endorsement'] == 'YES').astype(int)
        
        fig_product_parallel = px.parallel_categories(
            product_melted_df,
            dimensions=['Age', 'Country', 'AI_Endorsement', 'Product_Category'],
            color='AI_Endorsement_Numeric',
            color_continuous_scale='viridis',
            title="🔄 Product Purchase Journey Analysis"
        )
        fig_product_parallel.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=500
        )
        st.plotly_chart(fig_product_parallel, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def create_advanced_geographic_analysis(df):
    """Create advanced geographic analysis"""
    st.markdown('<h2 class="section-header">🌍 Advanced Geographic Analysis</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Interactive Bubble Map for Countries
        country_stats = df.groupby('Country').agg({
            'AI_Endorsement': lambda x: (x == 'YES').mean() * 100,
            'Online_Consumer': lambda x: (x == 'YES').mean() * 100,
            'AI_Satisfication': lambda x: (x == 'Satisfied').mean() * 100
        }).reset_index()
        
        fig_bubble_map = px.scatter(
            country_stats,
            x='AI_Endorsement',
            y='Online_Consumer',
            size='AI_Satisfication',
            color='Country',
            hover_data=['AI_Satisfication'],
            title="🌐 Country Performance Bubble Chart"
        )
        fig_bubble_map.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=400,
            xaxis_title="AI Endorsement Rate (%)",
            yaxis_title="Online Consumer Rate (%)"
        )
        st.plotly_chart(fig_bubble_map, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Region Distribution with Sunburst
        # Create a numerical column for coloring
        df_geo_sunburst = df.copy()
        df_geo_sunburst['AI_Endorsement_Numeric'] = (df_geo_sunburst['AI_Endorsement'] == 'YES').astype(int)
        
        fig_region_sunburst = px.sunburst(
            df_geo_sunburst,
            path=['Country', 'Living_Region', 'Age'],
            title="🗺️ Geographic Distribution Sunburst",
            color='AI_Endorsement_Numeric',
            color_continuous_scale='viridis'
        )
        fig_region_sunburst.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=400
        )
        st.plotly_chart(fig_region_sunburst, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Geographic AI Adoption Heatmap
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    geo_ai_data = df.groupby(['Country', 'Living_Region'])['AI_Endorsement'].apply(
        lambda x: (x == 'YES').mean() * 100).reset_index()
    
    geo_pivot = geo_ai_data.pivot(index='Living_Region', columns='Country', values='AI_Endorsement')
    
    fig_geo_heatmap = go.Figure(data=go.Heatmap(
        z=geo_pivot.values,
        x=geo_pivot.columns,
        y=geo_pivot.index,
        colorscale='Viridis',
        colorbar=dict(title='AI Endorsement (%)')
    ))
    fig_geo_heatmap.update_layout(
        title="🔥 AI Endorsement Rate by Country and Region",
        xaxis_title="Country",
        yaxis_title="Living Region",
        title_font_size=20,
        title_x=0.5,
        height=500
    )
    st.plotly_chart(fig_geo_heatmap, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def create_advanced_customer_segmentation(df):
    """Create advanced customer segmentation analysis"""
    st.markdown('<h2 class="section-header">👥 Advanced Customer Segmentation</h2>', unsafe_allow_html=True)
    
    # Prepare data for clustering
    le = LabelEncoder()
    df_cluster = df.copy()
    
    # Encode categorical variables
    categorical_cols = ['Age', 'Gender', 'Education', 'Annual_Salary', 'Living_Region']
    for col in categorical_cols:
        df_cluster[col + '_encoded'] = le.fit_transform(df_cluster[col])
    
    # Select features for clustering
    features = [col + '_encoded' for col in categorical_cols] + ['AI_Endorsement']
    X = df_cluster[features].copy()
    X['AI_Endorsement'] = (X['AI_Endorsement'] == 'YES').astype(int)
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=4, random_state=42)
    df_cluster['Cluster'] = kmeans.fit_predict(X)
    
    # Create AI_Endorsement_encoded column for the 3D plot
    df_cluster['AI_Endorsement_encoded'] = (df_cluster['AI_Endorsement'] == 'YES').astype(int)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # 3D Scatter Plot for Clusters
        fig_cluster_3d = px.scatter_3d(
            df_cluster,
            x='Age_encoded',
            y='Education_encoded',
            z='Annual_Salary_encoded',
            color='Cluster',
            size='AI_Endorsement_encoded',
            hover_data=['Age', 'Education', 'Annual_Salary', 'Gender'],
            title="🎯 3D Customer Segmentation"
        )
        fig_cluster_3d.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=500,
            scene=dict(
                xaxis_title="Age Group",
                yaxis_title="Education Level",
                zaxis_title="Salary Level"
            )
        )
        st.plotly_chart(fig_cluster_3d, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Cluster Characteristics Radar Chart
        cluster_analysis = df_cluster.groupby('Cluster').agg({
            'AI_Endorsement': lambda x: (x == 'YES').mean() * 100,
            'Online_Consumer': lambda x: (x == 'YES').mean() * 100,
            'AI_Satisfication': lambda x: (x == 'Satisfied').mean() * 100
        }).reset_index()
        
        fig_radar_cluster = go.Figure()
        
        for _, cluster in cluster_analysis.iterrows():
            fig_radar_cluster.add_trace(go.Scatterpolar(
                r=[cluster['AI_Endorsement'], cluster['Online_Consumer'], cluster['AI_Satisfication']],
                theta=['AI Endorsement', 'Online Consumer', 'AI Satisfaction'],
                fill='toself',
                name=f'Cluster {cluster["Cluster"]}'
            ))
        
        fig_radar_cluster.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            title="🎯 Cluster Characteristics Radar",
            title_font_size=20,
            title_x=0.5,
            height=500
        )
        st.plotly_chart(fig_radar_cluster, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Cluster Analysis Table
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    cluster_summary = df_cluster.groupby('Cluster').agg({
        'Age': lambda x: x.mode()[0] if len(x.mode()) > 0 else 'Unknown',
        'Gender': lambda x: x.mode()[0] if len(x.mode()) > 0 else 'Unknown',
        'AI_Endorsement': lambda x: (x == 'YES').mean() * 100,
        'Online_Consumer': lambda x: (x == 'YES').mean() * 100
    }).round(2)
    
    cluster_summary.columns = ['Most Common Age', 'Most Common Gender', 'AI Endorsement %', 'Online Consumer %']
    
    st.subheader("📊 Cluster Analysis Results")
    st.dataframe(cluster_summary, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def create_advanced_insights(df):
    """Create advanced insights with interactive elements"""
    st.markdown('<h2 class="section-header">💡 Advanced Business Insights</h2>', unsafe_allow_html=True)
    
    # Calculate key metrics
    total_consumers = len(df)
    ai_endorsement_rate = float((df['AI_Endorsement'] == 'YES').mean() * 100)
    online_consumer_rate = float((df['Online_Consumer'] == 'YES').mean() * 100)
    ai_satisfaction_rate = float((df['AI_Satisfication'] == 'Satisfied').mean() * 100)
    
    # Most popular AI tool
    ai_tools = ['AI_Tools_Used _Chatbots', 'AI_Tools_Used_Virtual_Assistant', 'AI_Tools_Used_Voice&Photo_Search']
    tool_usage = {}
    for tool in ai_tools:
        tool_name = tool.replace('AI_Tools_Used_', '')
        tool_usage[tool_name] = (df[tool] == 'YES').mean() * 100
    
    most_popular_tool = max(tool_usage, key=tool_usage.get)
    
    # Most popular payment method
    payment_methods = ['Payment_Method_Credit/Debit', 'Payment_Method_COD', 'Payment_Method_Ewallet']
    payment_usage = {}
    for method in payment_methods:
        method_name = method.replace('Payment_Method_', '')
        payment_usage[method_name] = (df[method] == 'YES').mean() * 100
    
    most_popular_payment = max(payment_usage, key=payment_usage.get)
    
    # Most popular product category
    product_categories = [
        'Product_Category_Appliances', 'Product_Category_Electronics',
        'Product_Category_Groceries', 'Product_Category_Personal_Care',
        'Product_Category_Clothing'
    ]
    category_usage = {}
    for category in product_categories:
        category_name = category.replace('Product_Category_', '')
        category_usage[category_name] = (df[category] == 'YES').mean() * 100
    
    most_popular_category = max(category_usage, key=category_usage.get)
    
    # AI adoption insights
    ai_by_age = df.groupby('Age')['AI_Endorsement'].apply(lambda x: (x == 'YES').mean() * 100)
    highest_ai_age = ai_by_age.idxmax()
    lowest_ai_age = ai_by_age.idxmin()
    
    # AI endorsement by education
    ai_by_edu = df.groupby('Education')['AI_Endorsement'].apply(lambda x: (x == 'YES').mean() * 100)
    highest_ai_edu = ai_by_edu.idxmax()
    
    # Create interactive insights dashboard
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📈 Market Overview
        """)
        st.metric("Total Consumers", f"{total_consumers:,}")
        st.metric("Online Consumer Rate", f"{online_consumer_rate:.1f}%")
        st.metric("AI Endorsement Rate", f"{ai_endorsement_rate:.1f}%")
        st.metric("AI Satisfaction Rate", f"{ai_satisfaction_rate:.1f}%")
    
    with col2:
        st.markdown("""
        ### 🏆 Top Performers
        """)
        st.metric("Most Popular AI Tool", most_popular_tool)
        st.metric("Most Popular Payment", most_popular_payment)
        st.metric("Most Popular Category", most_popular_category)
    
    # Interactive insights chart
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    insights_data = {
        'Metric': ['AI Endorsement', 'Online Consumer', 'AI Satisfaction'],
        'Rate': [ai_endorsement_rate, online_consumer_rate, ai_satisfaction_rate]
    }
    insights_df = pd.DataFrame(insights_data)
    
    fig_insights = px.bar(
        insights_df,
        x='Metric',
        y='Rate',
        color='Rate',
        color_continuous_scale='viridis',
        title="📊 Key Performance Metrics"
    )
    fig_insights.update_layout(
        title_font_size=20,
        title_x=0.5,
        height=400,
        xaxis_title="Metrics",
        yaxis_title="Rate (%)"
    )
    st.plotly_chart(fig_insights, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # AI adoption insights
    st.markdown("""
    ### 🤖 AI Adoption Insights
    """)
    st.markdown(f"""
    - **Highest AI Adoption Age Group:** {highest_ai_age} ({ai_by_age[highest_ai_age]:.1f}%)
    - **Lowest AI Adoption Age Group:** {lowest_ai_age} ({ai_by_age[lowest_ai_age]:.1f}%)
    - **Highest AI Adoption Education Level:** {highest_ai_edu} ({ai_by_edu[highest_ai_edu]:.1f}%)
    """)

def main():
    """Main dashboard function"""
    # Attractive Header Section
    st.markdown('<h1 class="main-header">🚀 AI-Powered E-commerce Analytics Hub</h1>', unsafe_allow_html=True)
    
    st.markdown('<p class="subtitle">Comprehensive Consumer Behavior Analysis & AI Adoption Insights</p>', unsafe_allow_html=True)
    
    # Dashboard Info Card
    st.markdown("""
    <div class="dashboard-info">
        <h3>🎯 Dashboard Overview</h3>
        <p>
            <span class="feature-icon">📊</span> Advanced Demographics Analysis
            <span class="feature-icon">🤖</span> AI Adoption Patterns
            <span class="feature-icon">💳</span> Payment Method Trends
            <span class="feature-icon">🛍️</span> Product Category Insights
            <span class="feature-icon">🌍</span> Geographic Distribution
            <span class="feature-icon">👥</span> Customer Segmentation
        </p>
        <div style="text-align: center; margin-top: 1rem;">
            <span class="status-badge">🟢 Live Analytics</span>
            <span class="status-badge">📈 Real-time Data</span>
            <span class="status-badge">🎨 Interactive Charts</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Load and preprocess data
    df = load_data()
    df = preprocess_data(df)
    
    # Sidebar filters with enhanced styling
    st.sidebar.markdown("## 🔍 Advanced Filters")
    
    # Country filter
    selected_countries = st.sidebar.multiselect(
        "🌍 Select Countries",
        options=df['Country'].unique(),
        default=df['Country'].unique()
    )
    
    # Age filter
    selected_ages = st.sidebar.multiselect(
        "👥 Select Age Groups",
        options=df['Age'].unique(),
        default=df['Age'].unique()
    )
    
    # Gender filter
    selected_genders = st.sidebar.multiselect(
        "👤 Select Gender",
        options=df['Gender'].unique(),
        default=df['Gender'].unique()
    )
    
    # AI Endorsement filter
    selected_ai = st.sidebar.multiselect(
        "🤖 Select AI Endorsement",
        options=df['AI_Endorsement'].unique(),
        default=df['AI_Endorsement'].unique()
    )
    
    # Apply filters
    filtered_df = df[
        (df['Country'].isin(selected_countries)) &
        (df['Age'].isin(selected_ages)) &
        (df['Gender'].isin(selected_genders)) &
        (df['AI_Endorsement'].isin(selected_ai))
    ]
    
    # Display filtered data info
    st.sidebar.markdown(f"**📊 Filtered Data:** {len(filtered_df)} records")
    
    # Add download button for filtered data
    if st.sidebar.button("📥 Download Filtered Data"):
        csv = filtered_df.to_csv(index=False)
        st.sidebar.download_button(
            label="Download CSV",
            data=csv,
            file_name="filtered_ecommerce_data.csv",
            mime="text/csv"
        )
    
    # Create dashboard sections
    create_advanced_demographics(filtered_df)
    create_advanced_ai_analysis(filtered_df)
    create_advanced_payment_analysis(filtered_df)
    create_advanced_product_analysis(filtered_df)
    create_advanced_geographic_analysis(filtered_df)
    create_advanced_customer_segmentation(filtered_df)
    create_advanced_insights(filtered_df)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>📊 Advanced E-commerce AI Behavior Dashboard | Built with Streamlit and Plotly</p>
        <p>🚀 Interactive Analytics & Business Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 