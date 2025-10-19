
/*--
Asset Management AI: Intelligent Research Platform - Setup Script
This script creates all necessary objects for the Asset Management AI demo
including roles, warehouses, databases, schemas, and proper security grants
--*/

USE ROLE accountadmin;

-- assign Query Tag to Session. This helps with performance monitoring and troubleshooting
ALTER SESSION SET query_tag = '{"origin":"sf_sit-is","name":"asset_management_ai:_intelligent_research_platform","version":{"major":1,"minor":0},"attributes":{"is_quickstart":1,"source":"sql"}}';

-- Create custom role for Asset Management AI demo
CREATE OR REPLACE ROLE asset_management_ai_role
    COMMENT = 'Role for Asset Management AI demo with Cortex Search, Cortex Analyst, and Streamlit capabilities';

-- Create warehouse for Asset Management AI demo
CREATE OR REPLACE WAREHOUSE asset_management_ai_wh
    WAREHOUSE_SIZE = 'small'
    WAREHOUSE_TYPE = 'standard'
    AUTO_SUSPEND = 60
    AUTO_RESUME = TRUE
    INITIALLY_SUSPENDED = TRUE
    COMMENT = 'Warehouse for Asset Management AI research analytics and document processing';

-- Grant warehouse usage to custom role
GRANT USAGE ON WAREHOUSE asset_management_ai_wh TO ROLE asset_management_ai_role;
GRANT OPERATE ON WAREHOUSE asset_management_ai_wh TO ROLE asset_management_ai_role;

USE WAREHOUSE asset_management_ai_wh;

-- Create database and schemas
CREATE DATABASE IF NOT EXISTS ASSET_MANAGEMENT_AI;
CREATE OR REPLACE SCHEMA ASSET_MANAGEMENT_AI.RESEARCH_ANALYTICS;

-- Grant database and schema access to custom role
GRANT USAGE ON DATABASE ASSET_MANAGEMENT_AI TO ROLE asset_management_ai_role;
GRANT USAGE ON SCHEMA ASSET_MANAGEMENT_AI.public TO ROLE asset_management_ai_role;
GRANT USAGE ON SCHEMA ASSET_MANAGEMENT_AI.RESEARCH_ANALYTICS TO ROLE asset_management_ai_role;

-- Grant create privileges on schemas for AI services
GRANT CREATE TABLE ON SCHEMA ASSET_MANAGEMENT_AI.public TO ROLE asset_management_ai_role;
GRANT CREATE VIEW ON SCHEMA ASSET_MANAGEMENT_AI.public TO ROLE asset_management_ai_role;
GRANT CREATE STAGE ON SCHEMA ASSET_MANAGEMENT_AI.public TO ROLE asset_management_ai_role;
GRANT CREATE FILE FORMAT ON SCHEMA ASSET_MANAGEMENT_AI.public TO ROLE asset_management_ai_role;
GRANT CREATE FUNCTION ON SCHEMA ASSET_MANAGEMENT_AI.public TO ROLE asset_management_ai_role;
GRANT CREATE CORTEX SEARCH SERVICE ON SCHEMA ASSET_MANAGEMENT_AI.public TO ROLE asset_management_ai_role;
GRANT CREATE TABLE ON SCHEMA ASSET_MANAGEMENT_AI.RESEARCH_ANALYTICS TO ROLE asset_management_ai_role;
GRANT CREATE VIEW ON SCHEMA ASSET_MANAGEMENT_AI.RESEARCH_ANALYTICS TO ROLE asset_management_ai_role;
GRANT CREATE STAGE ON SCHEMA ASSET_MANAGEMENT_AI.RESEARCH_ANALYTICS TO ROLE asset_management_ai_role;
GRANT CREATE FILE FORMAT ON SCHEMA ASSET_MANAGEMENT_AI.RESEARCH_ANALYTICS TO ROLE asset_management_ai_role;
GRANT CREATE FUNCTION ON SCHEMA ASSET_MANAGEMENT_AI.RESEARCH_ANALYTICS TO ROLE asset_management_ai_role;
GRANT CREATE CORTEX SEARCH SERVICE ON SCHEMA ASSET_MANAGEMENT_AI.RESEARCH_ANALYTICS TO ROLE asset_management_ai_role;
GRANT CREATE STREAMLIT ON SCHEMA ASSET_MANAGEMENT_AI.RESEARCH_ANALYTICS TO ROLE asset_management_ai_role;

-- Grant CORTEX_USER role for Cortex functions access (Search, Analyst, LLM functions)
GRANT DATABASE ROLE SNOWFLAKE.CORTEX_USER TO ROLE asset_management_ai_role;

-- Role hierarchy - grant custom role to sysadmin
GRANT ROLE asset_management_ai_role TO ROLE sysadmin;

USE DATABASE ASSET_MANAGEMENT_AI;
USE SCHEMA RESEARCH_ANALYTICS;

-- Create stage for research documents
CREATE OR REPLACE STAGE RESEARCH_DOCS
    DIRECTORY = (ENABLE = TRUE)
    ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE')
    COMMENT = 'Internal stage for research documents repository - PDFs, reports, and analysis files';

-- Grant stage access to custom role
GRANT READ ON STAGE RESEARCH_DOCS TO ROLE asset_management_ai_role;
GRANT WRITE ON STAGE RESEARCH_DOCS TO ROLE asset_management_ai_role;

-- List stage contents (initially empty)
LIST @RESEARCH_DOCS;

-- Create portfolio holdings table - this is the production table
CREATE OR REPLACE TABLE PORTFOLIO_HOLDINGS (
    HOLDING_ID VARCHAR(10),
    PORTFOLIO_NAME VARCHAR(50),
    SECURITY_NAME VARCHAR(100),
    SECTOR VARCHAR(50),
    MARKET_VALUE NUMBER(15,2),
    WEIGHT_PERCENT NUMBER(5,2),
    RISK_LEVEL VARCHAR(20),
    LAST_UPDATED DATE
);

-- Insert sample portfolio data aligned with the research documents (ie technology/health/esg/real estate/utilities sectors)
INSERT INTO PORTFOLIO_HOLDINGS VALUES
('H001', 'Growth Fund Alpha', 'Microsoft Corporation', 'Technology', 2500000.00, 16.29, 'Medium', '2024-02-15'),
('H002', 'Growth Fund Alpha', 'NVIDIA Corporation', 'Technology', 2200000.00, 14.33, 'High', '2024-02-15'),
('H003', 'Growth Fund Alpha', 'Johnson & Johnson', 'Healthcare', 1800000.00, 11.73, 'Low', '2024-02-15'),
('H004', 'Growth Fund Alpha', 'Pfizer Inc', 'Healthcare', 1500000.00, 9.77, 'Medium', '2024-02-15'),
('H005', 'ESG Impact Fund', 'Tesla Inc', 'Technology', 1200000.00, 7.82, 'High', '2024-02-15'),
('H006', 'ESG Impact Fund', 'Vestas Wind Systems', 'ESG/Renewable', 800000.00, 5.21, 'Medium', '2024-02-15'),
('H007', 'ESG Impact Fund', 'Unilever PLC', 'Consumer Goods', 600000.00, 3.91, 'Low', '2024-02-15'),
('H008', 'Emerging Markets Fund', 'Taiwan Semiconductor', 'Technology', 1000000.00, 6.51, 'High', '2024-02-15'),
('H009', 'Emerging Markets Fund', 'Tencent Holdings', 'Technology', 900000.00, 5.86, 'High', '2024-02-15'),
('H010', 'Real Estate Fund', 'American Tower Corp', 'Real Estate', 750000.00, 4.89, 'Medium', '2024-02-15'),
('H011', 'Real Estate Fund', 'Prologis Inc', 'Real Estate', 650000.00, 4.23, 'Medium', '2024-02-15'),
('H012', 'Conservative Income', 'Vanguard REIT ETF', 'Real Estate', 500000.00, 3.26, 'Low', '2024-02-15'),
('H013', 'Utilities Income Fund', 'NextEra Energy Inc', 'Utilities', 950000.00, 6.19, 'Low', '2024-02-15');

-- Grant SELECT privileges on all tables for Cortex Analyst semantic models
GRANT SELECT ON ALL TABLES IN SCHEMA ASSET_MANAGEMENT_AI.public TO ROLE asset_management_ai_role;
GRANT SELECT ON ALL TABLES IN SCHEMA ASSET_MANAGEMENT_AI.RESEARCH_ANALYTICS TO ROLE asset_management_ai_role;
GRANT SELECT ON FUTURE TABLES IN SCHEMA ASSET_MANAGEMENT_AI.public TO ROLE asset_management_ai_role;
GRANT SELECT ON FUTURE TABLES IN SCHEMA ASSET_MANAGEMENT_AI.RESEARCH_ANALYTICS TO ROLE asset_management_ai_role;

-- Grant SELECT privileges on all views for Cortex Analyst semantic models
GRANT SELECT ON ALL VIEWS IN SCHEMA ASSET_MANAGEMENT_AI.public TO ROLE asset_management_ai_role;
GRANT SELECT ON ALL VIEWS IN SCHEMA ASSET_MANAGEMENT_AI.RESEARCH_ANALYTICS TO ROLE asset_management_ai_role;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA ASSET_MANAGEMENT_AI.public TO ROLE asset_management_ai_role;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA ASSET_MANAGEMENT_AI.RESEARCH_ANALYTICS TO ROLE asset_management_ai_role;

-- Setup for Snowflake Intelligence agents
CREATE DATABASE IF NOT EXISTS snowflake_intelligence;
GRANT USAGE ON DATABASE snowflake_intelligence TO ROLE PUBLIC;
CREATE SCHEMA IF NOT EXISTS snowflake_intelligence.agents;
GRANT USAGE ON SCHEMA snowflake_intelligence.agents TO ROLE PUBLIC;
GRANT CREATE AGENT ON SCHEMA snowflake_intelligence.agents TO ROLE asset_management_ai_role;

-- Setup complete! Next steps:
-- 1. Upload research documents to @RESEARCH_DOCS stage
-- 2. Import and run the 0_start_here.ipynb notebook
-- 3. Create Streamlit application using streamlit/app.py
-- 4. Configure Cortex Analyst with PORTFOLIO_ANALYSIS.yaml
-- 5. Create Snowflake Intelligence agent

-- Verify setup
SELECT 'Setup completed successfully!' AS status;
SHOW ROLES LIKE 'asset_management_ai_role';
SHOW WAREHOUSES LIKE 'asset_management_ai_wh';
