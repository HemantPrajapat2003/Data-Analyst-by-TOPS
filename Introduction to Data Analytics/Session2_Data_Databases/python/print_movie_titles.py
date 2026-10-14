import json
from pathlib import Path

# Load the JSON file from the project's data folder.
json_path = Path(__file__).resolve().parents[1] / "data" / "trending_movies.json"

with open(json_path, "r", encoding="utf-8") as file:
    movies = json.load(file)

print("Movie titles:")
for movie in movies:
    print(movie["title"])
