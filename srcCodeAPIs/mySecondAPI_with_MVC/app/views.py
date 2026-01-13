from app import app
from flask import render_template, request, jsonify

### EXO1 - simple API
@app.route('/api/salutation', methods=['GET'])
def salutation():
    return jsonify({"message": "Hello World"})



#  EXO2 - API with simple display
@app.route('/')
def index():
    return render_template('index.html')

### EXO3 - API with parameters display 
@app.route('/', methods=['GET'])
def affiche():
    nom = request.args.get("nom", "farah")   
    age = request.args.get("age", "22")  
    # renvoie le rendu HTML
    return render_template("index.html", nom=nom, age=age)

if __name__ == '__main__':
    app.run(debug=True)

### EXO4 - API with parameters retrieved from URL 

@app.route('/params')
def params():
    nom = request.args.get("nom")
    age = request.args.get("age")

    return render_template("index.html", nom=nom, age=age)

if __name__ == '__main__':
    app.run(debug=True)