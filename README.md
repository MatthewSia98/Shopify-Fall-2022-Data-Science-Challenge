```python
import pandas as pd
```


```python
df = pd.read_csv(r'https://docs.google.com/spreadsheets/d/16i38oonuX1y1g7C_UAmiK9GkY7cS-64DfiDMNiR41LM/export?format=csv&gid=0')
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>order_id</th>
      <th>shop_id</th>
      <th>user_id</th>
      <th>order_amount</th>
      <th>total_items</th>
      <th>payment_method</th>
      <th>created_at</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>53</td>
      <td>746</td>
      <td>224</td>
      <td>2</td>
      <td>cash</td>
      <td>2017-03-13 12:36:56</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>92</td>
      <td>925</td>
      <td>90</td>
      <td>1</td>
      <td>cash</td>
      <td>2017-03-03 17:38:52</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>44</td>
      <td>861</td>
      <td>144</td>
      <td>1</td>
      <td>cash</td>
      <td>2017-03-14 4:23:56</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>18</td>
      <td>935</td>
      <td>156</td>
      <td>1</td>
      <td>credit_card</td>
      <td>2017-03-26 12:43:37</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>18</td>
      <td>883</td>
      <td>156</td>
      <td>1</td>
      <td>credit_card</td>
      <td>2017-03-01 4:35:11</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4995</th>
      <td>4996</td>
      <td>73</td>
      <td>993</td>
      <td>330</td>
      <td>2</td>
      <td>debit</td>
      <td>2017-03-30 13:47:17</td>
    </tr>
    <tr>
      <th>4996</th>
      <td>4997</td>
      <td>48</td>
      <td>789</td>
      <td>234</td>
      <td>2</td>
      <td>cash</td>
      <td>2017-03-16 20:36:16</td>
    </tr>
    <tr>
      <th>4997</th>
      <td>4998</td>
      <td>56</td>
      <td>867</td>
      <td>351</td>
      <td>3</td>
      <td>cash</td>
      <td>2017-03-19 5:42:42</td>
    </tr>
    <tr>
      <th>4998</th>
      <td>4999</td>
      <td>60</td>
      <td>825</td>
      <td>354</td>
      <td>2</td>
      <td>credit_card</td>
      <td>2017-03-16 14:51:18</td>
    </tr>
    <tr>
      <th>4999</th>
      <td>5000</td>
      <td>44</td>
      <td>734</td>
      <td>288</td>
      <td>2</td>
      <td>debit</td>
      <td>2017-03-18 15:48:18</td>
    </tr>
  </tbody>
</table>
<p>5000 rows × 7 columns</p>
</div>



# Question 1a

#### This is the naive average order value


```python
df['order_amount'].sum() / df['order_amount'].size
```




    3145.128



#### Sorting by order amount reveals why the average is skewed
Shop 42 is selling an unreasonable amount of sneakers.<br>
They sold 34,063 pairs of sneakers in 30 days totalling $11,990,176.


```python
sorted_df = df.sort_values(['order_amount', 'total_items'], ascending=[False, True])
sorted_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>order_id</th>
      <th>shop_id</th>
      <th>user_id</th>
      <th>order_amount</th>
      <th>total_items</th>
      <th>payment_method</th>
      <th>created_at</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>42</td>
      <td>607</td>
      <td>704000</td>
      <td>2000</td>
      <td>credit_card</td>
      <td>2017-03-07 4:00:00</td>
    </tr>
    <tr>
      <th>60</th>
      <td>61</td>
      <td>42</td>
      <td>607</td>
      <td>704000</td>
      <td>2000</td>
      <td>credit_card</td>
      <td>2017-03-04 4:00:00</td>
    </tr>
    <tr>
      <th>520</th>
      <td>521</td>
      <td>42</td>
      <td>607</td>
      <td>704000</td>
      <td>2000</td>
      <td>credit_card</td>
      <td>2017-03-02 4:00:00</td>
    </tr>
    <tr>
      <th>1104</th>
      <td>1105</td>
      <td>42</td>
      <td>607</td>
      <td>704000</td>
      <td>2000</td>
      <td>credit_card</td>
      <td>2017-03-24 4:00:00</td>
    </tr>
    <tr>
      <th>1362</th>
      <td>1363</td>
      <td>42</td>
      <td>607</td>
      <td>704000</td>
      <td>2000</td>
      <td>credit_card</td>
      <td>2017-03-15 4:00:00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4219</th>
      <td>4220</td>
      <td>92</td>
      <td>747</td>
      <td>90</td>
      <td>1</td>
      <td>credit_card</td>
      <td>2017-03-25 20:16:58</td>
    </tr>
    <tr>
      <th>4414</th>
      <td>4415</td>
      <td>92</td>
      <td>927</td>
      <td>90</td>
      <td>1</td>
      <td>credit_card</td>
      <td>2017-03-17 9:57:01</td>
    </tr>
    <tr>
      <th>4760</th>
      <td>4761</td>
      <td>92</td>
      <td>937</td>
      <td>90</td>
      <td>1</td>
      <td>debit</td>
      <td>2017-03-20 7:37:28</td>
    </tr>
    <tr>
      <th>4923</th>
      <td>4924</td>
      <td>92</td>
      <td>965</td>
      <td>90</td>
      <td>1</td>
      <td>credit_card</td>
      <td>2017-03-09 5:05:11</td>
    </tr>
    <tr>
      <th>4932</th>
      <td>4933</td>
      <td>92</td>
      <td>823</td>
      <td>90</td>
      <td>1</td>
      <td>credit_card</td>
      <td>2017-03-24 2:17:13</td>
    </tr>
  </tbody>
</table>
<p>5000 rows × 7 columns</p>
</div>




```python
df.loc[df['shop_id'] == 42, ['total_items', 'order_amount']].sum()
```




    total_items        34063
    order_amount    11990176
    dtype: int64



# Question 1b
The median is a better metric to report because it is more resilient to outliers in the data.

# Question 1c
The median order value is $284.00.


```python
df['order_amount'].describe()
```




    count      5000.000000
    mean       3145.128000
    std       41282.539349
    min          90.000000
    25%         163.000000
    50%         284.000000
    75%         390.000000
    max      704000.000000
    Name: order_amount, dtype: float64



# Question 2a
#### 54 orders were shipped by Speedy Express
SELECT COUNT(*) FROM Orders <br>
WHERE ShipperID IN <br>
(SELECT ShipperID FROM Shippers <br>
WHERE ShipperName = 'Speedy Express') <br>

# Question 2b
#### Employee with last name "Peacock" has the most orders with a total number of 40
SELECT Employees.LastName, COUNT(*) as "NumOrders" <br>
FROM Orders <br>
JOIN Employees <br>
ON Orders.EmployeeID = Employees.EmployeeId <br>
GROUP BY Orders.EmployeeId <br>
ORDER BY 2 DESC <br>
LIMIT 1

# Question 2c
#### ProductID 40 called "Boston Crab Meat" is the most ordered product by customers in Germany with a total quantity of 160
SELECT OrderDetails.ProductID, Products.ProductName, SUM(OrderDetails.Quantity) as "Quantity" <br>
FROM Orders <br>
JOIN OrderDetails <br>
ON Orders.OrderID = OrderDetails.OrderID <br>
JOIN Products <br>
ON OrderDetails.ProductID = Products.ProductID <br>
JOIN Customers <br>
ON Orders.CustomerID = Customers.CustomerID <br>
WHERE Orders.CustomerID IN <br>
(SELECT CustomerID <br> 
FROM customers <br>
WHERE Country = 'Germany') <br>
GROUP BY OrderDetails.ProductID <br>
ORDER BY 3 DESC <br>
LIMIT 1
