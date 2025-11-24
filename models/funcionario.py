from database import db 

class Funcionario(db.Model):
    __tablename__ = 'funcionarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)
    cultura = db.Column(db.String(50), nullable=False)
    salario = db.Column(db.Numeric(10,2), nullable=False)
    atribuicoes = db.Column(db.Text, nullable=False)
    data_cadastro = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Funcionario {self.nome}>'
  