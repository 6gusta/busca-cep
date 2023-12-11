from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('cep.html')

@app.route('/buscar_cep', methods=['GET'])
def busca():
    cep = request.args.get('cep')

    if cep:
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return jsonify({'resultado': 'sucesso', 'dados': data})
        else:
            return jsonify({'resultado': 'erro', 'mensagem': 'CEP não encontrado'}), 404
    else:
        return jsonify({'resultado': 'erro', 'mensagem': 'CEP não informado'}), 400
    
if __name__ == '__main__':
    app.run(debug=True, port=5001)
