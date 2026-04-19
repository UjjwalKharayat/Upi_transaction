from flask import Flask
import sqlite3
import pandas as pd
import matplotlib
matplotlib.use('Agg') # Draw in background
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def home():
    # 1. Get Data
    conn = sqlite3.connect('bank_data.db')
    df = pd.read_sql_query("SELECT sender_bank FROM transactions", conn)
    conn.close()
    
    # 2. Count Math
    counts = df['sender_bank'].value_counts()
    
    # 3. Draw Picture
    plt.figure(figsize=(10, 5))
    counts.plot(kind='bar')
    plt.title('Bank Market Share')
    plt.ylabel('Transactions')
    plt.tight_layout() # Fix margins
    
    # 4. Save Picture as Text
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    # 5. Show on Web
    return f"<h1>Market Share Dashboard</h1><img src='data:image/png;base64,{plot_url}'>"

if __name__ == '__main__':
    app.run(debug=True)