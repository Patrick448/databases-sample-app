from flask import Flask, render_template
import psycopg2
app = Flask(__name__)


data = [{'title': "Gestão de empresas", 'created':'21/02/2023'},
{'title': "Inglês Corporativo", 'created':'21/02/2023'},
{'title': "Análise de Dados", 'created':'21/02/2023'}]

def curso(id, nome, descricao, id_taxonomia, id2, area):
    return {'id': id, 'nome':nome, 'descricao':descricao, 'area': area}


def get_db_connection():
    conn = psycopg2.connect(user="postgres",
                                  password="pg12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="sample-db")
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * from ensino.curso c JOIN ensino.taxonomia t ON c.id_taxonomia = t.id;")
    records = cursor.fetchall()
    records_dict = [curso(*r) for r in records]
    conn.close()
    conn.close()

    return render_template('index.html', data=records_dict)


@app.route('/test')
def test():
    return "test"
