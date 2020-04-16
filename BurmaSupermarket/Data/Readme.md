# Data
The data is obtained from <a href="https://www.kaggle.com/aungpyaeap/supermarket-sales">Kaggle</a>. The data set is a selective data from a supermarket chain in Burma.


## Features
There are the features of this data set:
<ul>
	<li>InvoiceID</li>
	<li>Branch</li>
	<li>City</li>
	<li>CustomerType</li>
	<li>Gender</li>
	<li>ProductLine</li>
	<li>UnitPrice</li>
	<li>Quantity</li>
	<li>Tax5%</li>
	<li>Total</li>
	<li>Date</li>
	<li>Time</li>
	<li>Payment</li>
	<li>Cogs</li>
	<li>GrossMargin</li>
	<li>GrossIncome</li>
	<li>Rating</li>
</ul>
There are 1000 rows of transactions. The data is roughly balance by city, gender, customer type, product line, and payment type. The data set is small across 3 months to captures all the features.
<br><br>
There are some notes about the features:
* Column "Branch" is the label for "City", both columns are the same
* Each invoice records the purchase of the same product, the total is unitprice times quantity
* Some columns are wrongly labeled, such as Cogs
<br><br>
Some features are wrongly labeled or not useful:
<br>
1. Cogs - This column is supposed to be Grand Total. If you take this column times 1.05, the number equals to Total. So this number is supposed to be the grand total of the transaction before tax.<br>
2. GrossIncome - This column is identical to Tax5%, so this is not really gross income the supermarket collected. <br>
3. GrossMargin - This column takes Tax5% divided by Total, so this is not really the gross margin per transaction for supermarket. <br>
4. Branch - This column is a label for City, basically it functions identical to City. If you select City, it is not helpful to also pick Branch. 
<br><br>
Note that the data set does not have all transactions on every hour per branch. For example, on January 01, 2019 for Mandalay, there is only 3 transactions at 11:36am, 7:07pm, and 7:37pm. It shows that the data set is a selective data set of the original data set.
