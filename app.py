# -*- coding: utf-8 -*-
import logging

from flask import Flask
from flask_oidc import OpenIDConnect
from flask_restful import Api
from flask_compress import Compress
from flask_cors import CORS
from ambiente import static_folder, openid_db, uri
from routes import add_routes

logging.basicConfig(level = logging.DEBUG)

def create_app(armazenamento = None):
    app = Flask(__name__, static_folder = static_folder)
    app.config.update({
        'SECRET_KEY': 'MySecretIsMyPasswordBlaBla',
        'TESTING': True,
        'DEBUG': True,
        'SQLALCHEMY_DATABASE_URI': openid_db,
        'OIDC_CLIENT_SECRETS': 'client_secrets.json',
        'OIDC_ID_TOKEN_COOKIE_SECURE': False,
        'OIDC_REQUIRE_VERIFIED_EMAIL': False,
        'OIDC_OPENID_REALM': uri + '/oidc_callback'
    })

    CORS(app)
    Compress(app)
    print("app criado.")

    from db import create_db
    db = create_db()
    db.init_app(app)

    oidc = OpenIDConnect(app, armazenamento)
    add_routes(app, oidc)

    return app

