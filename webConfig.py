import os
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLAlchemy - Basic interfacing with an SQLite DB
SQLALCHEMY_RECORD_QUERIES = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'WebServerHexJSON.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Whoosh - Makes text searches of a DB much easier
WHOOSH_BASE = os.path.join(basedir, 'whooshSearch.db')
MAX_SEARCH_RESULTS = 1
