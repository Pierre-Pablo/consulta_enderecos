
from crypt import methods
from flask import Flask, render_template, request
from consulta_endereco import consulta_cep 

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def CEP():
    cep = request.form['Cep']
    consulta_cep(cep)
    return render_template('resultado_busca.html')


app.run(debug = True)