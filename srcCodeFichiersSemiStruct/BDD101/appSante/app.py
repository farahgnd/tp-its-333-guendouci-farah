from flask import Flask, request, jsonify
import json

app = Flask(__name__)


def get_rapports_sante(patient_id, filename='patients.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        patients = json.load(f)  
    for patient in patients:
        if patient["id"] == patient_id:
            return {
                "id": patient_id,
                "rapports_medicals": patient.get("rapports_medicals", [])
            }
    return {"erreur": "Patient non trouvé"}



@app.route('/patient/sante', methods=['POST'])
def patient_sante():
    data_request = request.get_json()       
    patient_id = data_request.get("id")     
    result = get_rapports_sante(patient_id)
    return jsonify(result)                  


if __name__ == '__main__':
    app.run(debug=True)
