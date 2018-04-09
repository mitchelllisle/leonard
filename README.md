![martha](https://user-images.githubusercontent.com/18128531/38394881-8b12db68-3973-11e8-93f5-145701744ca9.png)

[![CircleCI](https://circleci.com/gh/mitchelllisle/martha.svg?style=svg)](https://circleci.com/gh/mitchelllisle/martha)
[![codecov](https://codecov.io/gh/mitchelllisle/martha/branch/master/graph/badge.svg)](https://codecov.io/gh/mitchelllisle/martha)
[![GitHub release](https://img.shields.io/github/release/mitchelllisle/martha.svg)](https://GitHub.com/mitchelllisle/martha/releases/)
![GitHub issues](https://img.shields.io/github/issues/mitchelllisle/martha.svg)
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
Martha can be seen as a 'Quality of Life' python package that aims to assit in both an exploratory data analysis context as well as a productionised python project. There are a few main areas that Martha aims to assist with:

## Summaries
Often times I find myself needing to get some information about a dataset before diving into an analysis. Although there are some great existing tools within Pandas and other packages, I couldn't find something that quite tells me all the information I needed. Summaries are meant to bridge this gap.

The functions found in summaries are:

### Distribution
```python
martha.distribution(data, column)
```
This functions works off categorical data. It will return the frequency and percentage of data points that fit to each distinct category.

**Example**


### Interquartile Range
```python
martha.IQR(data, column)
```
This function returms the Interquartile range of a dataset. Useful for understand where the middle 50% of observations lie.

### Column Stats
```python
martha.columnStats(data)
```
This function will provide a summary of the types, counts, uniques and missing values in a column to asset the quality of dataset.


## Transformations

## Pre-Processing
