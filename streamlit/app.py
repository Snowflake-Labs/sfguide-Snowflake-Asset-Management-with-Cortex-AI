import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Streamlit App Configuration
st.set_page_config(
    page_title="Asset Management Intelligence Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Page Navigation
page = st.sidebar.selectbox(
    "📋 Navigate",
    ["🏦 Dashboard", "📖 Dashboard Guide"],
    index=0
)

# Title and Header
if page == "🏦 Dashboard":
    st.title("🏦 Asset Management Intelligence Dashboard")
    st.markdown("### Powered by Snowflake Cortex AI")
    st.markdown("---")
elif page == "📖 Dashboard Guide":
    st.title("📖 Dashboard Guide")
    st.markdown("### Understanding Your Asset Management Intelligence Dashboard")
    st.markdown("---")

# Page-specific content
if page == "🏦 Dashboard":
    # Sidebar Controls
    st.sidebar.header("📊 Dashboard Controls")
    refresh_data = st.sidebar.button("🔄 Refresh Data", type="primary")
    selected_time_range = st.sidebar.selectbox(
        "📅 Time Range",
        ["Last 30 Days", "Last 90 Days", "Last 6 Months", "Last Year"]
    )
    risk_threshold = st.sidebar.slider("⚠️ Risk Threshold", 1.0, 10.0, 7.0, 0.5)
    min_portfolio_value = st.sidebar.number_input("💰 Min Portfolio Value ($M)", 0.0, 100.0, 1.0)

    # Help Section
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 💡 Need Help?")
    st.sidebar.markdown("Switch to **📖 Dashboard Guide** page for detailed explanations!")

    # Sample data (in production, this would come from Snowflake Cortex AI queries)
    @st.cache_data
    def load_portfolio_data():
        return pd.DataFrame({
            'Portfolio': ['Growth Fund Alpha', 'ESG Impact Fund', 'Emerging Markets Fund', 'Real Estate Fund', 'Conservative Income', 'Technology Focus', 'Healthcare Plus'],
            'Total_Value': [78.5, 26.8, 19.2, 14.7, 5.1, 42.3, 33.9],  # in millions
            'Risk_Score': [6.5, 5.2, 8.1, 4.8, 3.2, 7.8, 5.9],
            'Tech_Allocation': [15.66, 12.0, 19.0, 0.0, 0.0, 45.2, 8.3],
            'YTD_Return': [12.4, 8.7, -2.3, 6.1, 4.2, 18.9, 14.2],
            'Sharpe_Ratio': [1.2, 1.1, 0.8, 1.0, 1.3, 1.4, 1.2],
            'AI_Sentiment': ['Bullish', 'Neutral', 'Bearish', 'Neutral', 'Bullish', 'Bullish', 'Bullish']
        })

    @st.cache_data
    def load_sector_data():
        return pd.DataFrame({
            'Sector': ['Technology', 'Healthcare', 'Real Estate', 'ESG/Renewable', 'Consumer Goods', 'Financial Services', 'Energy'],
            'Total_Allocation': [68.0, 33.0, 19.0, 8.0, 6.0, 25.4, 12.3],  # in millions
            'Research_Sentiment': ['Bullish', 'Bullish', 'Bearish', 'Bullish', 'Neutral', 'Neutral', 'Bearish'],
            'AI_Score': [8.2, 7.8, 4.3, 8.9, 6.1, 5.5, 3.8],
            'Risk_Level': ['Medium', 'Medium', 'High', 'Low', 'Medium', 'Medium', 'High']
        })

    # Load data
    portfolio_df = load_portfolio_data()
    sector_df = load_sector_data()

    # Filter data based on sidebar controls
    filtered_portfolio = portfolio_df[
        (portfolio_df['Total_Value'] >= min_portfolio_value) & 
        (portfolio_df['Risk_Score'] <= risk_threshold)
    ]

    # Main Dashboard Layout
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total AUM", f"${portfolio_df['Total_Value'].sum():.1f}M", f"{portfolio_df['YTD_Return'].mean():.1f}%")
    with col2:
        st.metric("Avg Risk Score", f"{portfolio_df['Risk_Score'].mean():.1f}", f"{len(filtered_portfolio)} portfolios")
    with col3:
        high_performers = len(portfolio_df[portfolio_df['YTD_Return'] > 10])
        st.metric("High Performers", high_performers, f"{high_performers/len(portfolio_df)*100:.0f}%")
    with col4:
        bullish_count = len(portfolio_df[portfolio_df['AI_Sentiment'] == 'Bullish'])
        st.metric("AI Bullish Signals", bullish_count, f"{bullish_count/len(portfolio_df)*100:.0f}%")

    st.markdown("---")

    # Row 1: Portfolio Analysis
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("�� Portfolio Risk vs Performance Analysis")
        
        # Interactive scatter plot
        fig_scatter = px.scatter(
            filtered_portfolio, 
            x='Risk_Score', 
            y='Total_Value',
            size='Tech_Allocation',
            color='AI_Sentiment',
            hover_data=['YTD_Return', 'Sharpe_Ratio'],
            title='Risk-Adjusted Portfolio Performance',
            labels={
                'Risk_Score': 'Risk Score (1-10)', 
                'Total_Value': 'Portfolio Value ($M)',
                'AI_Sentiment': 'AI Sentiment'
            },
            color_discrete_map={
                'Bullish': '#2E8B57',
                'Neutral': '#FFD700', 
                'Bearish': '#DC143C'
            }
        )
        
        fig_scatter.update_layout(height=500)
        st.plotly_chart(fig_scatter, use_container_width=True)

    with col2:
        st.subheader("🎯 AI Investment Insights")
        
        # AI Insights Panel
        for idx, row in filtered_portfolio.iterrows():
            sentiment_color = {"Bullish": "🟢", "Neutral": "🟡", "Bearish": "🔴"}[row['AI_Sentiment']]
            
            with st.expander(f"{sentiment_color} {row['Portfolio']}"):
                st.write(f"**Value:** ${row['Total_Value']:.1f}M")
                st.write(f"**Risk Score:** {row['Risk_Score']}/10")
                st.write(f"**YTD Return:** {row['YTD_Return']:.1f}%")
                st.write(f"**Sharpe Ratio:** {row['Sharpe_Ratio']:.2f}")
                
                if row['AI_Sentiment'] == 'Bullish':
                    st.success("AI recommends maintaining or increasing allocation")
                elif row['AI_Sentiment'] == 'Bearish':
                    st.error("AI suggests reducing exposure or hedging")
                else:
                    st.info("AI indicates neutral positioning appropriate")

    # Row 2: Sector Analysis and Document Insights
    st.markdown("---")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("🏭 Sector Allocation with AI Sentiment")
        
        # Interactive pie chart with sentiment colors
        colors = {'Bullish': '#2E8B57', 'Neutral': '#FFD700', 'Bearish': '#DC143C'}
        sector_colors = [colors[sentiment] for sentiment in sector_df['Research_Sentiment']]
        
        fig_pie = go.Figure(data=[go.Pie(
            labels=sector_df['Sector'],
            values=sector_df['Total_Allocation'],
            marker_colors=sector_colors,
            textinfo='label+percent+value',
            texttemplate='%{label}<br>%{percent}<br>$%{value:.1f}M',
            hovertemplate='<b>%{label}</b><br>' +
                          'Allocation: $%{value:.1f}M<br>' +
                          'Percentage: %{percent}<br>' +
                          '<extra></extra>'
        )])
        
        fig_pie.update_layout(
            title='Sector Allocation with AI Sentiment<br><sub>🟢Bullish 🟡Neutral ��Bearish</sub>',
            height=500,
            showlegend=False
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)
        
        # Sector performance table
        st.subheader("📊 Sector Performance Metrics")
        sector_display = sector_df.copy()
        sector_display['Total_Allocation'] = sector_display['Total_Allocation'].apply(lambda x: f"${x:.1f}M")
        sector_display['AI_Score'] = sector_display['AI_Score'].apply(lambda x: f"{x:.1f}/10")
        
        st.dataframe(
            sector_display[['Sector', 'Total_Allocation', 'AI_Score', 'Research_Sentiment', 'Risk_Level']],
            use_container_width=True,
            hide_index=True
        )

    with col2:
        st.subheader("📄 AI Document Analysis")
        
        # Document insights from Cortex AI analysis
        document_insights = [
            {
                "document": "Q4_2024_Technology_Sector_Outlook.pdf",
                "ai_summary": "Strong momentum in AI adoption and cloud infrastructure growth. Semiconductor companies showing 25% revenue growth potential.",
                "sentiment": "Bullish",
                "key_risk": "Regulatory concerns around data privacy",
                "recommendation": "15-20% allocation for growth portfolios"
            },
            {
                "document": "ESG_Investment_Trends_2024.pdf", 
                "ai_summary": "Climate transition investments demonstrate 18% annual returns. Social impact bonds show steady 6% yields with lower volatility.",
                "sentiment": "Bullish",
                "key_risk": "Greenwashing concerns and inconsistent ESG metrics",
                "recommendation": "25% allocation for institutional clients"
            },
            {
                "document": "Healthcare_Innovation_Investment_Opportunities.pdf",
                "ai_summary": "Gene therapy success rates at 35%. Telemedicine retention at 40% post-pandemic. Strong defensive characteristics.",
                "sentiment": "Bullish", 
                "key_risk": "Regulatory approval timelines and patent cliff exposure",
                "recommendation": "60% established healthcare, 40% innovation focus"
            }
        ]
        
        for doc in document_insights:
            sentiment_emoji = {"Bullish": "🟢", "Neutral": "🟡", "Bearish": "🔴"}[doc['sentiment']]
            
            with st.expander(f"{sentiment_emoji} {doc['document'][:25]}..."):
                st.write(f"**AI Summary:** {doc['ai_summary']}")
                st.write(f"**Key Risk:** {doc['key_risk']}")
                st.write(f"**Recommendation:** {doc['recommendation']}")
                
                if doc['sentiment'] == 'Bullish':
                    st.success(f"AI Sentiment: {doc['sentiment']} - Positive outlook")
                else:
                    st.info(f"AI Sentiment: {doc['sentiment']}")

    # Row 3: Performance Tracking and Alerts
    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("⚡ Real-time Alerts")
        
        # Simulated alerts based on AI analysis
        alerts = [
            {"type": "warning", "message": "Emerging Markets Fund risk score increased to 8.1", "time": "2 min ago"},
            {"type": "success", "message": "Technology Focus Fund outperforming benchmark by 5.2%", "time": "15 min ago"},
            {"type": "info", "message": "ESG Impact Fund reached target allocation", "time": "1 hour ago"},
            {"type": "warning", "message": "Real Estate sector sentiment shifted to Bearish", "time": "2 hours ago"}
        ]
        
        for alert in alerts:
            if alert["type"] == "warning":
                st.warning(f"⚠️ {alert['message']} ({alert['time']})")
            elif alert["type"] == "success": 
                st.success(f"✅ {alert['message']} ({alert['time']})")
            else:
                st.info(f"ℹ️ {alert['message']} ({alert['time']})")

    with col2:
        st.subheader("🎯 AI Recommendations")
        
        # AI-generated recommendations
        recommendations = [
            "Increase Technology sector allocation by 3-5% based on positive AI sentiment",
            "Consider hedging Real Estate exposure due to bearish outlook", 
            "Rebalance ESG portfolio to capture 18% return opportunity",
            "Monitor Emerging Markets volatility - consider reducing position size"
        ]
        
        for i, rec in enumerate(recommendations, 1):
            st.write(f"**{i}.** {rec}")

    with col3:
        st.subheader("📈 Performance Summary")
        
        # Performance metrics
        total_return = portfolio_df['YTD_Return'].mean()
        best_performer = portfolio_df.loc[portfolio_df['YTD_Return'].idxmax()]
        worst_performer = portfolio_df.loc[portfolio_df['YTD_Return'].idxmin()]
        
        st.metric("Average YTD Return", f"{total_return:.1f}%")
        st.write(f"**Best:** {best_performer['Portfolio']} ({best_performer['YTD_Return']:.1f}%)")
        st.write(f"**Worst:** {worst_performer['Portfolio']} ({worst_performer['YTD_Return']:.1f}%)")
        
        # Risk-adjusted returns
        avg_sharpe = portfolio_df['Sharpe_Ratio'].mean()
        st.metric("Average Sharpe Ratio", f"{avg_sharpe:.2f}")

    # Footer
    st.markdown("---")
    st.markdown("#### 🚀 About This Dashboard")
    st.markdown("""
    This interactive dashboard demonstrates how **Snowflake Cortex AI** can power real-time asset management analytics:

    - **AI_COMPLETE**: Document summarization and insight extraction
    - **AI_CLASSIFY**: Intelligent sentiment analysis and risk categorization  
    - **AI_AGG**: Natural language portfolio analytics
    - **Interactive Controls**: Dynamic filtering and real-time updates

    **💡 Pro Tip:** In production, connect this to live Snowflake data for real-time portfolio monitoring!
    """)

elif page == "📖 Dashboard Guide":
    # Dashboard Guide Page Content
    st.markdown("""
    Welcome to your comprehensive guide for understanding the **Asset Management Intelligence Dashboard**. 
    This AI-powered platform transforms complex financial data into actionable insights.
    """)
    
    # Overview Section
    with st.expander("🔍 **What Does This Dashboard Show You?**", expanded=True):
        st.markdown("""
        This dashboard is your **AI-powered command center** for investment management, answering critical questions:
        
        - **"Which portfolios are performing well?"** → Performance metrics at the top
        - **"What does AI think about our investments?"** → Color-coded sentiment analysis (🟢🟡🔴)
        - **"Where are our biggest risks?"** → Risk scores and real-time alerts
        - **"What do the latest research reports recommend?"** → AI document analysis
        - **"How should we adjust our strategy?"** → Dynamic AI recommendations
        
        **Key Benefits:**
        - 🚀 **90% reduction** in document processing time
        - 📊 **Real-time insights** from AI analysis of market data
        - �� **Actionable recommendations** tailored to your portfolio
        - 📈 **Professional visualizations** for client presentations
        """)
    
    # Dashboard Sections Explanation
    st.subheader("📊 Dashboard Sections Explained")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("📈 **Top Metrics Bar (KPIs)**"):
            st.markdown("""
            **Total AUM (Assets Under Management)**
            - Shows combined value of all portfolios ($220M+ in demo)
            - Tracks business growth and portfolio scale
            
            **Average Risk Score**
            - Portfolio risk on 1-10 scale (higher = more volatile)
            - Helps assess overall risk exposure
            
            **High Performers**
            - Portfolios exceeding 10% annual returns
            - Percentage shows team effectiveness
            
            **AI Bullish Signals**
            - Portfolios AI recommends as "buy/hold"
            - Green percentage indicates AI confidence
            """)
        
        with st.expander("📈 **Risk vs Performance Chart**"):
            st.markdown("""
            **How to Read:**
            - **X-axis:** Risk Score (1-10) - portfolio volatility
            - **Y-axis:** Portfolio Value ($M) - investment size
            - **Dot Size:** Technology allocation (bigger = more tech)
            - **Colors:** AI sentiment about each portfolio
            
            **Color Meanings:**
            - 🟢 **Green (Bullish):** AI recommends keeping/buying more
            - 🟡 **Yellow (Neutral):** AI sees mixed signals
            - 🔴 **Red (Bearish):** AI suggests reducing exposure
            
            **Key Insights:**
            - **Top-right:** High value, high risk (growth-focused)
            - **Bottom-left:** Lower value, lower risk (conservative)
            - **Hover:** See detailed performance metrics
            """)
    
    with col2:
        with st.expander("🏭 **Sector Allocation Pie Chart**"):
            st.markdown("""
            **Visual Elements:**
            - **Slice Size:** Investment amount by industry
            - **Colors:** AI sentiment by sector (same as above)
            - **Labels:** Show percentage and dollar amounts
            
            **Interactive Features:**
            - **Hover:** Detailed allocation information
            - **Click:** Focus on specific sectors
            - **Color patterns:** Quick visual of AI outlook
            
            **Strategic Insights:**
            - Identify over/under-exposed sectors
            - See where AI spots opportunities vs. risks
            - Guide rebalancing decisions
            """)
        
        with st.expander("📄 **AI Document Analysis**"):
            st.markdown("""
            **How It Works:**
            1. AI reads research PDFs using Snowflake Cortex
            2. Extracts key insights via natural language processing
            3. Provides summaries and recommendations
            4. Identifies risks and strategic considerations
            
            **Each Document Shows:**
            - **AI Summary:** Key findings in plain English
            - **Key Risk:** Main concerns identified
            - **Recommendation:** Specific allocation advice
            - **Sentiment:** Overall AI outlook
            
            **Business Value:**
            - Saves hours of manual document review
            - Catches insights humans might miss
            - Standardizes analysis across reports
            """)
    
    # Score Calculations
    st.subheader("🧮 How Are Scores Calculated?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.expander("⚠️ **Risk Scores (1-10)**"):
            st.markdown("""
            **AI analyzes multiple factors:**
            - **Historical volatility** (price fluctuations)
            - **Asset types** (stocks vs. bonds)
            - **Geographic exposure** (emerging markets risk)
            - **Sector concentration** (diversification level)
            
            **Scale interpretation:**
            - **1-3:** Conservative (government bonds, utilities)
            - **4-6:** Balanced (mixed stock/bond portfolios)
            - **7-10:** Aggressive (growth stocks, crypto, emerging markets)
            
            **Updates:** Recalculated daily with new market data
            """)
    
    with col2:
        with st.expander("🤖 **AI Sentiment Analysis**"):
            st.markdown("""
            **Snowflake Cortex AI processes:**
            - **Research documents** (earnings reports, analyst notes)
            - **News sentiment** (positive/negative media coverage)
            - **Technical indicators** (price trends, volume)
            - **Economic factors** (rates, inflation, GDP)
            
            **AI Processing Steps:**
            1. **AI_COMPLETE:** Summarizes research documents
            2. **AI_CLASSIFY:** Categorizes market outlook
            3. **AI_AGG:** Aggregates portfolio-level insights
            4. **Real-time updates** as new data arrives
            
            **Confidence levels** indicated by color intensity
            """)
    
    with col3:
        with st.expander("📊 **Performance Metrics**"):
            st.markdown("""
            **YTD Returns:**
            - Actual portfolio performance year-to-date
            - Calculated from real trading data
            - Compared to relevant benchmarks
            
            **Sharpe Ratio:**
            - Risk-adjusted returns (higher = better)
            - Formula: (Return - Risk-free rate) / Volatility
            - Industry standard for performance evaluation
            
            **AI Scores:**
            - Machine learning models trained on historical data
            - Continuously updated with market patterns
            - Validated against professional analyst opinions
            """)
    
    # Action Guide
    st.subheader("🎯 What Should You Do With This Information?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.expander("👨‍💼 **For Portfolio Managers**"):
            st.markdown("""
            **Daily Actions:**
            1. **Check red alerts first** - Address high-risk situations
            2. **Review bearish (red) sectors** - Consider rebalancing
            3. **Monitor high-risk portfolios** - Ensure client alignment
            4. **Act on AI recommendations** - Use as investment input
            
            **Weekly Reviews:**
            - Compare AI sentiment vs. your analysis
            - Identify sectors with changing outlooks
            - Adjust position sizes based on risk scores
            - Document rationale for decisions
            """)
    
    with col2:
        with st.expander("👔 **For Executives**"):
            st.markdown("""
            **Strategic Oversight:**
            1. **Track Total AUM growth** - Monitor business performance
            2. **Review high performer %** - Assess team effectiveness
            3. **Watch AI sentiment trends** - Understand market positioning
            4. **Use for client reporting** - Professional presentations
            
            **Key Metrics to Watch:**
            - Consistent positive AI sentiment across portfolios
            - Balanced risk distribution
            - Strong Sharpe ratios relative to benchmarks
            """)
    
    with col3:
        with st.expander("🛡️ **For Risk Management**"):
            st.markdown("""
            **Risk Controls:**
            1. **Set risk threshold alerts** - Use sidebar filters
            2. **Monitor sector concentration** - Avoid over-exposure
            3. **Track correlation patterns** - Identify clustering
            4. **Validate AI assessments** - Against internal models
            
            **Alert Thresholds:**
            - Risk scores > 8: Require senior approval
            - Sector allocation > 30%: Flag for review
            - Negative AI sentiment: Investigate immediately
            """)
    
    # Interactive Features Guide
    st.subheader("🔧 Interactive Features Guide")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("🎛️ **Sidebar Controls**"):
            st.markdown("""
            **Dashboard Controls:**
            - **🔄 Refresh Data:** Updates with latest information
            - **📅 Time Range:** Filter by different periods
            - **⚠️ Risk Threshold:** Show portfolios below risk level
            - **💰 Min Portfolio Value:** Filter out smaller portfolios
            
            **Navigation:**
            - **🏦 Dashboard:** Main analytics view
            - **📖 Dashboard Guide:** This help section
            
            **Pro Tips:**
            - Use risk threshold for client-specific views
            - Adjust time range for trend analysis
            - Combine filters for targeted insights
            """)
    
    with col2:
        with st.expander("📱 **Chart Interactions**"):
            st.markdown("""
            **Available Actions:**
            - **Hover:** See detailed information
            - **Click legend:** Hide/show data series
            - **Zoom:** Mouse wheel or drag selection
            - **Pan:** Click and drag to move view
            - **Reset:** Double-click to return to original view
            
            **Keyboard Shortcuts:**
            - **Space + drag:** Pan chart
            - **Shift + drag:** Box zoom
            - **Double-click:** Reset zoom
            
            **Export Options:**
            - Download charts as PNG
            - Save data tables as CSV
            """)
    
    # Pro Tips Section
    st.subheader("💡 Pro Tips for Maximum Effectiveness")
    
    tips = [
        "**Start with the metrics bar** - Get the overall picture before diving into details",
        "**Use the risk slider strategically** - Filter to match specific client risk profiles",
        "**Pay attention to color patterns** - Quick visual assessment of AI sentiment trends",
        "**Read AI document summaries** - Often contain the most actionable insights",
        "**Check alerts regularly** - Important changes are highlighted in real-time",
        "**Compare similar portfolios** - Look for patterns in the risk vs. performance chart",
        "**Hover over everything** - Most elements provide additional context on mouseover",
        "**Use time range filters** - Compare performance across different market periods"
    ]
    
    for tip in tips:
        st.write(f"• {tip}")
    
    # Footer
    st.markdown("---")
    st.success("""
    🎉 **Congratulations!** You're now ready to use the Asset Management Intelligence Dashboard effectively. 
    
    This AI-powered platform transforms hours of manual analysis into seconds of insight, helping you make better investment decisions faster.
    
    **Need more help?** Switch back to the 🏦 Dashboard and start exploring with your new knowledge!
    """)

# Technical Information in Sidebar
if __name__ == "__main__":
    st.sidebar.markdown("---")
    st.sidebar.markdown("**🔧 Technical Details**")
    st.sidebar.markdown(f"Data last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.sidebar.markdown("Connected to: Demo Dataset")
    st.sidebar.markdown("Refresh rate: Real-time")
    st.sidebar.markdown("**AI Models:** Snowflake Cortex")
