# Session 1 — Written task answers

## 1. Excel: Data, Information, Insight
- **Raw data:** `match_no`, `city`, `date_of_match`, `venue`, `home_team`, `away_team`, `toss_winner`, `winner`, `result`, and other match-level columns.
- **Information:** totals calculated from the rows, such as matches played per city or wins per team.
- **Insight:** summaries help compare team results or venue activity. Since the supplied project CSV is a small practice sample, conclusions apply only to that sample unless you use the complete official dataset.

## 2. SQL
Use `sql/task2_queries.sql`. The main query counts each team's appearances as either the home team or away team, then groups by team.

## 3. Python
Run `python python/task3_analysis.py`. It reads the CSV with pandas and displays the number of wins per team.

## 4. Power BI
Load the CSV and create a clustered column chart. Axis: `city`. Values: Count of `match_no`. Title: `Matches Played per City`.

## 5. Analytics example
**Descriptive analytics in an IPL app:** the app summarizes previous matches, wins, and player statistics. This improves user experience because people can quickly see what happened in past games without reading every match report.

## Suggested submission note
Replace the practice sample with your instructor's complete `IPL_2023_Matches.csv` before submitting final counts or claiming full-season insights.
