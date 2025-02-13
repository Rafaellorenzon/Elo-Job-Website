from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para a seção 1
@app.route("/section1")
def section1():
    return render_template("section1.html")

# Rota para a seção 2
@app.route("/section2")
def section2():
    return render_template("section2.html")

# Rota para a seção 3
@app.route("/section3")
def section3():
    return render_template("section3.html")

if __name__ == '__main__':
    app.run(debug=True)
