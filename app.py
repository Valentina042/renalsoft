from flask import Flask, render_template

app = Flask(__name__)


@app.route('/vista_inicio')
def main_template():  
    return render_template("index.html")

@app.route('/vista_anatomia')
def anatomia_template():  
    return render_template("vistaA.html")

@app.route('/vista_fisiologia')
def fisiologia_template():  
    return render_template("vistaF.html")

@app.route('/vista_morfologia')
def morfologia_template():  
    return render_template("vistaM.html")


if __name__ == '__main__':
    app.run()
