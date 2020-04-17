# A/B Testing Application
In the last phase, exploratory data analysis, we have raised two questions that we are very interested that might be helping us gaining customer's behavior insight to make better business plan. In this phase, we will use A/B testing to answer this question. 

## Goal
We want to use A/B Testing to answer these question:
* Question 1: Is the sales from members more than the sales from non-members?
* Question 2: Is the sales of Health & Beauty from Male more than the sales from Female?
* Once we have answer, the next question is how much we can trust the answer.

## Strategy
First, we will set the hypothesis for each question. In each question, we will manipulate the data and use A/B testing technical to obtain the p-value and decide whether to accept or reject the hypothesis in order to answer the question. Lastly, we will calculate the power to show the probability of Type II error. 

## Files
There are 3 files in this folder:
* abtestingkit.py - Helper code to conduct A/B testing, return p-value, power, and sample size needed to achieve desired power
* Burmasupermarket_abtesting_member.py - Driver program conduct A/B testing on answering Question 1 by calling abtestingkit.py
* Burmasupermarket_abtesting_hbmale.py - Driver program conduct A/B testing on answering Question 2 by calling abtestingkit.py

## A/B Testing Kit
The file of abtestingkit.py is the code of "A/B Testing kit". This is a dynamic program which is able to conduct A/B testing with any kind of data set. Once you have set the hypothesis, you may able to pass the data frame to return the p-value, power, and the sample size needed to achieve 80% power. The code only has one function: abtesting(), which required 5 parameters:
<br>
* df - Data Frame of the data set
* group - Group of partition in the data set
* target - The Feature which is tested in the data set
* diff - The different of the response variable desired to be tested, the parameter's default is 0
* alt - The signs of hypothesis, the available option are: 'equal', 'less than', 'more than'. 'equal' means the difference between A and B are the same in the null hypothesis. 'less than' means A is less than B in the null hypothesis. 'more than' means A is more than B in the null hypothesis.
<br>
The function calculates all the requirements needed in the A/B testing, including sample size, sample means, pooled variance, sample mean difference to calculate p-value and power. It also calculates the sample size needed to achieve 80% power. The function returns a dictionary which contains those results. 
<br>
The testing kit requires Pandas and Scipy (norm and ttest_ind).

## Question 1
Burmasupermarket_abtesting_member.py read the data set and call the the function in A/B Testing kit to receive the p-value of the A/B testing result, as well as the power and the sample size needed to achieve 80% power if the power is less than 80%. 
<br><br>
First, we set the null and alternative hypothesis to answer this question. Then we will run Burmasupermarket_abtesting_member.py to get p-value and power. Once we have the p-value and power, we can evaluate null hypothesis and estimate the type II error.
<br><br>
Question 1 is: Is the sales from members more than the sales from non-members?<br>
H<sub>0</sub>: Sales from members is greater than the sales from non-members, Sales<sub>member</sub> > Sales<sub>Non-member</sub>
<br>
H<sub>A</sub>: Sales from members is less than the sales from non-members, Sales<sub>member</sub> < Sales<sub>Non-member</sub>
<br><br>
If we set the significant value is 0.05. The p-value calculated from the file is 0.26 which is greater than the significant value. Therefore, we do not reject the null hypothesis. We can conclude that the sales from members is more than the sales from non-member. Since the power is 90%, the probability of type II error is 10%.

## Question 2
Burmasupermarket_abtesting_hbmale.py read the data set and call the the function in A/B Testing kit to receive the p-value of the A/B testing result, as well as the power and the sample size needed to achieve 80% power if the power is less than 80%. 
<br><br>
First, we set the null and alternative hypothesis to answer this question. Then we will run Burmasupermarket_abtesting_member.py to get p-value and power. Once we have the p-value and power, we can evaluate null hypothesis and estimate the type II error.
<br><br>
Question 2 is: Is the sales of Health & Beauty from Male more than the sales from Female?<br>
H<sub>0</sub>: Healthy & Beauty sales from male consumers is greater than the healthy & Beauty sales from female consumers, Sales<sub>male,Health & Beauty</sub> > Sales<sub>female,Health & Beauty</sub>
<br>
H<sub>A</sub>: Healthy & Beauty sales from male consumers is less than the sales from non-members, Sales<sub>male,Health & Beauty</sub> < Sales<sub>female,Health & Beauty</sub>
<br><br>
If we set the significant value is 0.05. The p-value calculated from the file is 0.06 which is greater than the significant value. Therefore, we do not reject the null hypothesis. We can conclude that the sales from members is more than the sales from non-member. Since the power is 99%, the probability of type II error is 1%.

## Reference
<a href="https://towardsdatascience.com/understanding-power-analysis-in-ab-testing-14808e8a1554">Power</a>
<br>
<a href="https://medium.com/@henryfeng/handy-functions-for-a-b-testing-in-python-f6fdff892a90">A/B Testing Python Code</a>
<br>
<a href="https://stackoverflow.com/questions/15984221/how-to-perform-two-sample-one-tailed-t-test-with-numpy-scipy">One-tailed t-test with scipy ttest_ind</a>
<br>
<a href="https://stats.stackexchange.com/questions/12900/when-is-r-squared-negative">Negative R-squared</a>