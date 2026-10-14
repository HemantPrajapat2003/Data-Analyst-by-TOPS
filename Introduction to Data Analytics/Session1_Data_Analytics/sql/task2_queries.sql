-- Session 1 Task 2: count matches played by each team (SQLite/MySQL-compatible)
-- Import the CSV into a table named matches first.
SELECT team, COUNT(*) AS total_matches_played
FROM (
    SELECT home_team AS team, match_no FROM matches
    UNION ALL
    SELECT away_team AS team, match_no FROM matches
) AS team_matches
GROUP BY team
ORDER BY total_matches_played DESC, team;

-- Optional: count matches won by each team
SELECT winner, COUNT(*) AS matches_won
FROM matches
WHERE winner IS NOT NULL AND winner <> ''
GROUP BY winner
ORDER BY matches_won DESC;
