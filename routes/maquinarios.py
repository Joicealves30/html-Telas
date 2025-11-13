from flask import Blueprint , render_template ,request

maquinario_route = Blueprint('maquinarios', __name__)

@maquinario_route.route('/dashboard')
def lista_maquinarios():
    return render_template('maquinario.html')


@maquinario_route.route('/novo', methods=['POST'])
def inserir_maquinario():
    return render_template('maquinario.html')

@maquinario_route.route('/new')
def form_maquinario():
    return render_template('maquinario.html')


@maquinario_route.route('/<int:maquinario_id>')
def detalhe_maquinario(maquinario_id):
    return render_template('maquinario.html')

@maquinario_route.route('/<int:maquinario_id>/edit')
def edit_maquinario(maquinario_id):
    return render_template('maquinario.html')

@maquinario_route.route('/<int:maquinario_id>/update' , methods=['PUT'])
def atualizar_maquinario(maquinario_id):
    pass

@maquinario_route.route('/<int:maquinario_id>/delete', methods=['DELETE'])
def deletar_maquinario(maquinario_id):
    pass