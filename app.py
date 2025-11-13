from flask import Flask, redirect, render_template, request, url_for
from routes.estoque import estoque_route
from routes.funcionarios import funcionario_route
from routes.maquinarios import maquinario_route

app = Flask(__name__)

app.register_blueprint(estoque_route, url_prefix='/estoque')
app.register_blueprint(funcionario_route, url_prefix='/funcionarios')
app.register_blueprint(maquinario_route, url_prefix='/maquinarios')

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/funcionarios')
def funcionarios():
    return render_template('funcionarios.html')

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')

@app.route('/maquinarios')
def maquinarios():
    return render_template('maquinarios.html')

if __name__ == '__main__':
    app.run(debug=True)
