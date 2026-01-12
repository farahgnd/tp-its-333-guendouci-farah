from app import app
from flask import render_template, request, jsonify

### EXO1 - simple API



### EXO2 - API with simple display
# @app.route('/')
# def index():
#     return render_template('index.html')



### EXO4 - API with parameters retrieved from URL 

@app.route('/', methods=['GET'])
def salutation_url():
    nom = request.args.get("nom")  # récupère le paramètre "nom" dans l'URL
    if not nom:
        return jsonify({"error": "Aucun nom fourni"}), 400
    return jsonify({"message": f"Bonjour {nom}"})

if __name__ == '__main__':
    app.run(debug=True)