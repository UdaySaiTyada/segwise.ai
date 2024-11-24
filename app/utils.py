import csv
from datetime import datetime
import ast
from io import StringIO

def parse_csv_content(content: str):
    """
    Parse CSV content into a list of dictionaries.
    """
    csv_data = StringIO(content)
    reader = csv.DictReader(csv_data)

    data = []
    for row in reader:

        release_date = None
        for fmt in ("%b %Y", "%b %d, %Y"):
            try:
                release_date = datetime.strptime(row["Release date"], fmt).date()
                break
            except ValueError:
                continue

        if not release_date:
            raise ValueError(f"Invalid date format: {row['Release date']}")

        supported_languages = ast.literal_eval(row["Supported languages"])

        categories = [category.strip() for category in row["Categories"].split(",") if category]
        genres = [genre.strip() for genre in row["Genres"].split(",") if genre]
        tags = [tag.strip() for tag in row["Tags"].split(",") if tag]


        # Append processed data
        data.append({
            "app_id": int(row["AppID"]),
            "name": row["Name"],
            "release_date": release_date,
            "required_age": int(row["Required age"]),
            "price": float(row["Price"]),
            "dlc_count": int(row["DLC count"]),
            "about_game": row["About the game"],
            "supported_languages": supported_languages,
            "windows": row["Windows"] == "True",
            "mac": row["Mac"] == "True",
            "linux": row["Linux"] == "True",
            "positive": int(row["Positive"]),
            "negative": int(row["Negative"]),
            "score_rank": float(row["Score rank"]) if row["Score rank"] else None,
            "developers": row["Developers"],
            "publishers": row["Publishers"] if row["Publishers"] else None,
            "categories": categories,
            "genres": genres,
            "tags": tags,
        })
    return data