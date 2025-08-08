import csv
from datetime import datetime
import os

print("🔍 Script started")

input_file = "askreddit_posts.csv"
output_file = "askreddit_cleaned.csv"

# Confirm the input file exists
if not os.path.exists(input_file):
    print(f"❌ File not found: {input_file}")
    exit()

print(f"📄 Found input file: {input_file}")

cleaned_posts = []
row_count = 0

# Read and convert
with open(input_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            created_date = datetime.utcfromtimestamp(float(row["Created_UTC"])).strftime('%Y-%m-%d %H:%M:%S')

            cleaned_posts.append({
                "Title": row["Title"],
                "Author": row["Author"],
                "Score": int(row["Score"]),
                "Created": created_date,
                "Comments": int(row["Num_Comments"]),
                "URL": row["URL"]
            })

            row_count += 1
        except Exception as e:
            print(f"⚠️ Skipped row due to error: {e}")

print(f"✅ Finished reading {row_count} posts")

# Sort and write output
if cleaned_posts:
    cleaned_posts.sort(key=lambda x: x["Score"], reverse=True)

    with open(output_file, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Title", "Author", "Score", "Created", "Comments", "URL"])
        writer.writeheader()
        writer.writerows(cleaned_posts)

    print(f"✅ Cleaned {len(cleaned_posts)} posts. File saved as {output_file}")
else:
    print("⚠️ No valid posts to write.")