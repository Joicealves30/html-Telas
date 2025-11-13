from flask import Blueprint , render_template ,request


estoque_route = Blueprint('estoque', __name__)


@estoque_route.route('/dashboard')
def lista_estoque():
    return render_template('estoque.html')


@estoque_route.route('/novo', methods=['POST'])
def inserir_estoque():
    return render_template('estoque.html')

@estoque_route.route('/new')
def form_estoque():
    return render_template('estoque.html')


@estoque_route.route('/<int:produto_id>')
def detalhe_estoque(saca_id):
    return render_template('detalhe_estoque.html')

@estoque_route.route('/<int:saca_id>/edit')
def edit_estoque(saca_id):
    return render_template('form_edit_estoque.html')

@estoque_route.route('/<int:saca_id>/update' , methods=['PUT'])
def atualizar_estoque(saca_id):
    pass

@estoque_route.route('/<int:saca_id>/delete', methods=['DELETE'])
def deletar_estoque(saca_id):
    pass