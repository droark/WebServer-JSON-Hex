from webFiles import db, app
import sys

# Whoosh may have issues with Python 3. For now, disable Whoosh under Python 3.
if sys.version_info >= (3, 0):
    enable_search = False
else:
    enable_search = True
    import flask.ext.whooshalchemy as whooshalchemy

# The DB model.
class SHA_JSON_DB(db.Model):
    # Tells Whoosh what should be searchable via plain text.
    __searchable__ = ['sha256Hash']

    # ID will be ignored. SHA-256 hash must be 64 hex chars. JSON data is
    # allowed to be really large for now. This could change later.
    id = db.Column(db.Integer, primary_key=True)
    sha256Hash = db.Column(db.String(64), index=True, unique=True)
    jsonData = db.Column(db.String(250000), index=True, unique=True)

    # Describes how to print class objects.
    def __repr__(self):
        return '<SHA-256 Hash - %r>' % (self.sha256Hash)

if enable_search:
    whooshalchemy.whoosh_index(app, SHA_JSON_DB)
