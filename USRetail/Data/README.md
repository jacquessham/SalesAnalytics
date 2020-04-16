# Data
The data comes from "Retail Data Analytics" from <a href="https://www.kaggle.com/manjeetsingh/retaildataset">Kaggle</a>. The data sets are now saved in 3 csv files. There are 45 stores from different regions in the US and each store contains numbers of departments. In here, there are 3 folders of data - Original, Refined, and Engineered.

## The Original files
The files originate from Kaggle that have not done any data cleansing are saved in the "Original" folder.<br>
1. Features dataset/Macro data [features_dataset.csv](/Original/features_dataset.csv)
* Columns:
** Store - Label for the store
** Date - The date of week, format: dd/mm/yyyy
** Temperature - The average temperature in Fehrenheit of the week in the region where the store is located
** Fuel_Price - The gasoline price in the region where the store is located
** MarkDown1-5 - Annoymized data related to promotion. The data is only available in 2011 but not available for all store, there are a lot of NA data in these columns
** CPI - Consumer Price Index
** Unemployment - Unemployment rate in percentage point
** IsHoliday - Whether the week is a special holiday week, boolean type
* The date range of this file is between 2010 and mid-2013, note that sales dataset
* I call this data set as "Macro data" because the features in this data set describes the macro-view of the store

2. Sales dataset [sales_dataset.csv](Original/sales_dataset.csv)
* Columns:
** Store - Label for the store
** Dept - Label for the department in a given store
** Date - The date of week, format: dd/mm/yyyy
** Weekly_Sales - Sales for the given department of a given store
** IsHoliday - Whether the week is a special holiday week, boolean type
* The date range of this file is between 2010 and 2012

3. Store dataset [stores_dataset.csv](Original/stores_dataset.csv)
* The meta data of the given 45 stores of this retail chain
* Column "Type" consists of A,B,C, each type is determined by the size in Column "Size"

## The Refined files
There are two files in this folder.
1. Features dataset/Macro data [features_dataset_refined.csv](Refined/features_dataset_refined.csv)
* The Original features data set consists a lot of NA in various columns
* Using [Refine_datafeatures.py](../DataEngineering/Refine_datafeatures.py) to fill the NA's. Find more infomation in the [DataEngineering Folder](../DataEngineering)
* NA's MarkDown1-5 fills 0, NA's in Temperature, Fuel_Price, CPI, Unemployment fills with previous period data due to time-series relationship
2. Holiday data [IsHoliday.csv](Refined/IsHoliday.csv)
* The data set determine which week is a special holiday
* It is determined by the week of the year based on previous holiday pattern
* Using [Refine_datafeatures.py](../DataEngineering/Refine_datafeatures.py) to find the pattern. Find more infomation in the [DataEngineering Folder](../DataEngineering)

## The Engineered files
There is one file which merge feature data and sales data, [sales_combined.csv](/Engineered/sales_combined.csv).
