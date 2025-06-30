from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']

    # Salvar os dados em um arquivo .txt
    with open('dados.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"Nome: {nome}, Email: {email}\n")

    return f"Dados salvos com sucesso! Nome: {nome}, Email: {email}"

@app.route('/cadastros')
def mostrar_cadastros():
    cadastros = []
    try:
        with open('dados.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(', ')
                if len(partes) == 2:
                    nome,email = partes
                    cadastros.append({'nome':nome, 'email': email})
    except FileNotFoundError:
        pass
    return render_template('lista.html', cadastros=cadastros)

if __name__ == '__main__':
    app.run(debug=True)
