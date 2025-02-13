import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Load data from the database
def load_data():
    conn = sqlite3.connect('sentiment_analysis.db')
    df = pd.read_sql_query("SELECT timestamp, sentiment, category FROM sentiment_data", conn)
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # Ensure datetime conversion
    conn.close()
    return df

# Plotting function
def plot_sentiment(df):
    plt.figure(figsize=(10, 5))
    for category in df['category'].unique():
        subset = df[df['category'] == category]
        plt.plot(subset['timestamp'], subset['sentiment'], label=category)
    plt.title('Sentiment Over Time by Category')
    plt.xlabel('Time')
    plt.ylabel('Sentiment')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

df = load_data()
if not df.empty:
    plot_sentiment(df)
else:
    print("No data to plot.")
