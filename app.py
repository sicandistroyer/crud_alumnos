from flask import Flask

#crear instancia
app =  Flask(__name__)

#Ruta raiz
@app.route('/')
def hola_mundo():
    return 'Hola Mundo'

if __name__ == '__main__':
    app.run(debug=True)