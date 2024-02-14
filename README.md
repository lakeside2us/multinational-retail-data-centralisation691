# multinational-retail-data-centralisation691

## Table of Contents

1. Project Title
2. Project Description
3. Usage Instructions
4. File Structure of the Project
5. License Information
6. Authors

### Project Title

Multinational Retail Data Centralisation

### Project Description

A multinational company that sells various goods across the globe currently stores its sales data in many different data sources.

As a result of having its sales data spread in many different data sources, it is not easy to access and analyse the sales data.

The company is trying to become more data-driven and therefore wants to make its sales data accessible from one centralised location.

The project aims to produce a system that stores the current company data in a centralised database and access data from this one central database.

After storing the sales data in a centralised database, the database will be quarried to obtain up-to-date metrics for the business.

### Usage Instructions

Make sure you install *pgAdmin 4* on your local computer and create a new database called *sales_data* in pgAdmin 4.

To connect to the various data sources, extract the data, clean the data and upload the data to *sales_data* database in pgAdmin 4, following these steps:

```
# Clone this repository
$ https://github.com/lakeside2us/multinational-retail-data-centralisation691.git

# Run the script to connect, clean and unload data into the database
$ python main.py 
```

### File Structure of the Project

```dotnetcli
1. gitignore
        Stores the files that contain the credentials needed to extract and load the data.

2. database_utils.py
        This defines the DatabaseConnector Class that is used to connect and upload the cleaned data to the sales_data database.

3. data_extraction.py
        This defines the DataExtractor Class that is used to extract all the data from the various data sources used by the company. The class also converts the data into Panda DataFrames for ease of processing, cleaning and human readability.

4. data_cleaning.py
        This defines the DataCleaning Class that is used to clean the data extracted from various sources.

5. main.py
        This is used to extract, clean and upload each DataFrame to sales_data.

6. milestone_3_queries
        This folder contains all queries for milestone 3 tasks.

7. milestone_4_queries
        This folder contains all queries for milestone 4 tasks.

``````



### License Information

This project is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).

### Author

***Name: Olawale Olalekan***

### Acknowledgments

AiCore