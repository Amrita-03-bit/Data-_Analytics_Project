import numpy as np
import pandas as pd

df=pd.read_csv("data.csv")

#Q 1 Calculate the company's total sales value.

Total_sales=(df["quantity"]*df["price"]).sum()
print("Total sales value :",Total_sales)

#Q 2 Calculate the average order value.

total_average=Total_sales/len(df)
print("Average order value:",total_average)

#Q 3 Identify the most expensive order.

df["total_sales"] = df["quantity"] * df["price"]
most_exp=df.loc[df["total_sales"].idxmax(),"product"]
print("Most expensive order:",most_exp)

#Q4 Identify the lowest value order.

low_exp=df.loc[df["price"].idxmin(),["product","price"]]
print("Most expensive order:",low_exp)

#Q 5 Find the product sold in the highest quantity.

pro_sold=df.loc[df["quantity"].idxmax(),"product"]
print("product sold in the highest quantity:",pro_sold)

#Q6 Find the product ordered most frequently.

most_fre=df.groupby("product")["order_id"].count()
print("product ordered most frequently:",most_fre.idxmax())

#Q7 Calculate the total sales value for each product.


Total_pro=df.groupby("product")["total_sales"].sum()
print("total sales value for each product:",Total_pro)

#Q8 Calculate the total sales value for each category.

total_cate=df.groupby("category")["total_sales"].sum()
print("total sales value for each category:",total_cate)

#Q9 Calculate the total sales value for each city.

total_city=df.groupby("city")["total_sales"].sum()
print("total sales value for each city:",total_city)

#Q10 Calculate the total spending of each customer.

total_spending=df.groupby("customer_name")["total_sales"].sum()
print("total spending of each customer:",total_spending)

#Q11 Identify the highest-spending customers.

high_spending=df.loc[df["total_sales"].idxmax(),"customer_name"]
print("highest-spending customers:",high_spending)

#Q12 Identify customers whose total spending is greater than ₹50,000.

greater=df.loc[df["total_sales"]>50000,"customer_name"]
print("customers whose total spending is greater than ₹50,000:",greater)

#Q 13 Calculate the number of orders placed by each customer.

no_of_order=df.groupby("customer_name")["order_id"].count()
print("number of orders placed by each customer",no_of_order)

#Q14 Calculate the total quantity purchased by each customer.

total_qun=df.groupby("customer_name")["quantity"].sum()
print("total quantity purchased by each customer.",total_qun)

#Q15 Identify the city with the highest number of orders.

orders_by_city = df.groupby("city")["order_id"].count()
print("city with the highest number of order:",orders_by_city.idxmax())

#Q16 Identify the city generating the highest revenue.

high_rev=df.groupby("city")["total_sales"].sum()
print("city generating the highest revenue:",high_rev.idxmax())

#Q17 Identify the most expensive product.

exp_pro=df.loc[df["price"].idxmax(),"product"]
print("most expensive product:",exp_pro)

#Q18 Identify products priced above ₹10,000.

pro_greater=df.loc[df["price"]>10000,"product"]
print("products priced above ₹10,000:",pro_greater)

#Q19 Calculate the number of distinct products in each category.

diff_pro=df.groupby("category")["product"].count()
print("number of distinct products in each category",diff_pro)

#Q20 Calculate the average selling quantity for each product.

avg_quantity = df.groupby("product")["quantity"].mean()
print("average selling quantity for each product.",avg_quantity)

#Q21. Calculate the sales for January, February, and March separately.
 
df["month"] = pd.to_datetime(df["order_date"]).dt.month_name()
monthly_sales = df.groupby("month")["total_sales"].sum()
print("sales for January, February, and March separately:",monthly_sales)


#22 Identify the month with the highest sales.

highest_sales_month = monthly_sales.idxmax()
print("Month with highest sales:", highest_sales_month)

#23 Identify the date with the highest sales.

df["date"]=pd.to_datetime(df["order_date"])
highest_sales=df.loc[df["total_sales"].idxmax(),"date"]
print("date with the highest sales:",highest_sales)

#24 Calculate the monthly sales trend.

monthly_sales = df.groupby("month")["total_sales"].sum()
print("Monthly sales trend:",monthly_sales.sort_index())