# Instructions

Download the files located [here](https://www.kaggle.com/datasets/jaeyoungkum/google-data-analytics-capstone-cyclistic-data/download?datasetVersionNumber=1)

Unzip the files inside the data folder.

# Misc data

I created a python env for this, with Python 3.10.7

# What it does?

**We assume the following conditions.**

_The data structure from the CSV files, the users have a fixed station name._

Obtain a list the csv files in the data directory.

For each file, call the function csv_content

For each row, if the station_name and stationd_id are valid values, 

I will append them to a list.

Sort the list by name

Create a set by iterating the list (**hint**: _a set does not allow duplicates, 
that's why i use it_)

From that set, obtain a sorted list

Create the final result a dictionary[str: set]
The dictionary will contain the station_name and a set of station_ids, since
the idea was to obtain all the different ids people give to a station

The program will do this for all the files and you will end up
with a list[dictionary[str:set]] of the 12 files (or whatever you have when you download the zip)
