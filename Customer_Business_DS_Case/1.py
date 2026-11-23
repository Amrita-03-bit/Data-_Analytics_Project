
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()

''' Dashboard 1 — Executive Overview

Management should be able to understand the company's overall performance at a glance.

Show:

- Total Revenue
- Total Orders
- Total Purchasing Customers
- Average Order Value
- Monthly Revenue Trend
- Revenue by Category
- Orders by Status
- Revenue Growth / Decline'''

# Q1 - Dashboard Outputs
# Dashboard Demo Video:
# https://drive.google.com/file/d/1uw0ZaqyVUMZA65MomoUmw-shuUYgRY_5/view?usp=sharing

''' Dashboard 2 — Customer Analytics

Show:

- Revenue by Customer Segment
- Top 10 Customers by Revenue
- Repeat Customers vs One-Time Customers
- Customer Purchase Frequency
- Customer Signup Trend
- Revenue by City
- Customer Spending Analysis'''

# Q2 - Dashboard Outputs
# Dashboard Demo Video:
# https://drive.google.com/file/d/1NM1mJYJVEixrAzMe-sodvmi7UK0JXfaa/view?usp=sharing

'''# Dashboard 3 — Product & Returns Analytics

Show:

- Top 10 Products by Revenue
- Top 10 Products by Quantity Sold
- Revenue by Product Category
- Low-Performing Products
- Return Rate
- Returns by Category
- Return Reasons
'''

# Q3 - Dashboard Outputs
# Dashboard Demo Picture:
#https://drive.google.com/file/d/1goxE3XpfG305gxt2bVuDSH16sj4fHheJ/view?usp=sharing

'''## Dashboard 4 — Marketing & Customer Support

Show:

- Marketing Spend
- Total Clicks
- Total Conversions
- Campaign Conversion Rate
- Campaign Performance Comparison
- Support Ticket Count
- Tickets by Issue Type
- Average Resolution Time
- Resolution Time by Issue Type

---'''
# Q4 - Dashboard Outputs
# Dashboard Demo Picture:
#https://drive.google.com/file/d/1ik7SuTSQB2m0dIni-rpO5Lb8WeqfcoJs/view?usp=sharing