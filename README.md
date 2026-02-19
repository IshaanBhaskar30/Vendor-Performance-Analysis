# 📊 Vendor Performance Analysis
## 🔍 Project Overview

End-to-end data analytics project focused on evaluating vendor performance, profitability drivers, inventory efficiency, and supplier concentration risk in a retail/wholesale business environment.

This project demonstrates the full analytics lifecycle — from data ingestion and transformation to statistical modeling and business recommendations.

### 🛠 Tech Stack

Python | Pandas | NumPy | SQL (SQLite) | Matplotlib | Seaborn | SciPy | Statsmodels

## ⚙️ Project Workflow
### 1️⃣ Data Engineering

    - Built automated ingestion pipeline to load multiple CSV files into SQLite using SQLAlchemy.

    - Merged structured tables into a unified analytical dataset.

    - Cleaned and filtered anomalies (negative margins, zero sales, extreme outliers).

### 2️⃣ Exploratory Data Analysis

    - Performed distribution, correlation, and outlier analysis.

    - Identified pricing inefficiencies and inventory anomalies.

### 3️⃣ Advanced Analysis

    - Pareto Analysis (80/20 Rule) → 17 vendors generate ~80% of total profit.

    - Vendor Dependency Risk → Top 10 vendors account for ~65% of sales.

    - Profitability Segmentation → Identified high-margin vs high-volume vendors.

    - Inventory Efficiency → Detected ~$2.7M tied in slow-moving inventory (Turnover & DIO analysis).

    - Bulk Purchasing Impact → Large-volume orders reduce unit cost by ~72%.

    - Statistical Testing → ANOVA & Kruskal-Wallis confirm significant profitability differences across vendor groups.

### 📈 Key Insights

    - Revenue is highly concentrated among a small group of vendors → operational risk.

    - High-volume vendors are not always the most profitable.

    - Mid-tier vendors provide stronger margin expansion opportunities.

    - Inventory inefficiencies directly impact working capital.

### 🎯 Business Impact

    - Proposed vendor diversification strategy to reduce concentration risk.

    - Recommended renegotiation for low-margin, high-volume vendors.

    - Identified pricing & promotional opportunities for high-margin, low-sales brands.

    - Delivered data-backed recommendations for improving profitability and cash flow efficiency.

### 🚀 What This Project Demonstrates

    - End-to-end analytics pipeline development
    
    - SQL + Python integration
    
    - Statistical validation of business hypotheses
    
    - Data-driven decision-making
    
    - Ability to translate analytics into executive recommendations
