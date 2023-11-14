from flask import Flask, render_template, request, flash
from Models.AnalizadorLexicografico import AnalizadorLexicografico

app = Flask(__name__)
app.secret_key = '123'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        texto = AnalizadorLexicografico(request.form["texto"])
        respuesta = texto.analizar()
        flash(respuesta[0])
        flash(respuesta[1])
        flash(respuesta[2])
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
