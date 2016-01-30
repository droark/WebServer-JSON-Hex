from webFiles import app, models, db
from webConfig import MAX_SEARCH_RESULTS
from flask import request
from hashlib import sha256
from sqlalchemy import exc
#from sqlalchemy import exc, asc, desc
#from sqlalchemy.sql import select
import sys
import json
import string

def addDataToDB(inHash, inData):
    """
    Attempt to add a JSON string and its accompanying hash to the DB. The code
    won't do a sanity check on the JSON string. It assumes you've already
    checked for validity!
    """

    # Check to make sure the data isn't in the DB before trying to add it.
    searchRes = searchDB(inHash)
    if searchRes != None:
        return 'Data is already in the database! Will not add again.\n'

    # Add an entry to the DB.
    retStr = ''
    u = models.SHA_JSON_DB(sha256Hash=inHash, jsonData=inData)
    db.session.add(u)
    try:
        db.session.commit()
        retStr = 'Data added to the database.\nData = %s\nSHA-256 hash = %s\n' % \
            (inData, inHash)
    except exc.IntegrityError:
        retStr = 'Data already in database! Data not added.\n'
    except exc.OperationalError:
        retStr = 'Database does not exist! Data not added.\n'
    except:
        retStr = 'Unknown Database Error! Data not added. Error = %s\n' % sys.exc_info()[0]
    finally:
        # Log whatever happened for debug purposes.
        print 'DEBUG (addDataToDB): %s' % retStr

    return retStr


def searchDB(searchKey):
    """
    Searches the database using an incoming key (hex-encoded string of the
    SHA-256 hash of the data in the DB). Designed to retrieve only one object,
    as there should be only one object in the DB anyway.
    """

    # Here's a bit of code showing how to query without Whoosh, which adds
    # overhead.
    # 1)Search for a specific key and print the retrieved SHA-256 hash.
#    mySQLQuery0 = select([models.SHA_JSON_DB]).where(models.SHA_JSON_DB.sha256Hash == searchKey)
#    mySQLQueryRes0 = db.session.execute(mySQLQuery0)
#    for item0 in mySQLQueryRes0.fetchall():
#        print 'DEBUG: SHA-256 Hash = %s' % item0.sha256Hash
#
    # 2)Get everything sorted in a particular order and print everything
    #   in the entry, broken down.
#    mySQLQuery1 = select([models.SHA_JSON_DB]).order_by(desc(models.SHA_JSON_DB.sha256Hash))
#    mySQLQueryRes1 = db.session.execute(mySQLQuery1)
#    for item1 in mySQLQueryRes1.fetchall():
#        print 'DEBUG: Query Contents (descending): Column 1 = %d' % item1[0]
#        print 'DEBUG: Query Contents (descending): Column 2 = %s' % item1[1]
#        print 'DEBUG: Query Contents (descending): Column 3 = %s' % item1[2]

    searchRes = None
    try:
        searchRes = models.SHA_JSON_DB.query.whoosh_search(searchKey, MAX_SEARCH_RESULTS).all()
    except exc.InvalidRequestError: # Occurs if the data was already in the DB.
        print 'DEBUG (searchDB): Database got an invalid request!'
    except:
        print 'DEBUG (searchDB): Unknown database error! Error = %s' % sys.exc_info()[0]

    # We only want one item, so get it from the list if it exists.
    if len(searchRes) == 0:
        searchRes = None
    else:
        searchRes = searchRes[0]
    return searchRes


@app.route('/')
def index():
    """
    Return a "Hello, World!" message alongside a little ray of sunshine.
    """
    return "Hello, you big, beautiful world. Go get 'em!"


@app.route('/sendJSON', methods=['GET', 'POST'])
def sendJSON():
    """
    Handles the case when data is sent to the server to be added to the DB. Data
    must be JSON-encoded, with "jsonData" being the key.
    """

    # The headers must contain "Content-Type: application/json" or the data
    # won't be added to the DB.
    if request.json == None:
        return "Request type is not JSON! mimetype = %s" % request.mimetype

    # Add only valid JSON strings to the DB.
    try:
        json.loads(request.json["jsonData"])
    except ValueError:
        return "Incoming data isn\'t a valid JSON string! Data won\'t be " \
               "added to the database.\n"

    # Hash the JSON string, then add the string & hash to the DB.
    if request.method == 'POST':
        inData = sha256(request.json["jsonData"])
        inDataSHA256 = inData.hexdigest()
        return addDataToDB(inDataSHA256, request.json["jsonData"])

    else:
        # In theory, you could do something here. We won't for now.
        pass
#        print 'DEBUG: mimetype = %s' % request.mimetype
#        print 'DEBUG: method = %s' % request.method


@app.route('/getJSON/<hashStr>', methods=['GET'])
def getJSON(hashStr):
    """
    Takes the incoming SHA-256 hash and uses it as a search key for the DB on
    the server. If a hit is found, return the value that was found, which will
    be a JSON-encoded string.
    """

    # Make sure the incoming string is a valid SHA-256 hash.
    if len(hashStr) != 64:
        return "The SHA-256 hash size isn\'t correct. Please check the string."

    # Check to make sure the input string is actually a hex string.
    if all(shaChars in string.hexdigits for shaChars in hashStr) == False:
        return "The SHA-256 hash has non-hex characters. Please check the string."

    # Search the DB! If we get a hit, return it, otherwise return an error.
    searchRes = searchDB(hashStr)
    if searchRes != None:
        return 'JSON data = %s\n' % searchRes.jsonData
    else:
        return 'Data represented by the SHA-256 hash isn\'t in the database!\n'
