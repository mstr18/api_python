from flask import Flask, jsonify, request

app = Flask (__name__)

livros = [

    {
        'id' : 1,
        'titulo' : 'O senhor dos aneis',
        'autor': 'JRRR Tolekien'
    },
    {
        'id' : 2,
        'titulo' : 'Titulo do livro 2',
        'autor': 'Autor 2'
    },
    {
        'id' : 3,
        'titulo' : 'Titulo do livro 3',
        'autor': 'Autor 3'
    },
]

#consultar todos
@app.route('/livros', methods=['GET'])
def obterLivros():
    return jsonify(livros)

#consultar por id
@app.route('/livros/<int:id>', methods=['GET'])
def obterLivrosId(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
#editar
@app.route('/livros/<int:id>', methods=['PUT'])
def alterarLivrosId(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
#Incluir
@app.route('/livros', methods=['POST'])
def incluirLivro():
     novo_livro = request.get_json()
     livros.append(novo_livro)
     return jsonify(livros)


#Deletar por id
@app.route('/livros/<int:id>',  methods=['DELETE'])
def excluirLivrosId(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)
        
app.run(port=5000, host='localhost', debug=True)