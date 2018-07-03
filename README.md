![martha](https://user-images.githubusercontent.com/18128531/38394881-8b12db68-3973-11e8-93f5-145701744ca9.png)

[![CircleCI](https://circleci.com/gh/mitchelllisle/martha.svg?style=svg)](https://circleci.com/gh/mitchelllisle/martha)
[![codecov](https://codecov.io/gh/mitchelllisle/martha/branch/master/graph/badge.svg)](https://codecov.io/gh/mitchelllisle/martha)
![Status](https://img.shields.io/badge/status-alpha-red.svg)

## Installation
```bash
pip install git+https://github.com/mitchelllisle/martha
```
## Upgrade
```bash
pip install --upgrade git+https://github.com/mitchelllisle/martha
```

# What is Martha?
Martha is a python package that aims to assit in both an exploratory data analysis context as well as a productionised python project. There are a few main areas that Martha aims to assist with:

## Summaries ☀️
Often times I find myself needing to get some information about a dataset before diving into an analysis. Although there are some great existing tools within Pandas and other packages, I couldn't find something that quite tells me all the information I needed. Summaries are meant to help bridge this gap.

The functions found in summaries are:

### Distribution
```python
martha.distribution(data, column)
```
This functions works off categorical datam although you can use it on any type. It will return the frequency and percentage of data points that fit to each distinct category. Useful for understanding if your data is distributed across multiple values or if there is some skew to the data.

**Example**
Suppose you have a dataset that looks like the following:

| Movie                   	| Distributor          	| BoxOffice    	| Budget      	|
|-------------------------	|----------------------	|--------------	|-------------	|
| Raiders of the Lost Ark 	| Lucasfilm            	| $225,686,079 	| $20,000,000 	|
| Back to the Future      	| Amblin Entertainment 	| $212,259,762 	| $19,000,000 	|
| Star Wars               	| Lucasfilm            	| $460,998,007 	| $11,000,000 	|

Running 
```python
martha.distribution(movies['Movie'])
```
Would give you:
```
                           occurences	percent
Raiders of the Lost Ark	   1	2.10    %33.33
Back to the Future         1	2.10    %33.33
Star Wars: A New Hope      1	2.10	  %33.33
```


### Column Stats
```python
martha.columnStats(data)
```
This function will provide a summary of the types, counts, uniques and missing values in a column to asset the quality of dataset.


## Quality Assurance 🧐 

### Missing Dates

```python
martha.missingDates(data, freq, format, returnType)
```
Missing Dates are not always easy to spot in a dataset with a number of dates. This function will date the data you pass and generate a series of complete dates using a period, and format that you specify. It will then match these dates with the ones provided and highlight any missing dates.
