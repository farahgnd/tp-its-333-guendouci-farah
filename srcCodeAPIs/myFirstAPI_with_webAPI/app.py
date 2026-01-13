from flask import Flask, jsonify, request

app = Flask(__name__)

## EXO1: API GET: renvoyer un helloworld - API end point name: "api/salutation"
@app.route('/api/salutation', methods=['GET'])
def salutation():
    return jsonify({"message": "Hello World"})

## EXO2: API POST: renvoyer un nom fourni en parametre - API end point name: "api/utilisateurs"
@app.route('/api/utilisateurs', methods=['POST'])
def utilisateurs():
    data = request.json      # récupère le JSON envoyé
    nom = data["nom"]        # récupère directement "nom"
    return jsonify({"nom": nom})  # renvoie le nom

# to be tested with curl: 
# >> curl.exe -i http://localhost:5000/api/salutation
# >> curl.exe -i -H "Content-Type: application/json" -d "{\"nom\":\"Bob\"}" http://localhost:5000/api/utilisateurs

if __name__ == '__main__':
    app.run(debug=True)
