import pandas as pd
import plotly.express as px
import streamlit as st
import random  
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Set page configuration
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# Function to get data from Excel
@st.cache_data
def get_data_from_excel():
    # Specify the full path to the Excel file
    excel_file_path = r"coffee.xlsx"

    # Read the Excel file
    df = pd.read_excel(
        io=excel_file_path,
        engine="openpyxl",
        sheet_name="orders",
        skiprows=0,
        usecols="A:P",
        nrows=1001,
    )

    return df  # Add this line to return the DataFrame

# Get data from Excel
df = get_data_from_excel()


# Générer une liste de valeurs aléatoires entre 0.0 et 10.0 avec la même longueur que df_selection
random_ratings = [round(random.uniform(0.0, 10.0), 2) for _ in range(len(df))]

# Ajouter la nouvelle colonne "Rating" au DataFrame
df['Rating'] = random_ratings

df = df.rename(columns={'Coffee Type': 'coffee_type', 'Roast Type': 'roast_type',
                        'Coffee Type Name': 'coffee_type_name', 'Roast Type Name': 'roast_type_name', 'Loyalty Card': 'loyalty_card'})

# Convert 'Order Date' to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract year and month
df['Years'] = df['Order Date'].dt.year
df['Months'] = df['Order Date'].dt.month_name()

# Create the pivot table
pivot_table = pd.pivot_table(df, values='Sales', 
                             index=['Years', 'Months'], 
                             columns='coffee_type_name', 
                             aggfunc='sum', 
                             fill_value=0)

# Display the pivot table
print(pivot_table)
# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
Country = st.sidebar.multiselect(
    "Select the Country:",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

coffee_type_name = st.sidebar.multiselect(
    "Select the Coffee Type:",
    options=df["coffee_type_name"].unique(),
    default=df["coffee_type_name"].unique(),
)

roast_type_name = st.sidebar.multiselect(
    "Select the Roast Type:",
    options=df["roast_type_name"].unique(),
    default=df["roast_type_name"].unique()
)

loyalty_card = st.sidebar.multiselect(
    "Select the Loyalty Card:",
    options=df["loyalty_card"].unique(),
    default=df["loyalty_card"].unique()
)




# Filtrer les données pour avoir exactement 1000 lignes
df_selection = df.query(
    "Country == @Country & coffee_type_name == @coffee_type_name & roast_type_name == @roast_type_name & loyalty_card == @loyalty_card"
)


st.dataframe(df_selection)

# ---- MAINPAGE -----

st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPI's

total_sales = int(df_selection["Sales"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int (round(average_rating ,0))
average_sale_by_transaction =  round(df_selection["Sales"].mean(),2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("""---""")



# Sales by Coffee Type [BAR CHART]

sales_by_coffee_type = df.groupby(by=["coffee_type_name"])[["Sales"]].sum().sort_values(by="Sales")
fig_coffee_sales = px.bar(
    sales_by_coffee_type,
    x="Sales",
    y=sales_by_coffee_type.index,
    orientation="h",
    title="<b> Sales by Coffee Type </b>",
    color_discrete_sequence=["#0083B8"] * len(coffee_type_name),
    template="plotly_white",
)
fig_coffee_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

st.plotly_chart(fig_coffee_sales)



#PIVOT TABLE 


# Convert 'Order Date' to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract year and month
df['Years'] = df['Order Date'].dt.year
df['Months'] = df['Order Date'].dt.month_name()

# Define the custom order for months
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Create a categorical data type with custom order
cat_dtype = pd.CategoricalDtype(categories=month_order, ordered=True)
df['Months'] = df['Months'].astype(cat_dtype)

# Create the pivot table
pivot_table = pd.pivot_table(df, values='Sales', 
                             index=['Years', 'Months'], 
                             columns='coffee_type_name', 
                             aggfunc='sum', 
                             fill_value=0)

# Sort the DataFrame by 'Months' and 'Years'
pivot_table = pivot_table.sort_values(by=['Years', 'Months'], ascending=[True, True])

# Display the sorted pivot table
print(pivot_table)



# Reset the index to make 'Years' and 'Months' regular columns
pivot_table_reset = pivot_table.reset_index()

# Convert 'Years' and 'Months' to strings
pivot_table_reset['Years'] = pivot_table_reset['Years'].astype(str)
pivot_table_reset['Months'] = pivot_table_reset['Months'].astype(str)

# Melt the DataFrame to create the necessary structure for the line chart
melted_df = pd.melt(pivot_table_reset, id_vars=['Years', 'Months'], var_name='coffee_type_name', value_name='Sales')
# Concatenate 'Years' and 'Months' columns
melted_df['Years_Months'] = melted_df['Years'] + ' ' + melted_df['Months']

# Order the concatenated column chronologically
month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
melted_df['Months'] = pd.Categorical(melted_df['Months'], categories=month_order, ordered=True)
melted_df = melted_df.sort_values(by=['Years', 'Months'])

# Create a line chart
fig_line_chart = px.line(melted_df, x='Years_Months', y='Sales', color='coffee_type_name',
                         title="Sales Over Time by Coffee Type",
                         labels={"Sales": "Total Sales", "Years_Months": "Years and Months"})

# Update the layout for better visualization
fig_line_chart.update_layout(
    xaxis_title="Years and Months",
    yaxis_title="Total Sales",
    template="plotly_white"
)

# Display the line chart using Streamlit
st.plotly_chart(fig_line_chart)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)