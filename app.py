# ...existing code...
from flask import Flask, redirect, render_template, request, url_for
from database import db 
from models.dono import Dono

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/fazendinha'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)    


from models.funcionario import Funcionario 

#parei aqui

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']

        
        dono = Dono.query.filter_by(username=usuario).first()

        if dono and dono.senha == senha:
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', erro="Usuário ou senha incorretos!")

    return render_template('login.html')

    
@app.route('/')
def home():
    return redirect(url_for('login')) 

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/funcionarios', methods=['GET', 'POST'])
def funcionarios():

    if request.method == 'POST':
        novo = Funcionario(
            nome=request.form['nome'],
            cargo=request.form['cargo'],
            cultura=request.form['cultura'],
            salario=float(request.form['salario']),
            atribuicoes=request.form['atribuicoes']
        )
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('funcionarios'))

    lista = Funcionario.query.all()
    return render_template('funcionarios.html', funcionarios=lista)

  

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')

@app.route('/maquinarios')
def maquinarios():
    return render_template('maquinarios.html')

if __name__ == '__main__':
    app.run(debug=True)
