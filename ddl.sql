/*
==================================================================================================

URL Dataset : https://www.kaggle.com/code/akshitmadan/complete-data-analysis-supermarket-dataset

This file contains commands to create a table and insert data into the table.

==================================================================================================
*/

BEGIN;

DROP TABLE IF EXISTS table_m3 CASCADE;

COMMIT;

BEGIN;

-- Create table
CREATE TABLE IF NOT EXISTS table_m3 (
    invoice_id VARCHAR(255) PRIMARY KEY,
    branch VARCHAR(255), 
    city VARCHAR(255), 
    customer_type VARCHAR(255), 
    gender VARCHAR(255), 
    product_line VARCHAR(255), 
    unit_price VARCHAR(255),
    quantity VARCHAR(255), 
    tax_5 VARCHAR(255), 
    total VARCHAR(255), 
    date VARCHAR(255),
    time VARCHAR(255), 
    payment VARCHAR(255), 
    cogs VARCHAR(255), 
    gross_margin_percentage VARCHAR(255),
    gross_income VARCHAR(255),
    rating VARCHAR(255)
);

COMMIT;

BEGIN;

-- Import the csv file into the table
COPY table_m3 
FROM '/files/maudy_raw.csv' 
DELIMITER ','
CSV HEADER;

COMMIT;