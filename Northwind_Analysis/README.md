# Northwind Traders – Data Analytics Project

## 1. Project Overview

Northwind Traders is a data analytics project focused on analyzing sales, customers, products, orders, employees, and shipping operations.

The project uses SQL, Python, Pandas, NumPy, Matplotlib, and Seaborn to explore business data, identify patterns, evaluate performance, and generate meaningful business insights.

## 2. Project Objectives

- Analyze overall sales and revenue performance.
- Identify top-performing products and categories.
- Understand customer purchasing behavior.
- Analyze sales performance across different countries.
- Evaluate employee performance.
- Examine order and shipping trends.
- Identify discontinued and low-performing products.
- Generate actionable business insights.

## 3. Dataset Description

The project uses seven CSV datasets from the Northwind Traders database.

| Dataset | Description |
|---|---|
| categories.csv | Product category information |
| customers.csv | Customer details and locations |
| employees.csv | Employee information |
| orders.csv | Customer order details |
| order_details.csv | Products and quantities in each order |
| products.csv | Product information and prices |
| shippers.csv | Shipping company details |

## 4. Tools and Technologies

- **Python** – Data analysis and processing
- **SQL (MySQL 8.0)** – Database queries and business analysis
- **Pandas** – Data manipulation and cleaning
- **NumPy** – Numerical calculations
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **Jupyter Notebook / VS Code** – Development environment
- **Git and GitHub** – Project version control

## 5. Business Questions

### A. Customer Analysis

1. How many customers are present in the database?
2. How many unique countries do customers belong to?
3. Which countries have the highest number of customers?
4. Which customers have placed the highest number of orders?
5. Which customers have never placed an order?

### B. Product Analysis

6. How many products are available in the database?
7. Which products have the highest unit prices?
8. Which products are discontinued?
9. Which product categories contain the highest number of products?
10. Which products have the lowest unit prices?

### C. Sales and Revenue Analysis

11. What is the total revenue generated from all orders?
12. Which products generate the highest revenue?
13. Which product categories generate the highest revenue?
14. Which countries generate the highest sales revenue?
15. What is the average order value?

### D. Order Analysis

16. How many total orders are present in the database?
17. Which customers have placed the most orders?
18. Which months have the highest number of orders?
19. What is the monthly sales trend?
20. What is the average number of products per order?

### E. Employee and Shipping Analysis

21. Which employees have handled the highest number of orders?
22. Which employees have generated the highest sales revenue?
23. Which shipping companies have handled the most orders?
24. What is the average shipping time?
25. Which countries have the longest average shipping time?

## 6. Project Workflow

### Step 1: Data Collection
- Collect the seven Northwind CSV datasets.
- Import the datasets into MySQL.
- Verify the database tables.

### Step 2: Database Exploration
- Inspect table structures.
- Identify columns and data types.
- Understand primary keys and relationships.
- Check the number of records in each table.

### Step 3: SQL Analysis
- Perform data exploration.
- Use filtering, grouping, sorting, and aggregate functions.
- Apply joins to combine related tables.
- Solve the 25 business questions.

### Step 4: Data Cleaning
- Load datasets using Pandas.
- Check missing values and duplicate records.
- Verify data types.
- Handle inconsistent data where necessary.

### Step 5: Exploratory Data Analysis (EDA)
- Perform univariate analysis.
- Perform bivariate analysis.
- Perform multivariate analysis.
- Identify trends and patterns.

### Step 6: Data Visualization
- Create bar charts for product and category comparisons.
- Create line charts for monthly sales trends.
- Create suitable charts for customer and employee performance.
- Interpret the visual results.

### Step 7: Business Insights
- Summarize important findings.
- Identify high-performing products and customers.
- Understand sales and shipping patterns.
- Present data-driven recommendations.

## 7. Visualizations

The project will include relevant visualizations such as:

- Country-wise customer distribution
- Top-selling products
- Category-wise revenue
- Monthly sales trends
- Employee sales performance
- Shipping company performance

## 8. Project Structure

```text
Northwind_Analysis/
│
├── data/
│   └── Northwind Traders/
│       ├── categories.csv
│       ├── customers.csv
│       ├── employees.csv
│       ├── orders.csv
│       ├── order_details.csv
│       ├── products.csv
│       └── shippers.csv
│
├── outputs/
│   ├── charts/
│   
│
├── 1.py
|
├── README.md

```

## 9. Expected Outcomes

- Better understanding of sales performance.
- Identification of top-performing products and customers.
- Insights into customer purchasing patterns.
- Evaluation of employee and shipping performance.
- Improved understanding of business operations.
- Data-driven recommendations for business improvement.

## 10. Conclusion

This project demonstrates the practical application of SQL, Python, and data visualization techniques in business analytics.

By analyzing the Northwind Traders dataset, the project aims to transform raw business data into meaningful insights that can support better decision-making.

---

**Project Category:** Data Analytics  
**Author:** Amrita  
**Tools:** Python, SQL, Pandas, NumPy, Matplotlib, Seaborn, MySQL