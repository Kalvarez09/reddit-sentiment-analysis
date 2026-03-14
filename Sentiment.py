import psycopg2
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)
    compound = vs['compound']
    if compound >= 0.05:
        label = "positive"
    elif compound <= -0.05:
        label = "negative"
    else:
        label = "neutral"
    return compound, label

def main():
    conn = psycopg2.connect(
        dbname="final",
    )
    cur = conn.cursor()

    # Crear tabla para resultados si no existe
    cur.execute("""
        CREATE TABLE IF NOT EXISTS post_sentiment (
            post_id SERIAL PRIMARY KEY,
            post_text TEXT,
            sentiment_score FLOAT,
            sentiment_label TEXT
        );
    """)
    conn.commit()

    # Cargar los posts
    cur.execute("SELECT id, body FROM posts;")
    rows = cur.fetchall()

    analyzer = SentimentIntensityAnalyzer()
    total = 0
    for post_id, text in rows:
        if not text:
            continue
        score, label = analyze_sentiment_vader(text)
        cur.execute(
            "INSERT INTO post_sentiment (post_text, sentiment_score, sentiment_label) VALUES (%s, %s, %s);",
            (text, score, label)
        )
        total += 1

    conn.commit()
    cur.close()
    conn.close()
    print(f"Análisis completado. Posts analizados: {total}")

if __name__ == "__main__":
    main()
