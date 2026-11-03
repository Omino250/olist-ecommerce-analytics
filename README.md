# Olist E-Commerce Analytics Pipeline: End-to-End Operational & RFM Segmentation Engine

Production-grade data engineering, customer segmentation, and logistics analytics platform built on 100,000+ Brazilian e-commerce transactional records across 9 relational database tables.

---

## 1. Project Overview & Business Context

Olist operates as a major e-commerce marketplace integrator in Brazil, enabling small and medium-sized merchants to list and sell products across national retail channels. As Olist scales across Latin America, Customer Acquisition Cost (CAC) on external digital channels has escalated. Transactional logs reveal a systemic platform vulnerability: while thousands of first-time orders are processed monthly, over 96.9% of buyers purchase once and never return.

To maximize Customer Lifetime Value (CLV) and insulate market share from competing marketplaces, Olist requires a transition away from broad discount blasts toward an automated, data-driven analytical pipeline. This project establishes an enterprise analytical infrastructure designed to process 9 relational database tables—spanning customer geographic locations, transactional timestamps, payment mechanics, logistics fulfillment logs, and post-purchase review scores.

The primary objective of this project is to build a modular, production-ready pipeline that ingests raw transactional data, cleanses multi-table relational joins, performs Recency, Frequency, and Monetary (RFM) feature engineering, segments customers via unsupervised machine learning, diagnoses regional fulfillment bottlenecks, and serves executive insights through an interactive web application.

---

## 2. Problem Statement

The core operational, retention, and logistical challenges facing Olist are anchored in four primary operational breakdowns:

1. **Extreme Structural Churn**: Out of 95,559 unique customers analyzed, only 2,924 buyers ever place a second order, establishing a baseline platform repeat purchase rate of 3.00%. The marketplace functions primarily as a single-transaction acquisition funnel rather than a recurring commerce engine.
2. **The Retention Satisfaction Paradox**: Operational intuition often attributes churn to customer dissatisfaction. However, analysis of 91,946 single-purchase buyers demonstrates that 85.6% leave 3- to 5-star ratings with an average initial score of 4.10 out of 5.00. Customer dissatisfaction is not the primary catalyst for churn; Olist simply lacks an intentional repeat-purchase loop or automated post-purchase re-engagement mechanism.
3. **Severe Regional Fulfillment Bottlenecks**: Logistics transit times and shipping charges vary heavily across Brazil's geographic regions. Late deliveries destroy customer ratings, causing 1- and 2-star reviews to surge to 52.89% when orders arrive past the estimated delivery date. Localized breakdowns—such as Rio de Janeiro's 13.47% delivery delay rate and long-haul shipping routes to Northern states taking up to 29 days—create severe friction in regions generating substantial revenue.
4. **Unprotected High-Value Revenue**: Dormant High-Spenders make up 33.67% of the customer base (32,176 users) with an average order value of R$ 300.74. Sitting inactive for an average of 281 days, these high-basket buyers represent an unaddressed revenue leak.

---

## 3. Tech Stack & Architecture

The analytical engine is structured as a modular Python repository engineered to maintain strict separation of concerns between data extraction, schema cleaning, feature transformation, machine learning, and UI presentation.

### Technology Stack
* **Programming Language**: Python 3.12+
* **Data Processing & Analytics**: Pandas, NumPy
* **Machine Learning & Feature Scaling**: Scikit-Learn (`StandardScaler`, `KMeans`)
* **Database Management & ORM**: MySQL Server 8.0, SQLAlchemy 2.0+, `pymysql`
* **Configuration & Security**: `python-dotenv`
* **Dashboard & Application**: Streamlit

### Repository Directory Structure

```
olist-ecommerce-analytics/
├── data/
│   ├── raw/                        # Raw relational CSV tables (git-ignored)
│   └── processed/                  # Cleaned parquet/CSV snapshots and RFM features
├── notebooks/
│   ├── 01_eda_and_sql_ingestion.ipynb
│   ├── 02_rfm_scaling_kmeans.ipynb
│   └── 03_logistics_sentiment_deepdive.ipynb
├── src/
│   ├── __init__.py
│   ├── data_cleaning.py            # Preprocessing, schema checks, and SQL ETL scripts
│   ├── rfm_segmentation.py         # Log transformation, scaling, and K-Means clustering
│   └── metrics_engine.py           # Executive KPI logic and aggregation engine
├── docs/
│   ├── database_schema.md          # ERD entity relationships across 9 tables
│   └── operational_audit_report.md # Data quality and pipeline audit metrics
├── .env.example                    # Environment variable template for DB credentials
├── .gitignore                      # Git exclusion rules for raw data and secrets
├── requirements.txt                # Fixed Python dependencies
└── app.py                          # Streamlit executive dashboard application
```

---

## 4. Executive KPI Engine

The pipeline computes 10 core operational metrics to benchmark marketplace performance, track retention dynamics, and quantify regional logistics friction.

| Metric Identifier | Metric Name | Mathematical Definition / Formula | Baseline Value | Strategic Significance |
| :--- | :--- | :--- | :--- | :--- |
| **KPI 1** | Overall Repeat Purchase Rate | $\frac{\text{Unique Customers with }>1\text{ Order}}{\text{Total Unique Customers}} \times 100$ | **3.00%** | Highlights single-purchase acquisition dependency (2,924 repeat out of 95,559 total). |
| **KPI 2** | RFM Segment Distribution | Share of total customer base per cluster centroid | **63.27%** Lost, **33.67%** At-Risk, **3.06%** Champions | Maps customer concentration from dormant single-purchasers to loyal repeat buyers. |
| **KPI 3** | Average Order Value (AOV) by Segment | $\frac{\text{Total Gross Monetary Revenue}}{\text{Total Order Count per Cluster}}$ | Champions: **R$ 307.59**, At-Risk: **R$ 300.74**, Low-Value: **R$ 68.44** | Identifies basket size disparities across behavioral customer personas. |
| **KPI 4** | CLV Contribution by Segment | Total monetary spend generated per cluster | At-Risk High Spenders: **27.07%** total revenue | Isolates key revenue drivers; 11.41% top spenders generate over a quarter of platform revenue. |
| **KPI 5** | Logistics Freight Ratio | $\frac{\text{Freight Value}}{\text{Product Price} + \text{Freight Value}} \times 100$ | **20.94%** platform average | Shipping costs consume ~21 cents of every Real spent, escalating up to 32.68% in remote states. |
| **KPI 6** | On-Time Delivery Rate | $\frac{\text{Orders Delivered } \le \text{ Estimated Date}}{\text{Total Delivered Orders}} \times 100$ | National: **91.93%**, Rio de Janeiro: **86.53%** (**13.47%** Delay Rate) | National averages hide localized logistical breakdowns in high-revenue states like RJ. |
| **KPI 7** | Average Review Score by Cluster | $\frac{\text{Sum of Review Stars}}{\text{Total Submitted Reviews per Cluster}}$ | Baseline: **4.10 – 4.16 Stars** | Proves initial satisfaction is high across churned and retained buyers alike. |
| **KPI 8** | Frictional One-Timers | $\frac{\text{Single-Purchase Buyers with Delays or 1-2 Star Reviews}}{\text{Total Single-Purchase Buyers}} \times 100$ | **16.63%** | Quantifies first-time buyers whose initial interaction was impaired by service failure. |
| **KPI 9** | Geographic Concentration | State-by-state distribution of order volume & revenue | SP: **40,501 orders** (>40%), Southeast: **>65%** | Confirms high volume concentration in SP, RJ, and MG alongside uniform churn (5.53%–6.88%). |
| **KPI 10** | Preferred Payment Method Share | Breakdown of Credit Card, Boleto, Voucher, Debit per segment | Credit Card: **72.51%–79.03%**, Boleto: **17.17%–21.93%** | Credit cards dominate checkout; flexible installments drive higher basket sizes and repeat transactions. |

---

## 5. RFM Customer Segmentation & Findings

### Data Scaling & Feature Transformation Pipeline
Raw transactional metrics exhibit severe right-skewness. Across 95,559 customers, monetary spend ranges from R$ 0.85 to R$ 13,664.00 with a median of R$ 107.78, while order frequency sits at 1.00 for over 96.9% of records. Feeding unscaled monetary values directly into distance-based algorithms like K-Means causes monetary outliers to warp cluster centroids.

To resolve this imbalance, the preprocessing pipeline applies a sequential two-step feature transformation:
1. **Log Transformation**: $x_{\text{transformed}} = \ln(x + 1)$ via `np.log1p`, compressing exponential monetary and frequency distributions.
2. **Standardization**: Rescaling via `StandardScaler` to force features to a mean of $\mu = 0$ and standard deviation of $\sigma = 1$.

```python
# Feature scaling and clustering pipeline in src/rfm_segmentation.py
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def preprocess_and_cluster_rfm(rfm_df, n_clusters=4, random_state=42):
    """
    Log transforms, standardizes, and clusters RFM customer metrics.
    """
    # Step 1: Log transform heavily skewed RFM features
    rfm_log = np.log1p(rfm_df[['recency', 'frequency', 'monetary']])
    
    # Step 2: Standardize features to mean=0, std=1
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_log)
    
    # Step 3: Fit K-Means clustering model
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
    rfm_df['cluster'] = kmeans.fit_predict(rfm_scaled)
    
    return rfm_df, kmeans, scaler
```

### Optimal Cluster Selection ($k = 4$)
Evaluating inertia reductions across cluster counts $k \in [1, 8]$ reveals a clear mathematical elbow at $k = 4$. Moving from $k = 1$ to $k = 4$ yields substantial reductions in sum-of-squared distances, whereas $k = 5$ and $k = 6$ produce diminishing returns.

```
Inertia / Within-Cluster Sum of Squares (WCSS):
k=1 : 286,677.0  | --------------------------------------------------
k=2 : 182,340.5  | ----------------------------------
k=3 : 124,192.1  | --------------------
k=4 :  81,405.3  | ------------ [Elbow Point]
k=5 :  68,211.8  | ----------
k=6 :  57,940.2  | --------
```

### Customer Persona Cluster Profiles

| Cluster ID | Cluster Business Persona | Customer Count | Share of Total | Mean Recency (Days) | Mean Frequency | Mean Monetary (R$) | Behavioral Profile & Retention Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Cluster 0** | Dormant Low-Value Buyers | 42,581 | 44.56% | 298.4 | 1.00 | R$ 68.44 | Purchased low-ticket items nearly a year ago. Low engagement priority; avoid expensive retargeting. |
| **Cluster 1** | Dormant High-Spenders (At-Risk) | 32,176 | 33.67% | 281.2 | 1.00 | R$ 300.74 | High single-order spend (appliances/furniture). Prime target for high-priority CRM win-back campaigns. |
| **Cluster 2** | Champions / Loyal Repeat Buyers | 2,924 | 3.06% | 227.1 | 2.11 | R$ 307.59 | Captures 100% of platform repeat buyers. Requires VIP loyalty perks and early access promotions. |
| **Cluster 3** | Recent New Buyers | 17,878 | 18.71% | 51.3 | 1.00 | R$ 132.86 | Fresh acquisition cohort. Immediate target for 30-day onboarding automated email/SMS sequences. |

### Product Category Repeat Dynamics
Repeat purchasing varies significantly by category type:
* **High-Repeat Staples**: `home_appliances` records the highest repeat rate at **17.94%**, followed by `fashion_bags_accessories` (**12.31%**), `furniture_decor` (**9.26%**), and `bed_bath_table` (**9.24%**).
* **One-Off Purchase Traps**: Discretionary and tech categories experience severe single-purchase churn, led by `electronics` (**3.38%** repeat rate), `cool_stuff` (**3.51%**), `consoles_games` (**3.63%**), and `office_furniture` (**4.15%**).

---

## 6. Logistics & Regional Friction

Logistics performance across Brazil's 27 states confirms that delivery timelines and shipping burdens directly dictate customer sentiment and fulfillment efficiency.

### Geographic Distance & Freight Scaling
Distance between merchant origin and customer destination scales shipping costs and delivery timelines almost linearly:

* **Local Deliveries (<100 km)**: Average freight fee of **R$ 13.45**, transit time of **6.5 days**, repeat purchase rate of **6.34%**.
* **Regional Deliveries (100–1,000 km)**: Average freight fee of **R$ 21.10**, transit time of **11.8 days**, repeat purchase rate of **6.41%**.
* **Long-Haul Inter-State (>1,000 km)**: Average freight fee of **R$ 46.58**, transit time of **23.4 days**, repeat purchase rate drops to **5.13%**.

### Remote State Shipping Burdens
Customers in Brazil's Northern and Northeastern states endure severe shipping cost inflation and extended transit times:

* **Roraima (RR)**: Freight fees account for **32.68%** of total order value, with an average transit time of **29.39 days**.
* **Amazonas (AM)**: Freight fees account for **29.61%** of total order value, with an average transit time of **26.43 days**.
* **Maranhão (MA)**: Sellers originating in MA exhibit a seller-side delay rate of **23.14%** with an average fulfillment time of **17.73 days**.

### Specific Route Lags Originating from São Paulo (SP) Hub
São Paulo sellers generate 68,635 orders (over 70% of total seller origin volume). Long-haul routes to Northern and Northeastern destinations experience severe delays:
* **SP → Alagoas (AL)**: Average delivery duration of **25.00 days** with a **26.07%** late delivery rate.
* **SP → Pará (PA)**: Average delivery duration of **23.12 days** with a **21.45%** late delivery rate.
* **SP → Maranhão (MA)**: Average delivery duration of **22.84 days** with a **22.10%** late delivery rate.

### Operational Asymmetry: Delivery Delays vs. Customer Sentiment
Delivery timeline integrity is the single largest determinant of post-purchase review scores:

```
On-Time / Early Deliveries  [Avg Review: 4.29 / 5.00]
├── 5-Star Reviews: 68.4%
├── 3-4 Star Reviews: 22.4%
└── 1-2 Star Reviews:  9.18%

Late Deliveries (>0 Days Past Estimated Date) [Avg Review: 2.57 / 5.00]
├── 5-Star Reviews: 21.2%
├── 3-4 Star Reviews: 25.9%
└── 1-2 Star Reviews: 52.89%  <-- 5.7x Increase in Negative Sentiment
```

---

## 7. Interactive Streamlit Dashboard

Phase 8 implements an executive web application built with Streamlit (`app.py`), enabling business stakeholders to inspect KPIs, filter regional metrics, and trigger CRM workflows in real time.

```
                         ┌──────────────────────────────┐
                         │    MySQL Relational Database │
                         │       (9 SQL Tables)         │
                         └──────────────┬───────────────┘
                                        │ (SQLAlchemy Connection Pool)
                                        ▼
                         ┌──────────────────────────────┐
                         │   src/metrics_engine.py      │
                         │   src/rfm_segmentation.py    │
                         └──────────────┬───────────────┘
                                        │ (Pandas DataFrames / Models)
                                        ▼
                         ┌──────────────────────────────┐
                         │     Streamlit (app.py)       │
                         │  Executive KPI & Filtering   │
                         └──────────────────────────────┘
```

### Dashboard Core Capabilities
1. **Real-Time Executive KPI Banner**: Renders live platform summaries for Repeat Purchase Rate, Platform AOV, On-Time Delivery Rate, and High-Spender Revenue Share.
2. **Interactive Multi-Filter Panel**: Filters entire dashboard state dynamically by Customer State (e.g., SP, RJ, RR), Product Category (e.g., `bed_bath_table`, `health_beauty`), RFM Segment Cluster, and Payment Method.
3. **Logistics & Regional Friction Map**: Visualizes delay rate spikes by state, identifying high-risk routes (e.g., Rio de Janeiro at 13.47% delay) via interactive charts and state breakdown tables.
4. **RFM Segment Deep-Dive**: Displays cluster scatter plots (Recency vs. Monetary) along with revenue contribution distributions across segments.
5. **CRM Win-Back Trigger Generator**: Generates actionable customer lists for At-Risk High Spenders (Cluster 1) who have crossed 120+ days of inactivity, exportable directly to CSV for marketing automation platforms.

---

## 8. Challenges & Technical Solutions

Building a production-grade analytics pipeline over multi-gigabyte transactional logs presented four primary engineering hurdles.

### Challenge 1: Database Credential Security
* **Problem**: Hardcoding MySQL database connection strings (`mysql+pymysql://user:pass@localhost:3306/olist`) in pipeline scripts risks exposing credentials in version control.
* **Engineered Solution**: Implemented strict secret isolation using `python-dotenv`. All database connection parameters are loaded at runtime from a local `.env` file via an engine construction helper in `src/data_cleaning.py`.

```python
# Database credential management pattern in src/data_cleaning.py
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def get_db_engine():
    """
    Constructs a SQLAlchemy connection pool from environment variables.
    """
    db_user = os.getenv("DB_USER", "root")
    db_pass = os.getenv("DB_PASS", "")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "3306")
    db_name = os.getenv("DB_NAME", "olist")
    
    connection_url = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    return create_engine(connection_url, pool_pre_ping=True, pool_size=10)
```

### Challenge 2: Large Raw CSV Tracking & Git Repository Bloat
* **Problem**: Storing raw multi-million row CSV files directly inside Git repositories causes slow clone times, repository bloat, and exceeds GitHub file size limits.
* **Engineered Solution**: Enforced explicit `.gitignore` rules targeting raw dataset directories while maintaining `.gitkeep` structural markers. Included a lightweight schema initialization script (`docs/database_schema.md`) to allow automated database recreation.

```gitignore
# Exclude raw data files and local environment files
data/raw/*.csv
data/processed/*.parquet
.env
*.log
.DS_Store
__pycache__/
```

### Challenge 3: Extreme Monetary Skew Warping Clustering
* **Problem**: Raw monetary spend spans from R$ 0.85 to R$ 13,664. Feeding raw features into K-Means causes Euclidean distance calculations to be dominated by monetary magnitude, isolating a handful of high spenders while clumping 99% of users into a single uninformative cluster.
* **Engineered Solution**: Built a sequential feature transformation pipeline executing log compression `np.log1p` to normalize feature distributions followed by `StandardScaler` standardizing variables to $\mu = 0, \sigma = 1$.

### Challenge 4: Multi-Table Relational Schema Integrity
* **Problem**: Joining 9 separate relational tables (`orders`, `customers`, `order_items`, `sellers`, `order_payments`, `order_reviews`, etc.) introduced risks of duplicate row inflation and missing key references.
* **Engineered Solution**: Structured data extraction in `src/data_cleaning.py` using explicit primary-foreign key joins (`customer_id`, `order_id`, `seller_id`) combined with automated sanity checks verifying zero null values and zero duplicate customer records post-aggregation.

---

## 9. Strategic Recommendations

Based on empirical findings across RFM customer segmentation, logistics friction analysis, and financial payment mechanics, executive management should execute the following four data-driven strategies:

### 1. Protect High-Value Revenue via Automated CRM Triggers
* **Insight**: Cluster 1 (Dormant High-Spenders) contains 32,176 customers who spent an average of R$ 300.74 on high-ticket items (furniture, appliances) but have been inactive for ~281 days. Losing this segment represents a major revenue leak.
* **Actionable Strategy**: Deploy an automated "VIP Recency Watchdog" trigger. When a customer in the top 20% of monetary spend hits **120 days of inactivity**, automatically trigger personalized recommendations for complementary high-repeat categories (e.g., home decor accessories for furniture buyers) along with exclusive financing incentives.

### 2. Remediate Regional Fulfillment Bottlenecks in High-Revenue States
* **Insight**: Rio de Janeiro (RJ) generates over 13% of platform volume but suffers a **13.47% delivery delay rate**. Furthermore, long-haul routes from São Paulo to Northern states (e.g., SP → AL, SP → MA) take 22 to 25 days, causing 1- and 2-star reviews to surge to 52.89%.
* **Actionable Strategy**: Establish regional fulfillment partner nodes in the Northeast (e.g., Bahia or Pernambuco) to handle high-demand products, bypassing long-haul transit from SP. Implement strict logistics SLA monitoring for sellers in Maranhão (MA), where seller-side fulfillment delays reach 23.14%.

### 3. Deploy an Automated Logistics Friction Safety Net
* **Insight**: 16.63% of first-time buyers experience a service failure (delivery delay or negative review) on their very first order, creating a permanent barrier to platform return.
* **Actionable Strategy**: Implement an automated post-delivery compensation flow. When transactional logs record an order delayed by $>3$ days or traveling $>1,000\text{ km}$, automatically dispatch a proactive apology email with an instant R$ 20 category credit within 48 hours of delivery—rebuilding goodwill before the buyer forms a negative brand impression.

### 4. Capitalize on High-Installment Financing & Voucher Dynamics to Drive Retention
* **Insight**: Customers utilizing extended financing (7–10+ installments) show an Average Order Value **3.5x higher** (R$ 333.83 vs. R$ 95.87) and **double the repeat purchase rate** (10.85% vs. 5.41%) compared to single-payment buyers. Additionally, voucher users achieve an **8.56% repeat rate** (~40% higher than standard non-voucher buyers at 6.13%).
* **Actionable Strategy**: Promote flexible installment financing prominently on product pages for items over R$ 200. Integrate automated digital voucher rewards directly into post-purchase checkout confirmations to establish recurring purchase habits among first-time buyers.
