from flask import Flask, render_template
import psycopg2
app = Flask(__name__)


data = [{'title': "Gestão de empresas", 'created':'21/02/2023'},
{'title': "Inglês Corporativo", 'created':'21/02/2023'},
{'title': "Análise de Dados", 'created':'21/02/2023'}]

def curso(id, nome, descricao, id_taxonomia, id2, area):
    return {'id': id, 'nome':nome, 'descricao':descricao, 'area': area}

def aluno(id, nome, end_cidade, end_uf, data_matricula):
    return {'id': id, 'nome':nome, 'end_cidade':end_cidade, 'end_uf': end_uf, 'data_matricula': data_matricula}


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

@app.route('/course-students/<id>')
def course_students(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"""SELECT u.id, u.nome, u.end_cidade, u.end_uf, data_matricula from ensino.curso c 
            JOIN ensino.alunocurso ac ON ac.id_curso = c.id
            JOIN ensino.aluno al ON ac.id_aluno = al.id
            JOIN ensino.usuario u on al.id = u.id
            WHERE c.id = {id};
            """)
    records = cursor.fetchall()
    records_dict = [aluno(*r) for r in records]
    conn.close()
    conn.close()


    return render_template('course_students.html', data=records_dict)


@app.route('/test')
def test():
    return "test"
