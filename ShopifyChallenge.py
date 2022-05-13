#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r'https://docs.google.com/spreadsheets/d/16i38oonuX1y1g7C_UAmiK9GkY7cS-64DfiDMNiR41LM/export?format=csv&gid=0')
print(df, '\n')


# # Question 1a

# #### This is the naive average order value

# In[3]:


print(df['order_amount'].sum() / df['order_amount'].size, '\n')


# #### Sorting by order amount reveals why the average is skewed
# Shop 42 is selling an unreasonable amount of sneakers.
# They sold 34,063 pairs of sneakers in 30 days totalling $11,990,176.

# In[4]:


sorted_df = df.sort_values(['order_amount', 'total_items'], ascending=[False, True])
print(sorted_df, '\n')


# In[5]:


print(df.loc[df['shop_id'] == 42, ['total_items', 'order_amount']].sum(), '\n')


# # Question 1b
# The median is a better metric to report because it is more resilient to outliers in the data.

# # Question 1c
# The median order value is $284.00.

# In[6]:


print(df['order_amount'].describe())


# # Question 2a
# #### 54 orders were shipped by Speedy Express
# SELECT COUNT(*) FROM Orders 
# WHERE ShipperID IN 
# (SELECT ShipperID FROM Shippers 
# WHERE ShipperName = 'Speedy Express') 

# # Question 2b
# #### Employee with last name "Peacock" has the most orders with a total number of 40
# SELECT Employees.LastName, COUNT(*) as "NumOrders" 
# FROM Orders 
# JOIN Employees 
# ON Orders.EmployeeID = Employees.EmployeeId 
# GROUP BY Orders.EmployeeId 
# ORDER BY 2 DESC 
# LIMIT 1

# # Question 2c
# #### ProductID 40 called "Boston Crab Meat" is the most ordered product by customers in Germany with a total quantity of 160
# SELECT OrderDetails.ProductID, Products.ProductName, SUM(OrderDetails.Quantity) as "Quantity" 
# FROM Orders 
# JOIN OrderDetails 
# ON Orders.OrderID = OrderDetails.OrderID 
# JOIN Products 
# ON OrderDetails.ProductID = Products.ProductID 
# JOIN Customers 
# ON Orders.CustomerID = Customers.CustomerID 
# WHERE Orders.CustomerID IN 
# (SELECT CustomerID  
# FROM customers 
# WHERE Country = 'Germany') 
# GROUP BY OrderDetails.ProductID 
# ORDER BY 3 DESC 
# LIMIT 1
