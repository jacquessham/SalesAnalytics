# Exploring Features
There are two features that we need to look at to improve model accuracy: Date and Markdown. We don't know whether either features has any effect on making prediction.

## Strategy
We will train 2 models for each feature, each model include or exclude the feature. We will evaluate either model and find which one has a higher accuracy, evaluated by R-square.

## Files and Results
There are two files, each file explore the effect on including or excluding date or all Markdown columns. The results will be saved in Results.
* Train_Store_withDate.py - Train models include or exclude column "Date"
* Train_Store_withoutMarkdown.py - Train models include or exclude "Markdown1-5"
* DateResult.txt in Results folder consists the result from Train_Store_withDate.py
* MarkdonwResult.txt in Results folder consists the result from Train_Store_withoutMarkdown.py
Click [here](/Results) to the Results folder.

## Date
The result from Train_Store_withDate.py is:
* with Date:    82% R-square
* without Date: 83% R-square
As the result, it is better to exclude column "Date".

## Markdowns
The result from Train_Store_without_Markdown.py is:
with Markdowns:    83% R-square
without Markdowns: 85% R-square
As the result, it is better to exclude columns of markdowns.

## Verdict
Based on the result above, we have found that it is better to exclude both "Date" and all markdown columns as part of the features in the prediction model.

## Next Step
The next step is to tune the hyperparameter. Click [here](../Tuning) for the Tuning Folder.