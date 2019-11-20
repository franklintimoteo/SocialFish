import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import click

from .config import config
from .core.view import head
from .core.cleanFake import cleanFake
from .core.dbsf import init_db_command
from .core.cleanFake import clean_fake_command

from .core.config import DATABASE


head()
login_manager = LoginManager()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    #configurações para testes
    config_name = config_name.data or os.getenv('FLASK_CONFIG')
    config_name = config_name or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #inicializa o gerenciador de login
    login_manager.init_app(app)
    #incializa o bootstrap
    Bootstrap(app)
    #inicializa SQLAlchemy
    db.init_app(app)

    # cria diretorio instance ex: mkdir ../instance
    # exist_ok - não levanta uma exceção caso o diretório já exista
    os.makedirs(app.instance_path, exist_ok=True)
    # adicionar comando init_db_command ex: flask init-db
    app.cli.add_command(init_db_command)
    app.cli.add_command(clean_fake_command)
    app.cli.add_command(test)

    from .socialfish import socialbp # Blueprint
    app.register_blueprint(socialbp)
    return app

import click

@click.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)