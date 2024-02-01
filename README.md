# Objectives

This project is designed to evaluate the following concepts:

- Ability to use Apache Airflow
- Ability to perform data validation using Great Expectations
- Comprehensive understanding of NoSQL concepts
- Ability to prepare data for use before entering a NoSQL database
- Ability to process and visualize data using Kibana

---

# Data Sources
The dataset is obtained from the following repository:

- [Kaggle datasets](https://www.kaggle.com/code/akshitmadan/complete-data-analysis-supermarket-dataset/input)

# Problems

Create a report containing Exploratory Data Analysis (EDA) of the dataset.

The dataset, named `data_raw.csv`, undergoes Data Cleaning and data validation using Great Expectation. All processes are executed through a pipeline using Apache Airflow. The following steps are taken:

1. The dataset is named `data_raw.csv`.

2. Data is inserted into local PostgreSQL and given a table name to store the data, named `table_m3`.

3. After the data is in the database, retrieve all data from the database using Python and perform several Data Cleaning steps using Python:
   - Remove duplicate data.
   - Normalize columns by:
     + Converting all column names to lowercase. Example: `ID` → `id`, `EDUCATION` → `education`, `Age` → `age`.
     + Changing data types.

4. After Data Cleaning, save the cleaned data to a CSV file named `data_clean.csv`.

5. Create a Python Notebook (`data_GX.ipynb`) to validate the data using Great Expectations. The chosen Expectation criteria include:
   - 7 Expectations, which include Expectations for:
     + to be unique
     + to be between min_value and max_value
     + to be contain in column
     + to be in type list
     + to be match strftime format
     + to be in set

   - All seven Expectations used return `success: true`.

6. In addition to saving it to a CSV file as in point 4, the cleaned data is also inserted into Elasticsearch using Python.

7. Automation is achieved by creating a DAG with the following criteria:
   - The DAG contains 3 nodes/tasks:
     + `Fetch from PostgreSQL`: contains a script to retrieve data from PostgreSQL.
     + `Data Cleaning`: contains a script to perform Data Cleaning and save it to a CSV file.
     + `Post to Elasticsearch`: contains a script to load the CSV containing cleaned data and insert it into Elasticsearch.
   - Scheduling is done every day at 06:30.
   - The DAG file is named `DAG.py`.

8. Create a Kibana dashboard for this cleaned data with the following specifications:
   - Exploratory Data Analysis is related to:
     * The background of the report
     * The objectives to be achieved
     * The division/team in need
     * Etc.
   - There are 6 visualizations for the data that support the achievement of the objectives of the EDA process. The 6 visualizations use plots such as:
     * 1 Bar Plot
     * 1 Pie Chart
     * 1 Vertical Bar Plot
     * 1 Word Cloud
     * 1 Table
     * 1 Line Chart

    - 1 visualization in `Markdown` format that contains:
     + Conclusions from the exploration.
     + Further suggestions or business insights based on the exploration.
     + The conclusions include recommendations regarding the objectives determined based on a combination of the exploration results and an external reference (such as theory in a domain, statements from an expert, competitor facts, etc.) so that the recommendations are targeted and reasonable.
   - Total visualizations: 6 visualizations + 1 Markdown visualization for conclusions = 7 visualizations.

---

## Conceptual Problems

1. Explain what is meant by NoSQL using your understanding!

2. Explain when to use NoSQL and Relational Database Management System!

3. Mention 2 examples of NoSQL tools/platforms other than Elasticsearch, along with the advantages of these tools/platforms!

4. Explain what you understand from Airflow in your own words!

5. Explain what you understand from Great Expectations in your own words!

6. Explain what you understand from Batch Processing in your own words (Definition, Use Case Examples, Tools, etc.)!