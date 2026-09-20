import os
import mysql.connector
import pandas as pd
import numpy as np
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password = os.getenv("MYSQL_PASSWORD"),
    database="food_delivery_db"
)
query = "SELECT *FROM restaurants;"

df = pd.read_sql(query, conn)

# 5 Find the number of restaurants in each city.

num_of_res=df.groupby("city")["restaurant_name"].count()
print("number of restaurants in each city",num_of_res)

query_1="SELECT * FROM customers;"
df=pd.read_sql(query_1,conn)

# 6 . Find the number of customers in each city.

num_of_cus=df.groupby("city")["customer_name"].count()
print("number of customers in each city ",num_of_cus)

# 10. Check whether any table contains duplicate primary-key values.

tables={
    "customers":"customer_id",
    "restaurants":"restaurant_id",
    "orders":"order_id",
    "order_items":"order_item_id",
    "payments":"payment_id",
    }
for table,id in tables.items():

    query_3=f"SELECT {id} FROM {table}"
    df=pd.read_sql(query_3,conn)

    if df[id].duplicated().any():
        print(f"{table}:Duplicate primary_key values found")
    else:
        print(f"{table}: NO duplicate primary_kry values")  

# 13. Find the total number of orders placed by each customer.

query_4="SELECT customers.customer_name,orders.order_id FROM customers INNER JOIN orders ON customers.customer_id=orders.customer_id;"

df=pd.read_sql(query_4,conn)

total_order=df.groupby("customer_name")["order_id"].nunique()
print("total number of orders placed by each customer", total_order) 

#14. Find the total amount spent by each customer.

query_5="SELECT customers.customer_name,(order_items.quantity*order_items.item_price) as total_amount  FROM customers INNER JOIN orders ON customers.customer_id=orders.customer_id INNER JOIN order_items ON orders.order_id=order_items.order_id;"

df=pd.read_sql(query_5,conn)

total_amount=df.groupby("customer_name")["total_amount"].sum()
print("total amount spent by each customer",total_amount)

#15. Identify the highest-spending customer.

high_spending=df.loc[df["total_amount"].idxmax(),"customer_name"]
print("Identify the highest-spending customer:",high_spending)

#21. Find customers who placed more than 5 orders.

query_6="SELECT customers.customer_name , orders.order_id FROM customers INNER JOIN orders on customers.customer_id=orders.customer_id;"

df=pd.read_sql(query_6,conn)

place=df.groupby("customer_name")["order_id"].count()
print("customers who placed more than 5 orders:",place[place>5])

#22. Find restaurants whose revenue is greater than the average restaurant revenue.

query_7="SELECT restaurants.restaurant_name,(order_items.quantity*order_items.item_price) as total_revenue FROM restaurants INNER JOIN orders ON restaurants.restaurant_id=orders.restaurant_id INNER JOIN order_items ON order_items.order_id=orders.order_id; "

df=pd.read_sql(query_7,conn)

rest_ren=df.groupby("restaurant_name")["total_revenue"].sum()
avg_rev=rest_ren.mean()
print("restaurants whose revenue is greater than the average restaurant revenue:",rest_ren[rest_ren>avg_rev])

# Q30  Calculate month-over-month revenue

query_8="SELECT orders.order_date,order_items.item_price*order_items.quantity AS revenue FROM orders INNER JOIN  order_items ON orders.order_id=order_items.order_id WHERE orders.order_status='Delivered';"

df=pd.read_sql(query_8,conn)

df["order_date"]=pd.to_datetime(df["order_date"])
df["month"]=df["order_date"].dt.to_period("M")

monthly_revenue=df.groupby("month")["revenue"].sum().reset_index()
monthly_revenue["previous_month_revenue"]=monthly_revenue["revenue"].shift(1)
monthly_revenue["mom_percentage"] = (monthly_revenue["revenue"] - monthly_revenue["previous_month_revenue"])

print(monthly_revenue)

#31. Bring a useful SQL result into Pandas and inspect the DataFrame.

query_9 = "SELECT orders.order_id,customers.customer_name, orders.order_status, orders.order_date FROM orders INNER JOIN customers ON orders.customer_id = customers.customer_id;"

df = pd.read_sql(query_9, conn)
print(df)

#32. Check missing values.

print("check missing values:",df.isnull().sum()) 

#33. Check duplicate records.

print("duplicate records:",df.duplicated().sum())

#34. Convert date columns to datetime.

df["order_date"]=pd.to_datetime(df["order_date"])
print("Convert date columns to datetime:",df["order_date"])

#35. Create an `order_value` column where appropriate.

query_10="SELECT * FROM order_items"
df=pd.read_sql(query_10,conn)
df["order_value"] = df["item_price"] * df["quantity"]

#36. Analyze customer spending distribution.

query_11="SELECT customers.customer_name , order_items.quantity*order_items.item_price AS order_value FROM customers INNER JOIN orders ON customers.customer_id=orders.customer_id INNER JOIN order_items ON order_items.order_id=orders.order_id;"
df=pd.read_sql(query_11,conn)
customer_spending = df.groupby("customer_name")["order_value"].sum()
print("customer spending distribution",customer_spending.describe())

#37. Find the highest-value customers.

high_value=df.loc[df["order_value"].idxmax(),"customer_name"]
print("highest-value customers:",high_value)

#38. Analyze restaurant performance using Pandas.

query_12 = "SELECT restaurants.restaurant_name,orders.order_id,orders.order_status,order_items.item_price,order_items.quantity FROM restaurants INNER JOIN orders ON restaurants.restaurant_id = orders.restaurant_id INNER JOIN order_items ON orders.order_id = order_items.order_id;"

df = pd.read_sql(query_12, conn)

df["revenue"] = df["item_price"] * df["quantity"]
restaurant_performance = df.groupby("restaurant_name").agg(
    total_orders=("order_id", "nunique"),
    total_revenue=("revenue", "sum")
).reset_index()

print(restaurant_performance)

#39.  Analyze delivery-time statistics by restaurant.

print(" Analyze delivery-time statistics by restaurant → Not applicable with the current dataset because delivery-time data is not available.")

#40. Identify unusually high delivery times.

print(" identify unusally high delivery times → Not applicable with the current dataset because delivery-time data is not available.")

#41. Compare average order values across cities.

query_13 = "SELECT restaurants.city,order_items.item_price * order_items.quantity AS order_value FROM restaurants INNER JOIN orders ON restaurants.restaurant_id = orders.restaurant_id INNER JOIN order_items ON orders.order_id = order_items.order_id;"

df = pd.read_sql(query_13, conn)

average_order =df.groupby("city")["order_value"].mean().reset_index()
print("Average order value across cities:",average_order)

#42. What city generates the most revenue?

most_rev=df.groupby("city")["order_value"].sum().idxmax()
print("What city generates the most revenue:",most_rev)

#43. Which restaurants are major revenue contributors?

query_14="SELECT restaurants.restaurant_name,order_items.item_price * order_items.quantity AS order_value FROM restaurants INNER JOIN orders ON restaurants.restaurant_id = orders.restaurant_id INNER JOIN order_items ON orders.order_id = order_items.order_id;"

df=pd.read_sql(query_14,conn)
restaurant_revenue = df.groupby("restaurant_name")["order_value"].sum().sort_values(ascending=False).reset_index()
print("Major revenue contributors:",restaurant_revenue.head(5))

#44. What proportion of orders are cancelled?

query_15="SELECT*FROM orders"

df=pd.read_sql(query_15,conn)

cancalled=(df["order_status"]=="Cancelled").sum()
total=len(df)
cancelled_per=(cancalled/total)*100
print("proportion of orders are cancelled:",cancelled_per)

#45. Which payment method is used most often?

query_16="SELECT*FROM payments"

df=pd.read_sql(query_16,conn)

pay_met=df["payment_method"].value_counts().idxmax()
print("Which payment method is used most often:",pay_met)

#46. Which customers are high-value?

query_17="SELECT customers.customer_name,order_items.quantity*order_items.item_price AS order_value FROM customers INNER JOIN orders ON customers.customer_id=orders.customer_id INNER JOIN order_items ON order_items.order_id=orders.order_id;"

df=pd.read_sql(query_17,conn)

high_val=df.groupby("customer_name")["order_value"].sum().idxmax()
print("customers are high-value:",high_val) 


#print(df)