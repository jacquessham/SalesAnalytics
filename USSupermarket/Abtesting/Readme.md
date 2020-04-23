# A/B Testing Application
In this phase, we will use A/B testing to answer some questions to find some business insights. 

## Background
When I look at the customer data set, I would like to learn more about the relationship between customers and spending score. The first question is does high income has a relationship with high spending score? If this is true, it means the supermarket attracts high-income customers; if this is false, it means the supermarket attracts low-income customers. The supermarket chain may use this infomation to target its strategic customers. Second, do both gender have the same spending score? The supermarket chain may use this information to allocate advertisement resource and procurement strategy.

## Questions
1. Question 1: Do high-income customers have higher spending score?
2. Question 2: Do both male and female customers have the same spending score?

## Strategy
First, we will set the hypothesis for each question. In each question, we will manipulate the data and use A/B testing technical to obtain the p-value and decide whether to accept or reject the hypothesis in order to answer the question. Lastly, we will calculate the power to show the probability of Type II error. 

## Files
There are 2 python and 2 result files in this folder:
* abtestingkit.py - Helper code to conduct A/B testing, return p-value, power, and sample size needed to achieve desired power. This is the same file in Part 1 A/B Testing
* ussupermarket_abtesting_Y.py - Driver program conduct A/B Testing on answering Question 1 and Question 2 by calling abtestingkit.py
* case1result.txt - Result of Question 1
* case2result.txt - Result of Question 2

## A/B Testing Kit
The file of abtestingkit.py is the code of "A/B Testing kit". This is a dynamic program which is able to conduct A/B testing with any kind of data set. Once you have set the hypothesis, you may able to pass the data frame to return the p-value, power, and the sample size needed to achieve 80% power. The code only has 2 function: abtesting(), and savefile(). abtesting() required 5 parameters:
* df - Data Frame of the data set
* group - Group of partition in the data set
* target - The Feature which is tested in the data set
* diff - The different of the response variable desired to be tested, the parameter's default is 0
* alt - The signs of hypothesis, the available option are: 'equal', 'less than', 'more than'. 'equal' means the difference between A and B are the same in the null hypothesis. 'less than' means A is less than B in the null hypothesis. 'more than' means A is more than B in the null hypothesis.
<br><br>
The function calculates all the requirements needed in the A/B testing, including sample size, sample means, pooled variance, sample mean difference to calculate p-value and power. It also calculates the sample size needed to achieve 80% power. The function returns a dictionary which contains those results.
The testing kit requires Pandas and Scipy (norm and ttest_ind).
<br><br>
savefile() required 2 parameters:
* result - Result in dictionary returned from abtesting()
* filepath - file path to save the file
<br><br> This code is the same code in [Part 1](../../BurmaSupermarket/ABtesting)

## Question 1
ussupermarket_abtesting_Y.py read the customer data set and call the the function in A/B Testing kit to receive the p-value of the A/B testing result, as well as the power and the sample size needed to achieve 80% power if the power is less than 80%.
<br><br>
The data set did not split the customers into low or high income customers. In a naive idea, we split the customers available in the data set into half and split each partition to low and high customers. Therefore, the code would find the median of customer and add one new column which classify whether the customer is low or high income customer. 
<br><br>
First, we set the null and alternative hypothesis to answer this question. Then we will run ussupermarket_abtesting_Y.py to get p-value and power. Once we have the p-value and power, we can evaluate null hypothesis and estimate the type II error.
<br><br>
Question 1: Do high-income customers have higher spending score?<br><br>
H<sub>0</sub>: High-income customers have higher spending score, Spenind Score<sub>High-income</sub> > Sales<sub>Low-Income</sub>, High-Income customers have higher satification
<br>
H<sub>A</sub>: High-income customers have lower spending score, Spenind Score<sub>High-income</sub> < Spenind Score<sub>Low-Income</sub>, Low-Income customers have higher satification
<br><br>
If we set the significant value is 0.05. The p-value calculated from the file is 0.44 which is greater than the significant value. Therefore, we do not reject the null hypothesis. We can conclude that high-income customers have higher spending score. Since the power is 98%, the probability of type II error is 2%.
<br><br>
As the result, we may expect this supermarket chain attracts high-income customer because we concluded that high-income customers have higher spending score than low-income customers' spending score. The supermarket chain may allocate more resource to marketing resource to high-income customers and sell more high-end products.

## Question 2
The same file, ussupermarket_abtesting_Y.py read the customer data set and call the the function in A/B Testing kit to receive the p-value of the A/B testing result, as well as the power and the sample size needed to achieve 80% power if the power is less than 80%. 
<br><br>
First, we set the null and alternative hypothesis to answer this question. Then we will run ussupermarket_abtesting_Y.py to get p-value and power. Once we have the p-value and power, we can evaluate null hypothesis and estimate the type II error.
<br><br>
I believe grocery is essential products to the customers, regardless of gender. I would like to verify whether both male and female customers have the same spending score. If the spending score of either gender is higher, it means the supermarket chain sells more products or provide services preferred by one of the genders.
<br><br>
Question 2: Do both male and female customers have the same spending score?<br><br>
H<sub>0</sub>: Male and Female customers have the same spending score, Spenind Score<sub>Male</sub> = Sales<sub>Female</sub>
<br>
H<sub>A</sub>: Male and Female customers have different spending score, Spenind Score<sub>Male</sub> ≠ Spenind Score<sub>Female</sub>
<br><br>
If we set the significant value is 0.05. The p-value calculated from the file is 0.41 which is greater than the significant value. Therefore, we do not reject the null hypothesis. We can conclude that high-income customers have higher spending score. Since the power is 87%, the probability of type II error is 13%.
<br><br>
As the result, we expect male and female have the same spending score. It means the satification of male and female customers are the same that the supermarket chain do not need to take gender as a feature on any advertisement campaign or any strategic planning.

## Conclusion
After we have conducted A/B testing on Question 1 and Question. We have found that:
* Higher income customers have higher spending score
* The supermarket chain is more welcomed by high income customers than low income customers do.
* Male and female customers have the same spending score
* The supermarket chain is preferred by either gender equally

## Next Step
In the next step, we will interpret the spending effect to profit. You may find the analysis in the Interpretation phase [here](../Interpretation)