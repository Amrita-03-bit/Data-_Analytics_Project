import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



load_dotenv()
password = os.getenv("DB_PASSWORD")
engine = create_engine(f"mysql+pymysql://northwind_user:{password}@localhost:3306/northwind")


# 1. How many customers are present in the database?

customers = pd.read_csv("data/Northwind Traders/customers.csv")
total_customers = customers.shape[0]
print("Total Customers:", total_customers)

# 2. How many unique countries do customers belong to?

total_country=customers["country"].nunique()
print("Total country:",total_country)

#3. Which countries have the highest number of customers?

df=customers
counts=df.groupby("country")["customerID"].count()
highest_count=counts[counts==counts.max()]
print("countries have the highest number of customers:",highest_count)

# Create bar graph

plt.figure(figsize=(12, 6))
bars=plt.bar(counts.index,counts.values)
plt.bar_label(bars)
plt.xlabel("Country Name")
plt.ylabel("Number of Customers")
plt.title("Number of Customers by Country")
plt.xticks(rotation=45)
plt.savefig("outputs/charts/customers_by_country.png",dpi=300,bbox_inches="tight")
plt.show()

# 4. Which customers have placed the highest number of orders?

query="SELECT customerID, COUNT(orderID) AS total_orders FROM orders GROUP BY customerID HAVING total_orders=(SELECT MAX(total_orders) FROM (SELECT COUNT(orderID) AS total_orders FROM orders GROUP BY customerID)AS customer_counts);"
df = pd.read_sql(query, engine)
print("highest order:",df)

# 5. Which customers have never placed an order?

query_1="SELECT c.customerID FROM customers AS c LEFT JOIN orders AS o ON c.customerID=o.customerID WHERE o.orderID IS NULL; "
df=pd.read_sql(query_1,engine)
print("order not placed:\n",df)

# 6. How many products are available in the database?

products = pd.read_csv("data/Northwind Traders/products.csv")
total_products = len(products)
print("total products :",total_products)

# 7. Which products have the highest unit prices?

query_2="SELECT productName,unitPrice FROM products WHERE unitPrice=(SELECT MAX(unitPrice) FROM products); "
df=pd.read_sql(query_2,engine)
print("highest_price:\n",df)

# 8. Which products are discontinued?

query_3="SELECT productName discontinued FROM products WHERE discontinued>=1;"
df=pd.read_sql(query_3,engine)
print("discontinued \n",df)

# 9. Which product categories contain the highest number of products?

query_4="SELECT c.categoryName , COUNT(p.productID) as total_products FROM products AS p INNER JOIN categories AS c ON c.categoryID=p.categoryID GROUP BY c.categoryName,c.categoryID  HAVING total_products =(SELECT MAX(total_products) FROM (SELECT COUNT(productID) AS total_products FROM products GROUP BY categoryID) AS category_counts);"
df=pd.read_sql(query_4,engine)
print("Highest product category:\n", df)

# 10. Which products have the lowest unit prices?
query_5="SELECT productName,unitPrice FROM products WHERE unitPrice=(SELECT MIN(unitPrice) FROM products); "
df=pd.read_sql(query_5,engine)
print("lowest_price:\n",df)

# 11. What is the total revenue generated from all orders?

query_6="SELECT orderID ,SUM(unitPrice*quantity) AS Revenue FROM order_details GROUP BY orderID; "
df=pd.read_sql(query_6,engine)
print("total revenue by order:\n",df)

# 12. Which products generate the highest revenue?

query_7="SELECT p.productName , SUM(o.unitPrice*o.quantity) AS Revenue FROM order_details AS o INNER JOIN products AS p ON o.productID=p.productID GROUP BY p.productID,p.productName HAVING Revenue=(SELECT MAX(Revenue) FROM(SELECT SUM(unitPrice*quantity) AS Revenue FROM order_details  GROUP BY productID ) AS product_revenue); "
df = pd.read_sql(query_7, engine)
print("Products with highest revenue:\n", df)

# 13. Which product categories generate the highest revenue?

query_8="SELECT c.categoryName,SUM(o.unitPrice*o.quantity) AS Revenue FROM products AS p INNER JOIN order_details AS o ON o.productID=p.productID INNER JOIN categories AS c ON c.categoryID=p.categoryID  GROUP BY c.categoryID, c.categoryName HAVING Revenue=(SELECT MAX(Revenue) FROM (SELECT SUM(o.unitPrice*o.quantity) AS Revenue FROM  products AS p INNER JOIN order_details AS o ON o.productID=p.productID GROUP BY p.categoryID) AS category_revenue);"
df=pd.read_sql(query_8,engine)
print("category having highest revenue:\n",df)

# 14. Which countries generate the highest sales revenue?

query_9="SELECT c.country,SUM(o.unitPrice*o.quantity) AS Revenue FROM orders AS ord INNER JOIN order_details AS o ON ord.orderID=o.orderID  INNER JOIN customers AS c ON c.customerID=ord.customerID GROUP BY c.country HAVING Revenue=(SELECT MAX(Revenue) FROM(SELECT SUM(o.unitPrice*o.quantity) AS revenue FROM orders AS ord INNER JOIN order_details AS o ON ord.orderID=o.orderID INNER JOIN customers AS c ON c.customerID = ord.customerID GROUP BY c.country) AS country_revenue);"
df=pd.read_sql(query_9,engine)
print("highest country revenue\n",df)

# 15. What is the average order value?

query_10="SELECT AVG(order_revenue) AS average FROM (SELECT orderID,SUM(unitPrice*quantity) AS order_revenue FROM order_details GROUP BY orderID) AS order_value;"
df=pd.read_sql(query_10,engine)
print("average order value \n",df)

# 16. How many total orders are present in the database?

query_11="SELECT count(orderID) AS total_order FROM orders;"
df=pd.read_sql(query_11,engine)
print("total_order:",df)

# 17. Which customers have placed the most orders?

query_12="SELECT customerID,COUNT(orderID) AS customer_order FROM orders GROUP BY customerID HAVING customer_order=(SELECT MAX(customer_order) FROM(SELECT COUNT(orderID) AS customer_order FROM orders GROUP BY customerID) AS customer_count);"
df=pd.read_sql(query_12,engine)
print("customer most order\n",df)

# 18. Which months have the highest number of orders?

query_13="SELECT DATE_FORMAT(orderDate,'%%M_%%Y')AS ORDER_MONTH , COUNT(orderID)  AS total_order FROM orders GROUP BY DATE_FORMAT(orderDate,'%%M_%%Y') HAVING total_order =(SELECT MAX(total_order) FROM (SELECT COUNT(orderID) AS total_order FROM orders GROUP BY DATE_FORMAT(orderDate,'%%M_%%Y')) AS order_date); "
df=pd.read_sql(query_13,engine)
print("highest month order\n",df)

# 19. What is the monthly sales trend?

query_14="SELECT DATE_FORMAT(orderDate,'%%M_%%Y')AS ORDER_MONTH , COUNT(orderID)  AS total_order FROM orders GROUP BY DATE_FORMAT(orderDate,'%%M_%%Y');"
df=pd.read_sql(query_14,engine)
print("monthly sales trend\n",df)

plt.figure(figsize=(10,6))
plt.plot(df["ORDER_MONTH"],df["total_order"],marker="s")
plt.xlabel("month")
plt.ylabel("total order")
plt.title("monthly sales trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid()
plt.savefig("outputs/charts/month_trend.png",dpi=300,bbox_inches="tight")
plt.show()

#20. What is the average number of products per order?

query_15="SELECT AVG(product_order) AS average FROM  (SELECT orderID ,SUM(quantity) AS product_order FROM order_details GROUP BY orderID) AS order_products;"
df=pd.read_sql(query_15,engine)
print("average product order\n",df)

# 21. Which employees have handled the highest number of orders?

query_16="SELECT e.employeeID,e.employeeNAME ,COUNT(o.orderID) AS total_order FROM orders AS o INNER JOIN employees AS e ON e.employeeID=o.employeeID GROUP BY e.employeeID,e.employeeName HAVING total_order=(SELECT MAX(total_order) FROM (SELECT COUNT(orderID) AS total_order FROM orders GROUP BY employeeID )AS employee_orders); "
df=pd.read_sql(query_16,engine)
print("employee highest order\n",df)

# 22. Which employees have generated the highest sales revenue?

query_17="SELECT e.employeeID,e.employeeName,SUM(o.quantity * o.unitPrice) AS Revenue FROM employees  AS e  INNER JOIN orders AS ord ON e.employeeID=ord.employeeID INNER JOIN order_details AS o ON ord.orderID=o.orderID GROUP BY e.employeeID,e.employeeName HAVING Revenue =(SELECT MAX(Revenue)FROM (SELECT SUM(o.quantity * o.unitPrice) AS Revenue  FROM orders AS ord INNER JOIN order_details AS o ON o.orderID=ord.orderID GROUP BY  ord.employeeID) AS employee_revenue);"
df=pd.read_sql(query_17,engine)
print("employee revenue\n",df)

#23. Which shipping companies have handled the most orders?

query_18="SELECT s.companyName,COUNT(o.orderID) AS total_order FROM shippers AS s INNER JOIN orders AS o ON o.shipperID=s.shipperID GROUP BY s.shipperID,s.companyName HAVING total_order=(SELECT MAX(total_order) FROM (SELECT COUNT(o.orderID) AS total_order FROM orders AS o INNER JOIN shippers AS s ON s.shipperID=o.shipperID GROUP BY s.shipperID ) AS shipper_order);"
df=pd.read_sql(query_18,engine)
print("shipping highest order\n",df)

#24. What is the average shipping time?

query_19="SELECT AVG(DATEDIFF(shippedDate,orderDate)) AS average_shipping_days FROM orders WHERE shippedDate IS NOT NULL AND orderDate IS NOT NULL;"
df=pd.read_sql(query_19,engine)
print("averge shipping time\n",df)

# 25. Which countries have the longest average shipping time?

query_20="SELECT c.country,AVG(DATEDIFF(O.shippedDate,O.orderDate)) AS average_shipping FROM orders AS o INNER JOIN customers AS c ON o.customerID=c.customerID WHERE o.shippedDate IS NOT NULL AND o.orderDate IS NOT NULL GROUP BY c.country HAVING average_shipping=(SELECT MAX(average_shipping) FROM (SELECT AVG(DATEDIFF(o.shippedDate,o.orderDate)) AS average_shipping FROM orders AS o INNER JOIN customers AS c ON c.customerID=o.customerID  WHERE o.shippedDate IS NOT NULL AND o.orderDate IS NOT NULL GROUP BY c.country) AS country_average); "
df=pd.read_sql(query_20,engine)
print("largest average time by country\n",df)