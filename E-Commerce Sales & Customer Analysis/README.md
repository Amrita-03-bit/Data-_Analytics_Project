# E-Commerce Sales Analysis

## Project Overview

This project analyzes e-commerce sales data to understand **sales performance, customer behavior, product performance, and business trends**.

The project follows a practical business-analysis scenario where an e-commerce company provides a sales dataset and asks an analyst to extract meaningful information from it for management decision-making.

## Business Objective

The objective of this project is to analyze the company's sales data and answer practical business questions related to:

- Overall sales performance
- Order value and order behavior
- Customer spending and purchasing behavior
- Product sales and revenue contribution
- Category performance
- City-wise sales performance
- Monthly and date-wise sales trends
- Top-performing customers and products
- Business performance and key findings

## Dataset

The project uses a single source dataset:

**File:** `data.csv`

The dataset contains:

- Order ID
- Customer Name
- City
- Product
- Category
- Quantity
- Price
- Order Date

The same dataset is used for the complete analysis. No duplicate dataset is created for different tools.

## Manager's Business Requirements

The analysis is designed around the following management requirements:

### Overall Business Analysis

1. Calculate the company's total sales value.
2. Calculate the average order value.
3. Identify the most expensive order.
4. Identify the lowest-value order.
5. Find the product sold in the highest quantity.
6. Find the product ordered most frequently.
7. Calculate total sales value for each product.
8. Calculate total sales for each category.
9. Calculate total sales for each city.
10. Calculate total spending for each customer.

### Customer Analysis

11. Identify the highest-spending customers.
12. Identify customers whose total spending is greater than ₹50,000.
13. Calculate the number of orders placed by each customer.
14. Calculate the total quantity purchased by each customer.
15. Identify the city with the highest number of orders.
16. Identify the city generating the highest revenue.

### Product Analysis

17. Identify the most expensive product.
18. Identify products priced above ₹10,000.
19. Calculate the number of distinct products in each category.
20. Calculate the average selling quantity for each product.

### Time Analysis

21. Calculate sales separately for January, February, and March.
22. Identify the month with the highest sales.
23. Identify the date with the highest sales.
24. Analyze the monthly sales trend.

### Business Questions

25. Identify the company's top customers.
26. Identify the products contributing the most revenue.
27. Identify the category generating the highest revenue.
28. Identify products selling in relatively low quantities.
29. Identify the top 3 products based on sales value.


## Analysis Approach

The analysis follows a structured workflow:

Company Dataset
      ↓
    data.csv
      ↓
 ┌────┴─────┐
 ↓          ↓
SQL      Python
          ↓
     Pandas + NumPy
          ↓
   Business Analysis
          ↓
    Key Findings

## Tools & Technologies

- **Python** — data analysis and programming
- **Pandas** — data cleaning, grouping, aggregation and analysis
- **NumPy** — numerical calculations and analysis
- **SQL** — business queries and data analysis
- **DuckDB** — querying the CSV dataset using SQL
- **Git & GitHub** — project version control and portfolio presentation

## Key Business Metrics

The analysis calculates business metrics such as:

- Total Sales
- Average Order Value
- Total Orders
- Total Quantity Sold
- Customer Spending
- Product Revenue
- Category Revenue
- City Revenue
- Monthly Sales
- Top Customers
- Top Products

For sales/revenue calculations, order value is calculated using:

Sales Value = Quantity × Price

## Business Findings

The final analysis provides **5–7 important findings** for management, covering areas such as:

- Revenue-generating products
- High-value customers
- Best-performing categories
- High-performing cities
- Monthly sales performance
- Product quantity performance
- Areas requiring further business attention

## Project Structure

E-Commerce-Analytics/
│
├── data.csv
├── 1.py
├── 2.sql
└── README.md

## Purpose

This project was developed as a practical **E-Commerce Sales Analysis** project to demonstrate the ability to work with a real-world style business dataset and convert raw sales data into meaningful business insights using SQL, Python, Pandas, and NumPy.

## Author

**Amrita**