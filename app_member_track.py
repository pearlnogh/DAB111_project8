from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route('/test')
def test():
    return "Flask is working!"

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/data')
def data():
    connection = sqlite3.connect('gym_members_tracking.db')
    dataset = pd.read_sql_query("SELECT * FROM gym_members_tracking LIMIT 20", connection)
    connection.close()
    return render_template('data.html', tables=dataset.to_html(classes='table table-striped', index=False))

if __name__ == '__main__':
    app.run(debug=True)
