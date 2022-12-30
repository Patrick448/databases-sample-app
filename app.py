from flask import Flask, render_template
import psycopg2
app = Flask(__name__)


data = [{'title': "Gestão de empresas", 'created':'21/02/2023'},
{'title': "Inglês Corporativo", 'created':'21/02/2023'},
{'title': "Análise de Dados", 'created':'21/02/2023'}]

def get_db_connection():
    conn = psycopg2.connect(user="postgres",
                                  password="pg12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="sample-db")
    return conn

@app.route('/')
def index():
    conn = psycopg2.connect(user="postgres",
                                  password="pg12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="sample-db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS posts;CREATE TABLE posts (id INTEGER PRIMARY KEY,created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,title TEXT NOT NULL,content TEXT NOT NULL);")
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
    cursor.close()
    conn.close()

    return render_template('index.html', data=data)
