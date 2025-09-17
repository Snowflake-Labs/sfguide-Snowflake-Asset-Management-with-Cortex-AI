# 🏔️ Snowflake Asset Management AI Demo

🎯 **Objective**: Build a comprehensive AI-powered asset management system that combines document search, portfolio analytics, and intelligent assistance capabilities.

This demo provides detailed step-by-step instructions for setting up a sophisticated Asset Management AI demo in Snowflake, featuring:

- 🔍 **Cortex Search** - Intelligent document search and retrieval
- 📊 **Cortex Analyst** - Advanced portfolio data analysis
- 🖥️ **Streamlit Integration** - Interactive web application
- 🤖 **Snowflake Intelligence** - AI agent with advanced portfolio analysis and document search

## 🚀 What You'll Build

By the end of this setup, you'll have a fully functional AI system that can:

✅ Search through research documents using natural language  
✅ Analyze portfolio data with conversational queries  
✅ Provide intelligent recommendations combining both data sources  
✅ Deliver insights through an intuitive web interface  

## 📋 Repository Structure

```
├── README.md                             # This comprehensive guide
├── LEGAL.md                              # Legal notices
├── LICENSE                               # License information
├── notebooks/                            # Snowflake Notebooks
│   ├── environment.yml                   # Python package dependencies
│   └── 0_start_here.ipynb                # Main setup notebook for Cortex Search
├── scripts/                              # SQL and configuration files
│   ├── setup.sql                         # Database and schema setup script
│   └── semantic_models/                  # Sample semantic models for Cortex Analyst
│       └── PORTFOLIO_ANALYSIS.yaml       # yaml model for Cortex Analyst
│   └── generated_pdfs/                   # Sample research documents
│       └── *.pdf                         # PDF research documents for demo
└── streamlit/                            # Streamlit application
    ├── app.py                            # Streamlit dashboard code
```

## 📋 Prerequisites

### 🔑 Required Access & Permissions

☑️ Snowflake account with appropriate privileges  
☑️ SQL execution permissions  
☑️ Ability to create databases, schemas, and stages  
☑️ Access to Snowflake Notebooks  
☑️ Access to Snowflake Intelligence features  
☑️ [Cross Region Cortex Inference enabled](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference) (if required for your region)  

### 📁 Required Demo Files

Ensure you have all the following files ready:

| File Type | Description | Location | Usage |
|-----------|-------------|----------|-------|
| 📄 SQL setup script | Database and schema creation | `scripts/setup.sql` | Step 1 |
| 📚 PDF documents | Sample research documents (download first) | `scripts/generated_pdfs/` folder | Step 2 & 3 |
| 📓 Jupyter notebook | Cortex Search setup and processing (download first) | `notebooks/0_start_here.ipynb` | Step 2 & 4 |
| 📊 Cortex Analyst | Portfolio analysis semantic model | `scripts/PORTFOLIO_ANALYSIS.yaml` | Step 5 |
| 🤖 Snowflake Intelligence | AI agent configuration and testing | Step 6 | Step 6 |
| 🖥️ Streamlit app | Interactive dashboard code | `streamlit/app.py` | Step 7 |


---

## 🏗️ Setup Instructions

### 1️⃣ Step 1: Execute SQL Setup Statements

#### 1.1 Access Snowsight and Open Worksheets
1. Open **Snowflake** in your web browser (Snowsight interface)
2. Navigate to **Projects → Worksheets** in the left sidebar
3. Click **+ Worksheet** to create a new SQL worksheet

#### 1.2 Import and Execute the Setup Script
1. Locate the `scripts/setup.sql` file from this repository
2. Open the file and copy all contents
3. Paste the SQL statements into your new Snowflake worksheet
4. **Important**: The script uses `accountadmin` role for initial setup
5. Execute all statements by clicking **▶ Run All** or pressing `Ctrl+Shift+Enter`

#### 1.3 What the Setup Script Creates
The enhanced `setup.sql` script will automatically create:

**Security & Access:**
- **Role**: `asset_management_ai_role` with Cortex and Streamlit capabilities
- **Warehouse**: `asset_management_ai_wh` (Small, auto-suspend after 60 seconds)
- **Grants**: Comprehensive permissions for AI services and data access

**Data Infrastructure:**
- **Database**: `ASSET_MANAGEMENT_AI` 
- **Schema**: `RESEARCH_ANALYTICS`
- **Stage**: `RESEARCH_DOCS` internal stage (with encryption enabled)
- **Table**: `PORTFOLIO_HOLDINGS` with sample portfolio data
- **Sample Data**: 13 portfolio holdings across Technology, Healthcare, ESG, Real Estate, and Utilities sectors

**Snowflake Intelligence Setup:**
- **Database**: `snowflake_intelligence` for AI agent storage
- **Schema**: `snowflake_intelligence.agents` for agent management
- **Permissions**: CREATE AGENT privileges for the demo role


**Note**: If you continue with `accountadmin`, that's fine too - the setup script grants all necessary permissions to both roles.

---

### 2️⃣ Step 2: Download Demo Files

#### 2.1 Download the Notebook
1. Navigate to the `notebooks/` folder in this repository
2. **Download the notebook file**: `0_start_here.ipynb`
   - Click on the file in GitHub
   - Click the **Download** button
   - **Alternative**: Clone the entire repository to get all files locally
3. **Note the location** where you saved the notebook file for Step 4

#### 2.2 Download Research Documents  
1. Navigate to the `scripts/generated_pdfs/` folder in this repository
2. **Download all PDF files** individually or clone the repository to get them locally
3. Ensure you have all 8 research documents downloaded:
   - NovaTech Insights - Technology Sector Overview.pdf
   - NovaTech Insights - Emerging Markets.pdf
   - NovaTech Insights - ESG Trends.pdf
   - Gaming Industry Trends in 2025.pdf
   - FinTech Innovation Investment Opportunities.pdf
   - Dissertation on the Utility Sector.pdf
   - Stellar Motors Inc. - 10-K Annual Report.pdf
   - SNOW_2025.pdf

---

### 3️⃣ Step 3: Upload Research Documents

#### 3.1 Locate Your Downloaded Research Documents
1. **Find the downloaded PDF files** from Step 2.2 on your local machine
2. These documents are specifically chosen to match the portfolio holdings created in Step 1
3. **Document types include**:
   - **Technology Sector Analysis**: NovaTech Insights - Technology Sector Overview.pdf
   - **Emerging Markets Research**: NovaTech Insights - Emerging Markets.pdf
   - **ESG/Sustainability Analysis**: NovaTech Insights - ESG Trends.pdf
   - **Gaming Industry Trends**: Gaming Industry Trends in 2025.pdf
   - **FinTech Investment Research**: FinTech Innovation Investment Opportunities.pdf
   - **Utility Sector Analysis**: Dissertation on the Utility Sector.pdf
   - **Company Annual Report**: Stellar Motors Inc. - 10-K Annual Report.pdf
   - **Market Analysis**: SNOW_2025.pdf

#### 3.2 Upload Documents via Snowsight Data Interface

**Method A: Snowsight Web Interface (Recommended)**
1. In Snowsight, navigate to **Data → Databases**
2. Expand **ASSET_MANAGEMENT_AI** → **RESEARCH_ANALYTICS**
3. Click on **Stages** and select the `RESEARCH_DOCS` stage
4. Click **+ Files** button to open the upload dialog
5. **Select all 8 downloaded PDF files** from your local machine:
   - Browse to where you saved the files from Step 2.2
   - You can drag and drop multiple files at once
   - Or use Ctrl+Click (Windows) / Cmd+Click (Mac) to select multiple files
6. Click **Upload** to transfer all documents to the stage
7. Wait for the upload progress to complete

**Method B: SQL Commands (Alternative)**
If you prefer using SQL commands, you can upload via PUT statements:
```sql
-- Ensure you're in the correct context
USE DATABASE ASSET_MANAGEMENT_AI;
USE SCHEMA RESEARCH_ANALYTICS;

-- Upload files (replace with actual local file paths where you downloaded them)
PUT file:///path/to/your/downloads/NovaTech_Insights_Technology_Sector_Overview.pdf @RESEARCH_DOCS;
PUT file:///path/to/your/downloads/Gaming_Industry_Trends_in_2025.pdf @RESEARCH_DOCS;
PUT file:///path/to/your/downloads/Stellar_Motors_Inc_10K_Annual_Report.pdf @RESEARCH_DOCS;
-- Repeat for each of the 8 downloaded PDF files
```

### 4️⃣ Step 4: Load Notebook and Create Cortex Search Service

#### 4.1 Access Snowflake Notebooks in Snowsight
1. In Snowsight, navigate to **Projects → Notebooks** in the left sidebar
2. Click **+ Notebook** to create a new notebook
3. Choose **Import .ipynb file** option

#### 4.2 Import the Downloaded Notebook
1. Click **Browse** and select the `0_start_here.ipynb` file you downloaded in Step 2.1
2. **Configure the notebook environment**:
   - **Database**: `ASSET_MANAGEMENT_AI`
   - **Schema**: `RESEARCH_ANALYTICS`
   - **Warehouse**: `asset_management_ai_wh` (created in Step 1) or any S/M size warehouse
3. Click **Create Notebook**

#### 4.3 Understanding the Notebook Structure
The `0_start_here.ipynb` notebook contains:
- **Executive Summary**: Overview of the AI research pipeline transformation
- **Solution Architecture**: Detailed explanation of the 5-component system
- **Document Processing Pipeline**: Code for processing PDF research documents
- **Cortex Search Setup**: Instructions for creating the `INVESTMENT_SEARCH_SVC` service
- **Interactive Examples**: Sample queries and search demonstrations

#### 4.4 Execute Notebook with Uploaded Documents
1. Now that documents are uploaded from Step 3, proceed with document processing
2. **Execute cells sequentially** from top to bottom, following the notebook's guidance
3. The notebook will establish database connections and process the uploaded documents

#### 4.5 Document Processing Workflow
The notebook will guide you through:
1. **Document Parsing**: Extract text content from the uploaded PDFs
2. **Text Chunking**: Break documents into optimal-sized segments for search
3. **Embedding Generation**: Create vector embeddings using Snowflake Cortex
4. **Metadata Extraction**: Add relevant tags and classifications
5. **Search Service Creation**: Deploy the `INVESTMENT_SEARCH_SVC` Cortex Search service

#### 4.6 Add More Documents (Optional)
If you have additional research documents to add later:
1. Upload them to the `RESEARCH_DOCS` stage using the same methods from Step 3.2
2. Re-run the document processing cells in the notebook to include new documents
3. The search service will automatically include the new content

---

### 5️⃣ Step 5: Configure Cortex Analyst

#### 5.1 Access Cortex Analyst
1. Navigate to **AI & ML → Cortex Analyst** in Snowsight

#### 5.2 Upload Configuration File
1. From the **Create new** dropdown, select **Upload YAML file**
2. Download the `scripts/PORTFOLIO_ANALYSIS.yaml` file from this repository
3. Upload the YAML document from this repo

#### 5.3 Configure Stage and Path
1. Select the stage we created earlier: `RESEARCH_DOCS`
2. Add the path as: `semantic_models`
3. Click **Upload**

#### 5.4 Save Semantic Model
1. Review the configuration to ensure it correctly references your database and schema
2. Click **Save** to save the new Cortex Analyst semantic model
3. **Note the semantic model name** for the next step (typically named after your YAML file)

---

## 6️⃣ Step 6: Create and Test Snowflake Intelligence Agent

#### 6.1 Access Snowflake Intelligence
1. Navigate to **AI & ML → Snowflake Intelligence** in Snowsight
2. Click **+ Agent** to create a new agent

#### 6.2 Configure Agent Basic Settings
Configure your agent with these details:
- **Platform Integration**: Check Create this agent for Snowflake Intelligence
- **Agent Name**: `Research_Assistant`
- **Display Name**: `Research Assistant`
- **Click Create**
- **Click Edit** and navigate to Instructions
- **Instructions**: Copy and paste this instruction set:
```
You are an expert investment research assistant for Global Asset Management. You have access to:

1. A comprehensive research document library via Cortex Search containing reports on technology, healthcare, ESG, and real estate sectors
2. Portfolio data for analyzing current holdings and performance

Your role is to:
- Answer questions about investment research and market analysis
- Provide insights on portfolio holdings and sector performance
- Search through research documents to find relevant information
- Analyze portfolio data to support investment decisions
- Combine document insights with portfolio data for comprehensive analysis

Always provide data-driven responses and cite relevant sources when possible.
```

#### 6.3 Add Cortex Search Tool
1. Navigate to **Tools**
2. Click **+ Add Tool**
3. Select **Cortex Search**
4. **Name**: `Document_search`
5. **Tool Description**: `Search through investment research documents and reports`
6. Choose the `INVESTMENT_SEARCH_SVC` service created in Step 4
7. Click **Add**

#### 6.4 Add Cortex Analyst Tool
1. From **Tools**, click **+ Add Tool** again
2. Select **Cortex Analyst**
3. **Select semantic model file**: Choose the file we uploaded when creating Cortex Analyst
4. **Select database/schema/stage**: Choose `ASSET_MANAGEMENT_AI` → `RESEARCH_ANALYTICS` → `RESEARCH_DOCS` and select the file we uploaded
5. Add the following details:
   - **Name**: `Portfolio_analysis`
   - **Description**: `Analyze portfolio data and generate insights` or generate via Cortex
   - **Timeout**: 60 seconds
6. Click **Add**

#### 6.5 Finalize and Test Agent
1. Review all settings and tools
2. Ensure both Cortex Search and Cortex Analyst tools are properly configured and click **Save**
3. **Two ways to interact with your agent**:
   - **Option A**: Test directly from the agent configuration screen (chat interface at bottom)
   - **Option B**: Navigate to **Snowsight → AI → Snowflake Intelligence** and select your agent
4. **Test immediately** with these sample queries:

**📊 Portfolio Analysis Queries (using Cortex Analyst):**
- "What are our current portfolio holdings by sector?"
- "Which holdings have the highest risk levels?"
- "Chart our portfolio holdings by sector and risk"
- "Summarize our investment portfolio and outline the risk associated with each"

**🔍 Document Research Queries (using Cortex Search):**
- "What are the key technology trends mentioned in our research documents?"
- "Find information about ESG investment opportunities in our research library"
- "Compare the technology sector insights from our different research reports"

**💡 Strategic Portfolio Insights (combining both tools):**
- "What are the primary growth catalysts mentioned for our Technology holdings?"
- "What ESG trends are likely to impact our portfolio?"
- "Provide a summary of our Technology Sector Overview report and how it will impact our portfolio"

#### 6.6 Demo Capabilities and Access Options
1. **Try portfolio analysis queries** to see how the agent analyzes your portfolio data
2. **Test document search** to see how the agent searches through your uploaded research documents
3. **Combine both capabilities** by asking questions that require both portfolio data and document insights
4. **Note the comprehensive responses** with relevant citations from both data sources

**Access Your Agent:**
- **In Configuration Screen**: Use the chat interface at the bottom of the agent configuration screen
- **Snowflake Intelligence Portal**: Navigate to **Snowsight → AI → Snowflake Intelligence** and select your "Research Assistant" agent
- **Better Experience**: The Snowflake Intelligence portal provides a full-screen chat interface optimized for longer conversations

**Your agent can now:**
- **Analyze portfolio data** using natural language queries (Cortex Analyst)
- **Search through research documents** using semantic search (Cortex Search)
- **Generate insights** by combining portfolio data with document research
- **Provide intelligent recommendations** based on both data sources
- **Create visualizations** and charts for portfolio analysis
- **Extract specific information** from your research library and portfolio data

---

### 7️⃣ Step 7: Create Streamlit Application

#### 7.1 Prepare the Streamlit Application Code
1. Locate the `streamlit/app.py` file from this repository
2. Open the file and copy all the Python code contents
3. This file contains the complete interactive dashboard for portfolio analytics and document search

#### 7.2 Create New Streamlit App
1. In Snowsight, navigate to **Streamlit** in the left sidebar
2. Click **+ Streamlit App**
3. Configure the app:
   - **Name**: `GAM Research Assistant App` (or similar)
   - **Database**: `ASSET_MANAGEMENT_AI`
   - **Schema**: `RESEARCH_ANALYTICS`
   - **Warehouse**: `asset_management_ai_wh` (or same as used for notebook)

#### 7.3 Deploy Streamlit Code
1. Delete any default code in the Streamlit editor
2. Paste the copied Python code from `app.py`
3. Add `plotly` from the packages dropdown
4. Click **Run** to deploy the app

---

## 🎯 Demo Story: Asset Management AI Transformation

This demonstration showcases how Global Asset Management (GAM) revolutionized their investment research and portfolio management processes using Snowflake's integrated AI platform.

### 📊 The Challenge
GAM's analysts were spending **30-40% of their time** organizing and finding documents instead of analyzing investments:
- **Manual classification** of research reports and SEC filings
- **Keyword-based searches** missing critical insights
- **Siloed data** across different systems preventing comprehensive analysis
- **Hours to answer** urgent research questions during volatile market conditions

### 🚀 The Transformation
GAM deployed a comprehensive AI research platform that delivers:
- **⚡ 30-second insights** instead of hours of manual research
- **🎯 Semantic understanding** of investment concepts and relationships
- **📊 Real-time portfolio analysis** with AI-driven risk assessment
- **🤖 Conversational research assistant** for instant answers

### 💡 Why Snowflake Makes This Possible
- **🚀 Integrated AI Stack**: LLMs, embeddings, and vector search natively within the data warehouse
- **⚡ No Infrastructure Management**: Automatic scaling without GPU cluster management
- **💰 Elastic Economics**: Pay only for actual compute usage
- **🔒 Enterprise Security**: SOC 2 compliance and encryption built-in
- **📊 Data Gravity**: Research documents and portfolio data in the same platform

### 📈 Business Impact
- **90% reduction** in research organization time
- **Instant access** to insights across thousands of documents
- **Real-time analysis** enabling rapid response to market changes
- **Zero infrastructure management** reducing IT overhead

---

## 🆘 Support

- 💬 [Snowflake Community](https://community.snowflake.com/)
- 📖 [Snowflake Documentation](https://docs.snowflake.com/)
- 🤖 [Cortex AI Documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex)
- 🔍 [Cortex Search Documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search)
- 🧠 [Snowflake Intelligence Documentation](https://docs.snowflake.com/en/user-guide/snowflake-intelligence)

