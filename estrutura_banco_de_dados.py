from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Cria um API flask
app = Flask(__name__)
# Cria um instância de SQLAlchemy
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)
db: SQLAlchemy
# Definir a estrutura da tabela Postagem
# id_postagem, titulo, autor


class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_auto = db.Column(db.Integer,db.ForeignKey('autor.id_autor'))
# Definir a estrutura da tabela Autor
# id_autor, nome, email, senha, adimn, postagens
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')


def inicializar_banco():
    # Executar o comando para criar o banco de dados
    db.drop_all()
    db.create_all()
    # Criar usuários adminstadores
    autor = Autor(nome='Fellipe',email='fellipesantiago12@outlook.com.br',
                senha='123456789',admin=True)
    db.session.add(autor)
    db.session.commit()

if __name__ == "__main__":
    inicializar_banco()


