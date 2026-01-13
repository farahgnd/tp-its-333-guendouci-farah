from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Config de la base
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecole.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------------- CLASSES ----------------

class Groupe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    etudiants = db.relationship('Etudiant', backref='groupe', lazy=True)

class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groupe.id'))

# ---------------- CREATION BASE ----------------

with app.app_context():
    db.create_all()  # crée toutes les tables si elles n'existent pas

    # créer le groupe ITS2 seulement si pas déjà là
    if not Groupe.query.filter_by(nom="ITS2").first():
        its2 = Groupe(nom="ITS2")
        e1 = Etudiant(nom="Farah", groupe=its2)
        e2 = Etudiant(nom="Amine", groupe=its2)
        e3 = Etudiant(nom="Sara", groupe=its2)

        db.session.add(its2)
        db.session.add_all([e1, e2, e3])
        db.session.commit()

# ---------------- ROUTES ----------------

@app.route('/')
def index():
    groupe = Groupe.query.filter_by(nom="ITS2").first()
    return {
        "groupe": groupe.nom,
        "etudiants": [e.nom for e in groupe.etudiants]
    }

if __name__ == '__main__':
    app.run(debug=True)
