import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Aesthetic configuration
sns.set_style("whitegrid")
plt.rcParams.update({'figure.max_open_warning': 0})

# Load CSVs
sentiment_counts = pd.read_csv('/tmp/sentiment_counts.csv')
avg_sentiment_score = pd.read_csv('/tmp/avg_sentiment_score.csv')
posts_per_day = pd.read_csv('/tmp/posts_per_day.csv')
top_positive_posts = pd.read_csv('/tmp/top_positive_posts.csv')
top_negative_posts = pd.read_csv('/tmp/top_negative_posts.csv')

# Convert date column to datetime if needed
if 'post_date' in posts_per_day.columns:
    posts_per_day['post_date'] = pd.to_datetime(posts_per_day['post_date'])

# --- Visualization 1: Sentiment Distribution (Pie chart) ---
plt.figure(figsize=(7, 7))
plt.pie(
    sentiment_counts['total_posts'],
    labels=sentiment_counts['sentiment_label'],
    autopct='%1.1f%%',
    colors=['#2ca02c', '#d62728', '#1f77b4']
)
plt.title('Sentiment Distribution')
plt.show()

# --- Visualization 2: Average Sentiment Score by Label (Bar chart) ---
plt.figure(figsize=(8, 5))
sns.barplot(
    data=avg_sentiment_score,
    x='sentiment_label',
    y='avg_sentiment_score',
    hue='sentiment_label',
    palette='deep',
    legend=False
)
plt.title('Average Sentiment Score by Label')
plt.xlabel('Sentiment Label')
plt.ylabel('Average Score')
plt.show()

# --- Visualization 3: Posts Activity Over Time (Line chart) ---
plt.figure(figsize=(12, 6))
sns.lineplot(data=posts_per_day, x='post_date', y='post_count')
plt.title('Number of Posts per Day')
plt.xlabel('Date')
plt.ylabel('Number of Posts')
plt.xticks(rotation=45)
plt.show()

# --- Visualization 4: Top 5 Positive Posts ---
print("\nTop 5 posts with highest positive sentiment:\n")
top_positives_display = top_positive_posts.copy()
top_positives_display['post_text'] = top_positives_display['post_text'].apply(lambda x: x[:150] + '...' if isinstance(x, str) else '')
print(
    top_positives_display[['sentiment_score', 'post_text']]
    .sort_values('sentiment_score', ascending=False)
    .head(5)
    .to_string(index=False)
)

# --- Visualization 5: Top 5 Negative Posts ---
print("\nTop 5 posts with lowest negative sentiment:\n")
top_negatives_display = top_negative_posts.copy()
top_negatives_display['post_text'] = top_negatives_display['post_text'].apply(lambda x: x[:150] + '...' if isinstance(x, str) else '')
print(
    top_negatives_display[['sentiment_score', 'post_text']]
    .sort_values('sentiment_score', ascending=True)
    .head(5)
    .to_string(index=False)
)

# --- Visualization 6: Rare Words Appearing 5x More Than Average ---
try:
    rare_words = pd.read_csv('/tmp/rare_words.csv')
    top_rare_words = rare_words.sort_values('count', ascending=False).head(20)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_rare_words, x='count', y='word', palette='magma')
    plt.title("Words Appearing 5x More Than Average")
    plt.xlabel("Count")
    plt.ylabel("Word")
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"\n[INFO] Skipping rare words chart: {e}")

# --- Visualization 7: Least Used Words (Count = 1) ---
try:
    least_words = pd.read_csv('/tmp/least_used_words.csv')

    if least_words.empty:
        print("\n[INFO] least_used_words.csv is empty.")
    else:
        plt.figure(figsize=(12, 6))
        sns.barplot(data=least_words, x='count', y='word', palette='coolwarm')
        plt.title("Words That Appear Only Once (Sample of 50)")
        plt.xlabel("Count")
        plt.ylabel("Word")
        plt.tight_layout()
        plt.show()
except Exception as e:
    print(f"\n[INFO] Skipping least used words chart: {e}")

print("\n✅ Visualizations completed.")
