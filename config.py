class Config(object):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    # Configuração do banco de dados PostgreSQL
    debug = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://lapisco:lapisco@localhost/lapisco'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    