# 🚀 Getting Started Guide

Welcome to the **AI-Powered E-commerce Analytics Hub**! This guide will help you get up and running quickly.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Git** (for version control)

### System Requirements

- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Memory**: Minimum 4GB RAM (8GB recommended)
- **Storage**: 2GB free space
- **Browser**: Modern browser (Chrome, Firefox, Safari, Edge)

## 🚀 Quick Start

### Option 1: Using the Launcher Script (Recommended)

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd AI_Python
   ```

2. **Make the launcher script executable**
   ```bash
   chmod +x run_dashboard.sh
   ```

3. **Run the dashboard**
   ```bash
   ./run_dashboard.sh
   ```

### Option 2: Manual Installation

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the dashboard**
   ```bash
   streamlit run app.py
   ```

### Option 3: Using Make (Advanced)

1. **Install development dependencies**
   ```bash
   make install-dev
   ```

2. **Run in development mode**
   ```bash
   make run-dev
   ```

## 🌐 Accessing the Dashboard

Once the dashboard is running, you can access it at:

- **Local URL**: `http://localhost:8501`
- **Network URL**: `http://your-ip:8501`

The dashboard will automatically open in your default browser.

## 📊 Understanding the Dashboard

### Main Sections

1. **🎯 Demographics Overview**
   - Consumer age distribution
   - Gender breakdown
   - Education levels
   - Geographic distribution

2. **🤖 AI Adoption Analysis**
   - AI endorsement rates
   - AI tools usage
   - Satisfaction levels
   - Adoption trends

3. **💳 Payment Method Analysis**
   - Payment preferences
   - Usage rates by demographic
   - Geographic patterns

4. **🛍️ Product Category Analysis**
   - Category preferences
   - Purchase patterns
   - Cross-category insights

5. **🌍 Geographic Analysis**
   - Country-wise performance
   - Regional trends
   - Market opportunities

6. **👥 Customer Segmentation**
   - AI-powered clustering
   - Segment characteristics
   - Behavioral patterns

7. **💡 Business Insights**
   - Key performance metrics
   - Actionable recommendations
   - Trend analysis

### Interactive Features

- **Filters**: Filter data by country, age, gender, and AI endorsement
- **Charts**: Interactive visualizations with hover effects
- **Download**: Export filtered data as CSV
- **Real-time Updates**: Metrics update based on selected filters

## 🎨 Customization

### Changing Themes

The dashboard supports multiple themes:

1. **Professional** (Default): Clean, business-focused design
2. **Modern**: Dark theme with modern aesthetics
3. **Minimal**: Simple, distraction-free interface

### Customizing Colors

You can modify the color scheme by editing `src/config/settings.py`:

```python
STYLE_CONFIG = {
    "primary_color": "#1f77b4",
    "secondary_color": "#ff7f0e",
    # ... other colors
}
```

### Adding New Charts

To add new visualizations:

1. Create a new function in `src/utils/chart_helpers.py`
2. Import and use it in `src/dashboard.py`
3. Apply consistent theming using `apply_chart_theme()`

## 🔧 Configuration

### Dashboard Settings

Key configuration options in `src/config/settings.py`:

- **Page Title**: Customize the dashboard title
- **Layout**: Wide or centered layout
- **Sidebar State**: Expanded or collapsed by default
- **Cache Settings**: Data caching duration and limits

### Performance Settings

- **Max Data Points**: Limit for large datasets
- **Chart Timeout**: Maximum time for chart rendering
- **Lazy Loading**: Enable/disable lazy loading

## 📈 Data Management

### Supported Data Formats

- **CSV Files**: Primary data format
- **Excel Files**: .xlsx and .xls formats
- **JSON Files**: For API data integration

### Data Requirements

Your dataset should include these columns:

- **Demographics**: Country, Age, Gender, Education, Annual_Salary
- **Behavior**: Online_Consumer, AI_Endorsement, AI_Satisfication
- **Payment Methods**: Payment_Method_* columns
- **Product Categories**: Product_Category_* columns
- **AI Tools**: AI_Tools_Used_* columns

### Data Cleaning

The dashboard automatically:

- Handles missing values
- Converts data types
- Validates data integrity
- Applies filters

## 🛠️ Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   streamlit run app.py --server.port 8502
   ```

2. **Missing Dependencies**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

3. **Data File Not Found**
   - Ensure data files are in `assets/data/`
   - Check file permissions
   - Verify file encoding (UTF-8 recommended)

4. **Memory Issues**
   - Close other applications
   - Reduce dataset size
   - Use data sampling

5. **Display Issues**
   - Clear browser cache
   - Update browser
   - Check internet connection

### Performance Optimization

- **Use modern browsers** for best performance
- **Stable internet connection** for smooth animations
- **Adequate system resources** for 3D visualizations
- **Regular cache clearing** for optimal performance

## 📚 Next Steps

### Learning Resources

1. **API Documentation**: See `docs/api/` for technical details
2. **Examples**: Check `examples/` for sample implementations
3. **Contributing**: Read `CONTRIBUTING.md` for development guidelines

### Advanced Features

1. **Custom Analytics**: Add your own analysis functions
2. **Data Integration**: Connect to external data sources
3. **Export Options**: Customize data export formats
4. **User Management**: Implement authentication and authorization

### Support

- **Documentation**: Comprehensive guides in `docs/`
- **Issues**: Report bugs on GitHub
- **Community**: Join our community discussions
- **Email**: Contact us at contact@aianalytics.com

## 🎉 Congratulations!

You're now ready to explore the AI-Powered E-commerce Analytics Hub! 

Start by:
1. Loading your data
2. Exploring the different sections
3. Using the interactive filters
4. Generating insights
5. Exporting your findings

Happy analyzing! 🚀✨ 