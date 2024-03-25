
**Title:** ☕️ Interactive Coffee Sales Dashboard (USA, UK, Ireland) ☕️

<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0));">

<h2 style="font-weight: bold; color: #333;">Explore Coffee Sales Across USA, UK, and Ireland</h2>

This Python project showcases the creation of an interactive dashboard for analyzing coffee sales data. It leverages the power of:

<ul style="list-style: none; padding: 0;">
  <li><i class="fas fa-book"></i> **Streamlit:** A framework specifically designed for building user-friendly data applications.</li>
  <li><i class="fas fa-table"></i> **Pandas:** A versatile library for data manipulation and analysis.</li>
  <li><i class="fas fa-chart-line"></i> **Plotly:** A versatile library for creating both static and interactive data visualizations.</li>
</ul>

**Key Functionalities:**

<div style="display: flex; flex-wrap: wrap; gap: 1rem;">
  <div style="width: 50%; padding: 1rem; background-color: rgba(230, 230, 230, 0.2); border-radius: 5px;">
    <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">Data Acquisition and Preparation</h3>
    <p>
      - Leverages pre-cleaned data prepared and exported from Excel (not included in this repository).
      - Defines a function to efficiently read the data from a CSV file.
      - Implements data caching for optimized performance.
    </p>
  </div>
  <div style="width: 50%; padding: 1rem; background-color: rgba(230, 230, 230, 0.2); border-radius: 5px;">
    <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">Data Enhancement and Analysis</h3>
    <p>
      - Introduces random ratings (demonstration purpose only) to enrich the dataset.
      - Applies clear and descriptive column names for readability.
      - Optimizes data types for streamlined processing.
      - Generates a pivot table to uncover sales trends across coffee type, year, and month.
    </p>
  </div>
  <div style="width: 50%; padding: 1rem; background-color: rgba(230, 230, 230, 0.2); border-radius: 5px;">
    <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">Interactive Exploration</h3>
    <p>
      - Provides a user-friendly sidebar with filters for:
        - Country
        - Coffee Type
        - Roast Type
        - Loyalty Card usage
      - Empowers users to delve into the data based on their specific interests.
    </p>
  </div>
  <div style="width: 50%; padding: 1rem; background-color: rgba(230, 230, 230, 0.2); border-radius: 5px;">
    <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">Data Visualization</h3>
    <p>
      - Presents key performance indicators (KPIs):
        - Total Sales
        - Average Rating
        - Average Sales per Transaction
      - Delivers insights through interactive visualizations:
        - Horizontal bar chart effectively depicts sales by coffee type.
        - Line chart visualizes sales trends over time, ensuring clear ordering of months and years.
    </p>
  </div>
</div>

**Live Demo:**

Experience the interactive dashboard in action: Streamlit Dashboard: [https://sales-dashboards.streamlit.app/](https://sales-dashboards.streamlit.app/)

** Note:**

The Excel data preparation and cleaning steps are not included in this repository as they focus on data quality maintenance.

This project demonstrates the practical application of Python libraries for data analysis, visualization, and interactive dashboard creation. Feel free to explore the code, adapt it to
