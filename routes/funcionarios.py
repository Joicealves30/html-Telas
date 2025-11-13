from flask import Blueprint , render_template ,request

funcionario_route = Blueprint('funcionarios', __name__)

@funcionario_route.route('/dashboard')
def lista_funcionarios():
    return render_template('funcionario.html')


@funcionario_route.route('/novo', methods=['POST'])
def inserir_funcionario():
    return render_template('funcionario.html')

@funcionario_route.route('/new')
def form_funcionario():
    return render_template('funcionario.html')


@funcionario_route.route('/<int:funcionario_id>')
def detalhe_funcionario(funcionario_id):
    return render_template('funcionario.html')

@funcionario_route.route('/<int:funcionario_id>/edit')
def edit_funcionario(funcionario_id):
    return render_template('form_edit_funcionario.html')

@funcionario_route.route('/<int:funcionario_id>/update' , methods=['PUT'])
def atualizar_funcionario(funcionario_id):
    pass

@funcionario_route.route('/<int:funcionario_id>/delete', methods=['DELETE'])
def deletar_funcionario(funcionario_id):
    pass