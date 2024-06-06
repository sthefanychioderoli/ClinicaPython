from flask import Flask, render_template, request, redirect

app = Flask(__name__)

login = [
        {'nome_animal':''},
        {'especie':''},
        {'raca':''},
        {'codigo':''},
        {'peso':''},
        {'nome_tutor':''},
        {'telefone':''}
 ]
num = 0
@app.route('/')
def index():
    return render_template('index.html', login=login, num=num)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        nome_animal = request.form['nome-animal']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = request.form['peso']
        nome_tutor = request.form['nome-tutor']
        telefone = request.form['telefone']
        num += 1
        login.append([nome_animal, especie, raca, peso, codigo, nome_tutor, telefone])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)