SESSION 5 - Exploratory Data Analysis (EDA) in Excel
====================================================
File: IPL_EDA_Session5.xlsx   (5 sheets)

NOTE ON DATA: This is a small SAMPLE IPL-style dataset (40 batting records, player names
are placeholders) created for the exercise. To use a real dataset, download one from
Kaggle (search "IPL dataset") and paste your rows into the "Data" sheet - all stats,
the chart and the highlighting update automatically if columns stay the same.

TASK 1 - Dataset            -> Sheet "Data" (Match, Player, Team, Venue, Runs, Balls, Fours, Sixes, Wickets, Result)

TASK 2 - Univariate analysis of Runs (sheet "Univariate", Excel functions)
  Mean   = AVERAGE()  -> 33.73
  Median = MEDIAN()   -> 28
  Min    = MIN()      -> 2
  Max    = MAX()      -> 118
  Std Dev = STDEV()   -> 25.26
  Insight: Mean (33.7) > Median (28), so the data is right-skewed - a few big
  scores pull the average up.

TASK 3 - Bivariate scatter plot (sheet "Scatter_Plot")
  X = Balls faced, Y = Runs scored, with a trendline.
  Correlation (CORREL) = 0.95 -> very strong positive relationship.
  How to make it by hand: select the Balls and Runs columns > Insert > Scatter Chart.

TASK 4 - Outliers (sheet "Data", column E highlighted + column K flag)
  Rule: Mean +/- 2 x Std Dev -> upper limit 84.24, lower limit -16.79
  Conditional formatting: Home > Conditional Formatting > New Rule > Use a formula
     =E2>Univariate!$B$10  (red)     =E2<Univariate!$B$11  (blue)
  Result: 2 high outliers - Player 10 (118 runs) and Player 27 (109 runs).
  No low outliers (the lower limit is below zero, and runs can't be negative).

TASK 5 - Multivariate analysis: Team x Venue (sheet "Pivot_Team_Venue")
  Table 1 = average runs per player, Table 2 = total runs, by Team and Venue.
  Insight: Chennai Super Kings at Wankhede (avg 90.5) and Gujarat Titans at Chepauk
  (avg 50) look high mainly because of the 2 outliers - so always check outliers
  before comparing group averages.

  To build a REAL PivotTable in Excel:
  1. Click any cell in the Data sheet > Insert > PivotTable > OK
  2. Drag Team -> Rows, Venue -> Columns, Runs -> Values
  3. Click Runs in Values > Value Field Settings > Average (or Sum)
