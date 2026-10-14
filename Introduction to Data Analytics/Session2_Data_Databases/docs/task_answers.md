# Session 2 — Data & Databases: Task Answers

## Task 1 — CSV in Excel vs Notepad
Use `data/IPL_match_sample.csv` if your instructor provides it. The package includes `zomato_restaurants_sample.csv` as an additional CSV practice file; it is synthetic and not actual Zomato data.

Two differences:
1. **Excel:** CSV values are arranged in rows and columns, making sorting, filtering, formulas, and charting easier. **Notepad:** the same file appears as plain text with values separated by commas.
2. **Excel:** column headers and data types are easier to inspect visually; **Notepad:** it is easier to see the raw comma-separated text and inspect delimiters, but analysis is harder.

## Task 2 — Read JSON and print movie titles
Run `python python/print_movie_titles.py`. It loads `data/trending_movies.json` and prints each `title`.

Expected output:
Movie titles:
The Shawshank Redemption
The Dark Knight
Inception
Interstellar
The Grand Budapest Hotel

## Task 3 — Import XLSX restaurant data into MySQL
The package includes `data/zomato_restaurants_sample.csv` because an actual XLSX export was not supplied. If the task specifically requires XLSX, open this CSV in Excel and choose Save As → Excel Workbook (.xlsx), or use the instructor-provided XLSX.
1. Open MySQL Workbench and connect to your local MySQL server.
2. Create/select schema `session2_practice`.
3. Right-click `Tables` → `Table Data Import Wizard`.
4. Select the XLSX converted to CSV first if using the wizard's supported CSV flow; if your Workbench version supports XLSX, select the XLSX directly. Otherwise save the sheet as CSV and import that CSV.
5. Choose/create table `zomato_restaurants`; check column names and types; finish import.
6. Run `sql/zomato_import_and_query.sql` (after confirming the table is imported).
Note: the provided sample restaurant data is fictional and is for practicing import only.

## Task 4 — ETL vs ELT
- **ETL (Extract, Transform, Load):** data is cleaned/transformed before loading into the destination. Example: a food delivery app extracts order records, standardizes restaurant names and removes invalid rows, then loads cleaned records into a reporting database.
- **ELT (Extract, Load, Transform):** raw data is loaded into the destination first, then transformed there. Example: a music app loads raw playlist/listening events into a cloud warehouse, then uses warehouse SQL to build cleaned playlist and listening summaries.

## Task 5 — OLTP or OLAP
1. Booking a movie ticket on BookMyShow — **OLTP**, because it processes a real-time transaction and updates seat availability.
2. Generating a monthly sales report for Flipkart sellers — **OLAP**, because it aggregates historical sales for analysis.
3. Adding a new contact in WhatsApp — **OLTP**, because it records an individual operational change.
4. Analyzing IPL team performance over 5 seasons — **OLAP**, because it summarizes historical data across many matches and seasons.

## Concepts
- Structured data: organized into a fixed schema such as rows/columns in a SQL table.
- Unstructured data: content without a rigid table schema, such as images, audio, or free-form documents.
- CSV: text with delimiter-separated values.
- XLSX: Excel workbook format.
- JSON: key-value/object and array format often used by APIs.
- RDBMS: relational database management system, e.g. MySQL.
- Data warehouse: system optimized for analytics and reporting.
- OLTP: Online Transaction Processing.
- OLAP: Online Analytical Processing.
