from app import db

class Funcionario(db.Model):
    __tablename__ = 'funcionarios'
#definindo modelo de dados 
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
