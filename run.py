from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    imc = None
    peso_calc = ""
    altura_calc = ""
    
    if request.method == 'POST':
        try:
            # Pegando os valores do formulário
            peso_calc = float(request.form.get("peso"))
            altura_calc = float(request.form.get("altura"))
            
            # Convertendo altura para metros (se necessário)
            altura_calc /= 100  # Considera altura em centímetros
            
            # Calculando o IMC
            if altura_calc > 0:
                # imc = round(peso_calc / (altura_calc ** 2), 2)
                imc = round(peso_calc / (altura_calc ** 2), 2)
        except (ValueError, TypeError):
            imc = "Valores inválidos"

    return render_template("index.html", peso_calc=peso_calc, altura_calc=altura_calc, imc=imc)

if __name__ == '__main__':
    app.run("127.0.0.1", port=80, debug=True)
