
# ================================================================
# PROJECT TITLE: IGN DATA ANALYSIS
# Libraries: NumPy, Pandas, Matplotlib
# ================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# ================================================================
# SCENARIO 1: DATA LOADING & PREPROCESSING
# ================================================================

#1. Load the dataset using Pandas. 
#2. Display: 
     #○ First 5 rows (head()) 
     #○ Last 5 rows (tail()) 
     #○ Shape of dataset 
#3. Remove the unnecessary column: 
     #○ "Unnamed: 0" (index column) 
#4. Check for missing values in: 
     #○ score, genre, platform 
#5. Handle missing values: 
     #○ Fill numeric column score with mean 
     #○ Fill categorical column genre with mode 
#6. Ensure correct data types: 
     #○ score → float 
     #○ release_year, release_month, release_day → integer

# Load dataset
data = pd.read_csv(
    r"C:\Python_Tasks\Analytics\Project2\ign.csv"
)

# Display first 5 rows
print("\nFirst 5 rows:")
print(data.head())

# Display last 5 rows
print("\nLast 5 rows:")
print(data.tail())

# Display shape
print("\nDataset Shape:")
print(data.shape)

# Remove unnecessary column
data.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')

# Check missing values
print("\nMissing values before handling:")
print(data[['score', 'genre', 'platform']].isnull().sum())

# Convert score into numeric
data['score'] = pd.to_numeric(data['score'], errors='coerce')

# Fill missing score with mean
data['score'] = data['score'].fillna(data['score'].mean())

# Fill missing genre with mode
if not data['genre'].mode().empty:
    data['genre'] = data['genre'].fillna(data['genre'].mode()[0])

# Fill missing platform with mode
if not data['platform'].mode().empty:
    data['platform'] = data['platform'].fillna(data['platform'].mode()[0])

# Convert data types
data['score'] = data['score'].astype(float)

for col in ['release_year', 'release_month', 'release_day']:
    data[col] = pd.to_numeric(data[col], errors='coerce')

    # Fill missing dates before integer conversion
    data[col] = data[col].fillna(data[col].median()).astype(int)

print("\nMissing values after handling:")
print(data[['score', 'genre', 'platform']].isnull().sum())

print("\nData types:")
print(data.dtypes)

print("\nData preprocessing completed!")

# Create folder to save graphs
os.makedirs(
    r"C:\Python_Tasks\Analytics\Project2\pictorial_analysis",
    exist_ok=True
)

output_folder = r"C:\Python_Tasks\Analytics\Project2\pictorial_analysis"


# ================================================================
# SCENARIO 2: LINE GRAPH (SCORE TREND)
# ================================================================

#1. Group data by release_year. 
#2. Calculate average score per year using Pandas. 
#3. Convert results into NumPy arrays. 
#4. Plot a line graph: 
     #○ X-axis → release_year 
     #○ Y-axis → average score 
#5. Add: 
     #○ Title: "Average Game Score Over Years" 
     #○ Axis labels 

#6. Save the graph: plt.savefig("avg_score_trend.png")

# Group data by release year
grouped_year = data.groupby('release_year')['score'].mean()

print("\nAverage score per year:")
print(grouped_year)

# Convert into NumPy arrays
years = grouped_year.index.to_numpy()
avg_scores = grouped_year.values

# Plot line graph
plt.figure(figsize=(10, 5))

plt.plot(years, avg_scores, marker='o', color='blue')

plt.title("Average Game Score Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")

plt.grid(True)
plt.tight_layout()

plt.savefig(os.path.join(output_folder, "avg_score_trend.png"))

plt.show()


# ================================================================
# SCENARIO 3: FILTERING + BAR CHART
# ================================================================

#1. Filter dataset where: 
    #○ score > 7 
#2. Count number of high-rated games per platform. 
#3. Select top 10 platforms using Pandas. 
#4. Convert data into NumPy arrays. 
#5. Plot a bar chart: 
    #○ X-axis → platform 
    #○ Y-axis → count of games 
#6. Rotate x-axis labels for readability. 
    #Save the graph: plt.savefig("top_platforms_bar.png")
    # Filter games where score > 7
filtered_data = data[data['score'] > 7]

# Count high-rated games per platform
top_rated_games = filtered_data.groupby('platform')['title'].count()

print("\nHigh-rated games per platform:")
print(top_rated_games)

# Select top 10 platforms
top_10 = top_rated_games.sort_values(ascending=False).head(10)

print("\nTop 10 platforms:")
print(top_10)

# Convert into NumPy arrays
platforms = top_10.index.to_numpy()
counts = top_10.values

# Plot bar chart
plt.figure(figsize=(12, 6))

plt.bar(platforms, counts, color='orange')

plt.title("Top 10 Platforms by High-Rated Games")
plt.xlabel("Platform")
plt.ylabel("Number of Games")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(os.path.join(output_folder, "top_platforms_bar.png"))

plt.show()


# ================================================================
# SCENARIO 4: AGGREGATION + PIE CHART
# ================================================================

#1. Count the number of games per genre. 
#2. Select top 5 genres using Pandas. 
#3. Prepare labels and values. 
#4. Plot a pie chart: 
     #○ Labels → genre 
     #○ Values → count 
#5. Add percentage labels (autopct). 
     #Save the graph: plt.savefig("genre_distribution.png")
     # Count games per genre
genre_counts = data['genre'].value_counts()

print("\nGames per genre:")
print(genre_counts)

# Select top 5 genres
top_5 = genre_counts.head(5)

print("\nTop 5 genres:")
print(top_5)

# Prepare labels and values
genres = top_5.index.to_numpy()
counts = top_5.values

# Plot pie chart
plt.figure(figsize=(8, 8))

plt.pie(
    counts,
    labels=genres,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Genre Distribution")

plt.tight_layout()

plt.savefig(os.path.join(output_folder, "genre_distribution.png"))

plt.show()


# ================================================================
# SCENARIO 5: ADVANCED ANALYSIS
# ================================================================

#Create a new column: 
    #○ score_category: 
  #■ score >= 9 → "Excellent" 
  #■ 7 <= score < 9 → "Good" 
  #■ < 7 → "Average" 
    #2. Convert editors_choice: 
    #○ Y → 1, N → 0
# PART 1: FEATURE ENGINEERING

# Create score_category column
data['score_category'] = np.where(
    data['score'] >= 9,
    "Excellent",
    np.where(data['score'] >= 7, "Good", "Average")
)

print("\nScore categories created!")

# Convert editors_choice Y -> 1 and N -> 0
data['editors_choice'] = data['editors_choice'].map({
    'Y': 1,
    'N': 0
})

print("\nEditors choice converted into numeric values!")

  #3. Use NumPy to: 
  #○ Calculate yearly score growth using np.diff() on average yearly scores
# PART 2: NUMPY ANALYSIS

# Calculate average score per year
yearly_avg = data.groupby('release_year')['score'].mean()

years = yearly_avg.index.to_numpy()
avg_scores = yearly_avg.values

# Calculate yearly score growth using np.diff()
score_growth = np.diff(avg_scores)

print("\nYearly score growth:")
print(score_growth)


#Line Graph 
  #4. Plot trend of: 
    #○ Average score per release_year 
    #Stacked Bar Chart 
  #5. Show count of: 
    #○ score_category per release_year 
    #Histogram 
  #6. Plot distribution of: 
    #○ score
# PART 3: VISUALIZATIONS

# 1. LINE GRAPH: SCORE TREND

plt.figure(figsize=(10, 5))

plt.plot(years, avg_scores, marker='o', color='green')

plt.title("Average Score Trend Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")

plt.grid(True)
plt.tight_layout()

plt.savefig(os.path.join(output_folder, "score_trend.png"))

plt.show()


# 2. STACKED BAR CHART: SCORE CATEGORY PER YEAR

category_counts = data.pivot_table(
    index='release_year',
    columns='score_category',
    aggfunc='size',
    fill_value=0
)

# Ensure consistent category order
category_counts = category_counts.reindex(
    columns=['Average', 'Good', 'Excellent'],
    fill_value=0
)

category_counts.plot(
    kind='bar',
    stacked=True,
    figsize=(14, 6),
    color=['skyblue', 'orange', 'green']
)

plt.title("Score Category Distribution per Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Games")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(os.path.join(output_folder, "score_category_stacked.png"))

plt.show()


# 3. HISTOGRAM: SCORE DISTRIBUTION

plt.figure(figsize=(10, 5))

plt.hist(
    data['score'].dropna(),
    bins=20,
    color='purple',
    edgecolor='black'
)

plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(os.path.join(output_folder, "score_distribution.png"))

plt.show()


# ================================================================
# PART 5: INSIGHTS
# ================================================================

# Year with highest average score
max_year = yearly_avg.idxmax()
max_score = yearly_avg.max()

print("\n====================================")
print("             PROJECT INSIGHTS")
print("====================================")

print(
    f"\nYear with highest average score: "
    f"{max_year} ({max_score:.2f})"
)

# Check overall score trend
if len(score_growth) > 0:
    if score_growth.mean() > 0:
        print("\nOverall trend: Average scores increased over time.")
    else:
        print("\nOverall trend: Average scores decreased or fluctuated.")

# Editors choice vs average score
editors_avg = data.groupby('editors_choice')['score'].mean()

print("\nAverage score based on Editors Choice:")
print(editors_avg)

if 1 in editors_avg.index and 0 in editors_avg.index:
    if editors_avg.loc[1] > editors_avg.loc[0]:
        print("\nEditors Choice games have higher average scores.")
    else:
        print("\nEditors Choice games do not have higher average scores.")
else:
    print("\nUnable to compare both Editors Choice groups.")

print("\n====================================")
print("       PROJECT COMPLETED!")
print("====================================")

print("\nAll graphs saved successfully in:")
print(output_folder)

print("\nTotal graphs generated: 6")
