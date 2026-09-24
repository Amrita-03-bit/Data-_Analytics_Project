-- @conn  Banking Risk MySQL 

-- 7. Find the earliest loan date.

SELECT loan_date AS earliest_loan_date FROM loans ORDER BY earliest_loan_date ASC LIMIT 1; 

-- 8. Find the latest loan date.

SELECT loan_date AS latest_loan_date FROM loans ORDER BY latest_loan_date DESC LIMIT 1; 

-- 11. Display customer name, city, occupation, annual income, and credit score.

SELECT customer_name,city,occupation,annual_income,credit_score FROM customers;

-- 12. Display customer name, loan ID, loan type, loan amount, and loan status.

SELECT customers.customer_name,loans.loan_id,loans.loan_type,loans.loan_amount,loans.loan_status FROM customers INNER JOIN loans ON customers.customer_id=loans.customer_id;

-- 21. Find customers with credit scores below a defined risk threshol

SELECT customer_name FROM customers WHERE credit_score<650;

-- 22. Find customers with high annual income but low credit scores.
SELECT customer_name, annual_income, credit_score FROM customers WHERE annual_income > (SELECT AVG(annual_income) FROM customers) AND credit_score < (SELECT AVG(credit_score) FROM customers);

-- 31. Calculate the total amount paid across all loans.

SELECT sum(loans.loan_amount) AS total_amount_paid FROM  loans INNER JOIN payments ON loans.loan_id=payments.loan_id WHERE payment_status="paid";

-- 32. Count successful payments.

SELECT COUNT(payment_status)FROM payments WHERE payment_status="paid" ;

-- 33. Count late payments.

SELECT COUNT(payment_status)FROM payments WHERE payment_status="late" ;

-- 34. Count missed payments.

SELECT COUNT(payment_status)FROM payments WHERE payment_status="missed" ;

-- 35. Find loans with late or missed payments.

SELECT loans.loan_amount,payments.payment_status FROM loans INNER JOIN payments ON loans.loan_id=payments.loan_id WHERE payment_status="late" OR payment_status="missed";

-- 39. Find the latest payment date for each loan.

SELECT loan_id  AS loan, MAX(payment_date) AS latest_date FROM payments GROUP BY loan ORDER BY loan  ;

-- 48. Rank branches by total loan value.

SELECT branches.branch_name,SUM(loans.loan_amount),RANK() OVER (ORDER BY sum(loans.loan_amount)   DESC) FROM loans INNER JOIN loan_branches ON loans.loan_id=loan_branches.loan_id INNER JOIN branches ON branches.branch_id=loan_branches.branch_id GROUP BY branches.branch_name;

-- 49. Rank customers by total loan amount.

SELECT customers.customer_name,SUM(loans.loan_amount),RANK() OVER (ORDER BY sum(loans.loan_amount) DESC) from customers INNER JOIN loans ON customers.customer_id=loans.customer_id GROUP BY customers.customer_name;

-- 50. Rank loan types by total loan value.

SELECT loan_type,SUM(loan_amount),RANK() OVER(ORDER BY sum(loan_amount)DESC) FROM loans GROUP BY loan_type;

-- 52. Find the top 3 customers by total loan amount.

SELECT customers.customer_name,SUM(loans.loan_amount) FROM customers INNER JOIN loans on customers.customer_id=loans.customer_id  GROUP BY customers.customer_id,customers.customer_name ORDER BY SUM(loans.loan_amount) DESC LIMIT 3;

-- 53. Find the top 3 loans by loan amount.

SELECT loan_id,loan_amount FROM loans ORDER BY loan_amount DESC LIMIT 3;

-- 54. Find each customer's first loan date.

SELECT customers.customer_name,MIN(loans.loan_date) FROM customers INNER JOIN loans ON customers.customer_id=loans.customer_id GROUP BY customers.customer_name   ;

-- 55. Find each customer's latest loan date.

SELECT customers.customer_name,MAX(loans.loan_date) FROM customers INNER JOIN loans ON customers.customer_id=loans.customer_id GROUP BY customers.customer_name   ;

-- 56. Find the latest payment for each loan.

SELECT loans.loan_id,MAX(payments.payment_date) FROM loans INNER JOIN  payments ON loans.loan_id=payments.loan_id GROUP BY loans.loan_id;

-- 57. Calculate a running total of loan amounts.

SELECT loan_id,SUM(loan_amount) OVER(ORDER BY loan_id )FROM loans;

-- 58. Compare each customer's loan amount with the overall average.

SELECT customers.customer_name,loans.loan_amount,AVG(loans.loan_amount) OVER() FROM customers INNER JOIN loans ON customers.customer_id=loans.customer_id ;