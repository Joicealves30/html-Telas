from database import db

class Dono(db.Model):
    __tablename__ = 'dono'

    id_dono = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), nullable=False)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(13))
    username = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(100))
