from flask import Flask
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # Connect to database
    conn = sqlite3.connect('bank_data.db')
    
    # Read first 10 rows
    df = pd.read_sql_query("SELECT * FROM transactions LIMIT 10", conn)
    conn.close()
    
    # Show as HTML table
    return "<h1>Bank Data</h1>" + df.to_html()

if __name__ == '__main__':
    app.run(debug=True)