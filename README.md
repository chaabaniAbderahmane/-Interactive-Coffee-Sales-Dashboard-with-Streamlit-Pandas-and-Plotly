# -Interactive-Coffee-Sales-Dashboard-with-Streamlit-Pandas-and-Plotly


This code creates an interactive dashboard for analyzing coffee sales data in usa , uk and ireland using the Streamlit framework, Pandas for data manipulation, and Plotly for data visualization. The data was initially prepared and cleaned using Excel before being utilized in this application. The primary functionalities of the code are:

-Importing necessary libraries: pandas, plotly.express, streamlit, random, and plotly.graph_objects.
-Setting up the Streamlit app configuration, including the page title, icon, and layout.
-Defining a function to read data from an Excel file (after data preparation and cleaning in Excel) and caching the data for efficient processing.
-Adding random ratings to the dataset for demonstration purposes.
-Renaming columns and converting data types for better readability and processing.
-Creating a pivot table to analyze sales by coffee type, year, and month.
-Building a sidebar with filters for country, coffee type, roast type, and loyalty card, allowing users to interactively filter the data.
-Displaying key performance indicators (KPIs) such as total sales, average rating, and average sales per transaction.
-Visualizing sales by coffee type using a horizontal bar chart.
-Creating a line chart to display sales over time by coffee type, with chronological ordering of months and years.

[Streamlit Dashboard](https://sales-dashboards.streamlit.app/)
