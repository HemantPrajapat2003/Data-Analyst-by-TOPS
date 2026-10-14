# Session 1 — Introduction to Data Analytics

## Important dataset note
The included CSV is a **15-row practice sample**, not the complete official IPL 2023 season dataset. It is included so you can test the code and learn the workflow. For submission, download the complete `IPL_2023_Matches.csv` provided by your instructor and place it in `data/`. Update the filename in `python/task3_analysis.py` if necessary. The exercise screenshot explicitly names the instructor's sample file, so use that exact file if it was provided in your course portal.

A public IPL 2023 match analysis example with a matching style of columns is available here:
https://mayur-dusane.github.io/MayurDusaneDataAnalayst.github.io/IPL%202023%20Notebook.html
A separate public IPL dataset repository is here:
https://github.com/ritesh-ojha/IPL-DATASET

## Folder structure
- `data/IPL_2023_Matches_PRACTICE_SAMPLE.csv` — small practice dataset
- `sql/task2_queries.sql` — SQL query for matches played by each team
- `python/task3_analysis.py` — Pandas analysis for matches won by each team
- `docs/task_answers.md` — written answers and instructions for Excel and Power BI

## Task 1 — Excel: raw data, information, insight
1. Open the CSV in Excel.
2. Raw data: match-level facts such as match number, city, date, teams, toss winner, winner, result margin, and umpires.
3. Information: summaries created from raw data, such as total matches by city or wins by team.
4. Insight example: a city with more rows hosted more matches in this sample. Do not treat the 15-row practice sample as a full-season conclusion.

## Task 2 — SQL
Import the CSV into a table named `matches`. Ensure column names match the CSV. Run `sql/task2_queries.sql`.
Each match contributes one appearance to each of its two teams, so use `UNION ALL` before grouping.

## Task 3 — Python
Install pandas with `python -m pip install pandas`. From the project folder run:
`python python/task3_analysis.py`
For the complete official dataset, change the filename in the script to `IPL_2023_Matches.csv`.

## Task 4 — Power BI
1. Open Power BI Desktop → Get Data → Text/CSV.
2. Select the match CSV and choose Load.
3. In Report view, add a clustered column chart.
4. Put `city` in X-axis and `match_no` in Y-axis, then change aggregation of `match_no` to **Count**.
5. Rename the visual to `Matches Played per City`.
6. If a city is listed under multiple spellings, clean/standardize city names in Power Query first.

## Task 5 — Analytics type example
**Descriptive analytics** explains what has already happened. An IPL app could show a user's recent match results, team win counts, and player statistics. This helps users understand past performance and quickly find relevant match information.

## Definitions
- Data: raw facts (for example, one match's date and winner).
- Information: data organized or summarized (for example, wins per team).
- Insight: a meaningful conclusion drawn from information (for example, one team won more matches in the selected period).
- Descriptive: what happened?
- Diagnostic: why did it happen?
- Predictive: what may happen next?
- Prescriptive: what action might help?
