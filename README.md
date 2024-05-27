# Airbnb_Data_Analysis_and_Visualization

A Streamlit dashboard has been created where user can access the various Airbnb listings and use filters to refine the search. A Geo Visualization map has been added to the dashboard based on the listings. Furthermore, data pre-processing and EDA has been performed and data has been visualized on Power BI based on various features.

**Introduction**

Airbnb sample data is available on Mongo DB Atlas and can be extracted for further analysis and visualization. The data here is provided as a Json file using which the necessary data is extracted to build a Airbnb Dahborad on Streamlit and the data is used for Visualization on Power BI.

As the data is not an updated one, search based on availability could not be performed.

**User Guide**

1. Airbnb dashboard created works based on several search filters provided. User can refine the search by providing the destination, property type, price, rating, number of occupants and number of bedroom.

2. Properties that match the search criteria are listed and user can view details of it by providing the property number (Index of the table) in the input filed provided. Host details can also be viewed further.
  
3. A Geo visualization has also been provided for easy selection of data based on the location.

**Developer Guide**

**1.Tools required**

  • Python

  • Visual Studio Code

  • Power BI

**2.Python libraries to install**
  **a.For dashboard creation**
    • Pandas

    • Json

    • Numpy

    • Streamlit

    •  Pydeck

  **b.For Analysis**

    • matplotlib.pyplot

    • Seaborn

    • scipy.stats

    • Numpy

    • Json

    • Pandas

**3. Modules to import**

  a. File handling Libraries

    • import json

  b. Pandas Library

    • import pandas

  c. Numerical calculatoins Library

    • import numpy as np

    • from scipy.stats import skew

  d. Visualization Libraries

    • import matplotlib.pyplot as plt

    • import seaborn as sns

  e. Dashboard Libraries

    • import streamlit as st

    • import pydeck as pdk

**4.Process**

  • Airbnb data can be extracted from Mongo DB Atlas after signing in

  • Here, the json file containing the extracted data has been provided

  • Necessary data are collected from the json file and stored in different dataframes

  • Data is pre processed by removing the duplicates, filling the null values and altering the data types of columns wherever necessary

  • Exploratory Data Analysis has been conducted on the price feature where the statistical central tendency measure, range, skewness etc. has been calculated

  • Univariate analysis has been performed on the Price feature
  
  • Bivariate and Mutivariate analysis has been performed on price, number of bedrooms and number of accommodates features for various countries

  • A streamit dashboard is created where user can drill down the data using the selective search options provided and refine the property listing based on the search criteria

  • Pandas is effectively used for conditional querying and display of data

  • Search criteria provided - Destination, property type, price, ratings, number of bedrooms and number of accomodates

  • A detailed view of the property that the user wants to take a look at is provided, where in details like location, description of the property, amenities, host details, ratings, reviews etc. are displayed

  • A geo visualzation of the refined listings is provided so that users can locate them on the map with ease

  • Power BI dashboard is created where visualizations of the data based on different features are displayed

  • Different csv files are created from the dataframes available and is uploaded to Power BI as data

  **NOTE:**

  • The airbnb_analysis.ipynb file contains the code for data extraction, pre processing and EDA. 
    
  • The dasboard.py file consists of the code for Streamlit dashboard creation and geo visualization. 
    
  • While, airbnb visualization.pbix (Power BI file) shows visualizations and insights based on the data.
