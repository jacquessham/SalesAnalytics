# Sales Analytics of Burma Supermarkets

This is one part of the Sales Analytics Project. The data set is a selective data set on supermarket transactions in 3 different supermarkets in Burma. The goal of this part is to find interesting data insight and make prediction models.

## Data

The data is obtained from <a href="https://www.kaggle.com/aungpyaeap/supermarket-sales">Kaggle</a>.
<br>
There are the features of this data set:
<ul>
	<li></li>
</ul>
There are 1000 rows of transactions. The data is roughly balance by city, gender, customer type, product line, and payment type. The data set is small across 3 months to captures all the features.
<br><br>
Some features are wrongly labeled or not useful:
<br>
1. Cogs - This column is supposed to be Grand Total. If you take this column times 1.05, the number equals to Total. So this number is supposed to be the grand total of the transaction before tax.<br>
2. GrossIncome - This column is identical to Tax5%, so this is not really gross income the supermarket collected. <br>
3. GrossMargin - This column takes Tax5% divided by Total, so this is not really the gross margin per transaction for supermarket. <br>
4. Branch - This column is a label for City, basically it functions identical to City.
<br><br>
Note that the data set does not have all transactions on every hour per branch. For example, on January 01, 2019 for Mandalay, there is only 3 transactions at 11:36am, 7:07pm, and 7:37pm. It shows that the data set is a selective data set of the original data set.

## Data Exploration

EDA (Organizating)

## A/B Testing

(Organizating)

Reference:
<br>
<a href="https://towardsdatascience.com/understanding-power-analysis-in-ab-testing-14808e8a1554">Power</a>
<br>
<a href="https://medium.com/@henryfeng/handy-functions-for-a-b-testing-in-python-f6fdff892a90">A/B Testing Python Code</a>
<br>
<a href="https://stackoverflow.com/questions/15984221/how-to-perform-two-sample-one-tailed-t-test-with-numpy-scipy">One-tailed t-test with scipy ttest_ind</a>
<br>
<a href="https://stats.stackexchange.com/questions/12900/when-is-r-squared-negative">Negative R-squared</a>


## Prediction Model

Logistic Regression, SVC, decision tree, time-series. (Organizating)

## Thought

(Organizating)