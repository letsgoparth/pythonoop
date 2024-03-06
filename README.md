# OOPs with Python
Object Oriented Programming with Python

<br/>
<div align="center">
  <img src="images/logo.png" alt="Logo" width="300" height="80">
  </a>
  

  <h3 align="center">OOP with Python</h3>

  <p align="center">
    Notes to recall fundamentals of Object Oriented Programming using Python
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#create-table">Class Basics</a></li>
    <li>
      <a href="#insert">Creating Class</a>
      <ul>
        <li><a href="#Inserting-single record">Creating Instance</a></li>
        <li><a href="#Inserting-with-reference-to-fields">Inserting with reference to fields</a></li>
        <li><a href="#inserting-multiple-records">Inserting Multiple Records</a></li>
      </ul>
    </li>
    <li><a href="#copy-table">Copy Table</a></li>
    <li><a href="#roadmap">Update</a></li>
    <li><a href="#contributing">Delete</a></li>
    <li><a href="#license">Select</a></li>
    <li><a href="#contact">Limit</a></li>
    <li><a href="#acknowledgments">Alias</a></li>
  </ol>
</details>

## Class Basics
### Creating Class
  ```python
  class one:
    pass
  ```

### Creating Instance
```python
class one:
    pass

ins = one()
```
### Class Methods
```python
class Item:
    def cal(self,x,y):
        return x*y

obj = Item()
obj.name = "Phone"
obj.price = 100
obj.quantity = 5

print(obj.cal(obj.price,obj.quantity))         

obj2 = Item()
obj2.name = "Laptop"
obj2.price = 1000
obj2.quantity = 3

print(obj2.cal(obj2.price,obj2.quantity))         

```

```
500
3000
```

## Magic Methods
Predefined methods staring with double undercores "__"

### Constructor

```python 
class Item:
    def __init__(self):
        print("Object Created")
```

### Parameterised Constructor with Dynamic Attributes

```python 
class one:
    def __init__(self,name,price,quantity=0):
        self.price = price
        self.quantity = quantity
        print(f"Instance created for {name}")

    def calculate_price(self):
        return self.price*self.quantity

ins = one("Phone",200,5)
print(ins.calculate_price())
```
```
Instance created for Phone
1000
```

### Assert Keyword
Debigging code using conditional statement

```python
class one:
    def __init__(self,price,quantity):
        self.price = price
        self.quantity = quantity
        
        assert price > 0, f"Price {price} is less than 1"
        assert quantity > 0, f"Quantity{quantity} is less than 1"
        
ins = one(0,5)
```
```
AssertionError: Price 0 is less than 1
```

### Class Attribute
Attributes defined in the class

```python
class one:
  a = 4
```
### View Attributes
```python
class one:
    def __init__(self,price,quantity):
        self.price = price
        self.quantity = quantity
        
ins = one(1,5)
print(ins.__dict__)
```
```
{'price': 1, 'quantity': 5}
```
### Item.all


```python
for i in classname.all:
  print(i.name)
```
### 





<!-- ## Insert
### Inserting single record

  ```sql
  INSERT INTO customers
  VALUES(‘Chester’, ‘Bennington’,’199901-01’)
  ```
### Inserting with reference to fields

  ```sql
  INSERT INTO customers(
      id,
      first_name,
      last_name)

  VALUES(
    1,
    ‘Mike’,
    ‘Shinoda’)

  ```
### Inserting Multiple Records
  ```sql
  INSERT INTO customers(
    First_name,
    Last_name,
    Instrument)
  VALUES
    (‘Mike’, ’Shinoda’, ’Producer’),
    (‘Joe’, ‘Hann’, Turntables’),
    (‘Rob’, ’Bourdon’, Drums’),

  ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Copy Table

### Copying table as it is

```sql
CREATE TABLE orders_archived AS
SELECT * FROM orders
```
### Copying with condition

```sql
CREATE TABLE orders_archived
SELECT * 
FROM orders
WHERE order_date <’2019-01-01’
 ```

## Update


```sql
UPDATE invoices
SET
payment_total = 0,
payment_date = ‘2019-03-01’
WHERE invoice_id = 1
```

## Delete

```sql
DELETE FROM invoices
WHERE invoice_id = (
  SELECT *
  FROM Clients
  WHERE name=’Myworks’)
```

## Select

```sql
SELECT *
  FROM customers
  WHERE customer_id = 1
  ORDER BY first_name
```
```sql
SELECT
  last_name,
  first_name,
  points+10
FROM customers
```

## Limit

```sql
SELECT *
FROM CUSTOMERS
LIMIT 3
```
```sql
SELECT *
FROM CUSTOMERS
LIMIT 6,3
```
* Skip first 6, get 3
## Alias

```sql
SELECT
  last_name,
  first_name,
  points + 10 as discount_factor
```
### Table Aliases
```sql
SELECT * c.order_id, o.order_id
  FROM orders o
  JOIN customer c
	  ON o.customer_id =c.customer_id
```
## Distinct

```sql
SELECT DISTINCT state
FROM customers
```

## Where

```sql
Select *
FROM customers
WHERE points > 3000
```
| Operators |  |
| -------- | ------- |
| != | not |
| <> | not |
| AND | and |
| OR | or |

```sql
SELECT *
FROM customers
WHERE birth_date > ‘2000-01-01’ OR points > 10
```

## In

```sql
SELECT *
FROM customers
  WHERE state IN(‘NY’,’TX’,’IL’)
```

## Between

```sql
DELETE FROM invoices
WHERE invoice_id = (
  SELECT *
  FROM Clients
  WHERE name=’Myworks’)
```
## Like

```sql
SELECT *
FROM customers
  WHERE last_name LIKE ‘b%’
```

| Symbols |  |
| -------- | ------- |
| % | Rest of the text |
| _ | Single character |

```sql
LIKE '%b%'
-- B in the Middle
LIKE ‘_____y’
-- 5 Spaces followed by 'y'
LIKE ‘b____y’
-- 'b' followed by 4 spaces and 'y' 
```

## Regexp

```sql
SELECT *
FROM customers
WHERE last_name REGEXP ‘field$’
```
| Symbols |  |
| -------- | ------- |
| \| | or/multiples patterns  |
| $ | end |
| ^ | start |
| [] | matches list |
| -| range |

```sql
REGEXP ‘field|mac’
-- Searches field or mac

REGEXP ’^field|mac|rose’
-- Starts with field or is mac or is rose

REGEXP ‘[hcb]at’
--searches hat, cat, bat

REGEXP ‘[a-h]e’
--is a to h with e
--ae,be,ce,de.....
```
## IsNull

```sql
SELECT *
FROM customers
WHERE phone IS NULLL
```
## Order By

```sql
SELECT *
FROM customers
ORDER BY state DESC, first Name DESC
```
```sql
SELECT * state, last_name
FROM customers
ORDER BY 1,2
```
## Between

```sql
DELETE FROM invoices
WHERE invoice_id = (
  SELECT *
  FROM Clients
  WHERE name=’Myworks’)
```
# Joins
## Inner Join

```sql
SELECT *
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
```
```sql
SELECT *
FROM order_items oi
JOIN order_item_notes oin
	ON oi.order_id = oin.order_id
	AND oi.product_id = oin.product_id
```
## Self Join

```sql
SELECT *
FROM employees e
JOIN employees m
	ON e.employee _name= m. manager
```
## Joining Multiple Tables
```sql
SELECT
	o.order_id
	o.order_date,
	c.first_name,
	c.last_name,
	os.name as Status
FROM orders o
JOIN customers c
	ON o.customer_id = c.customer_id
JOIN order_statuse os
	ON o.status = os.order_status_id
```
## Outer Join

```sql
SELECT *
FROM customers c
OUTER JOIN orders o
	ON c.customer_id = o.cusomer_id
ORDER  BY c.customer_id
```

## Left/Roght Join

```sql
SELECT *
FROM orders
LEFT JOIN customers
ON orders.customer_id = customers.customer_id
```
## Using

```sql
SELECT o.order_id,
	c.first_name,
FROM orders o
JOIN customers c
	USING (customer_id)
--same as o.customer_id = c.customer_id

```
## Cross Join

```sql
SELECT
	sh.name
	p.name
FROM shippers sh
CROSS JOIN products p

```
## Unions
Comibination of two or more commands joined by using 'union'
```sql
SELECT
first_name,
‘Active’ as Status
FROM shippers
	WHERE
	order_date >= ‘2019-01-01’ 

UNION

SELECT first_name,
‘Archived’ as Status
FROM shippers
	WHERE
	order_date < ‘2019-01-01’
OREDER BY first_name
``` -->

## Author

### __[Parth Verma](https://github.com/itsparthverma)__

<a href="https://www.linkedin.com/in/itsparthverma"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
<a href="https://letsgoparth.github.io/parthverma.github.io/"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-255E63?style=for-the-badge&logo=About.me&logoColor=white"></a>
<a href="https://www.kaggle.com/letsgoparth"><img alt="Kaggle" src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white"></a>
<a href="mailto:letsgoparth@gmail.com"><img alt="Mail" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a>

Parth Verma is a Computer Application student and a Data Analytics enthusiast from Delhi, India. 


<!-- 
Thanks to for icons https://github.com/alexandresanlim/Badges4-README.md-Profile/tree/master -->
