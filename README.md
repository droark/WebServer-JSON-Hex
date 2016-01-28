This is a set of two programs that are separate but somewhat designed to play together.

# HexTxToJSON
The first program (HexTxToJSON) takes a hex string-encoded Bitcoin transaction and converts the string into a JSON-encoded string appropriate for web page usage. Multiple versions of the string are printed out to accommodate different use cases.

**SOFTWARE REQUIREMENTS**:
[pybitcointools](https://github.com/vbuterin/pybitcointools) (Included with the codebase to simplify deployment)

**INSTALLATION STEPS (Linux)**:
None. The code should run as soon as it's downloaded.

### Convert a Bitcoin Tx to JSON ###
The program has one purpose: Convert a hex string-encoded Bitcoin transaction into JSON data. The program basically acts as a frontend that accesses the *pybitcointools* library, with some error handling included.

The following is an example of what is seen when submitting a string. Note how there are multiple versions of the output. This is done to support various methods for consuming JSON data.

```
$ python HexTxToJSON.py 0100000001383b58919c35d972c7e8cff56ce263cbaa4b31b70cdba0298fea312f826eb41c000000008a473044022025565fa72b39e18e9150ddfb28a1f319f13ecda507a87aa48895703c19aa110802200fa6b915064ce6c1de82a4aa6c6129c75d2ab0b61eaf7f7d5de42aef1323bb53014104cc9a9c754f14e342dd03527a5a18f58cbb835127861ea70f9e169354deb68470c16887fdfc00c2c1555ba2ddfc256549e3b50ac18a4d53fee13df5ff57d389d0ffffffff0248579e00000000001976a91436e325a5fe02032c2b08624850b9ae582a7ea54288ac038e3400000000001976a9143cb419f785182f3112d5ba1e0b3df65c77630ddf88ac00000000

Raw JSON string:
{"locktime": 0, "outs": [{"value": 10377032, "script": "76a91436e325a5fe02032c2b08624850b9ae582a7ea54288ac"}, {"value": 3444227, "script": "76a9143cb419f785182f3112d5ba1e0b3df65c77630ddf88ac"}], "version": 1, "ins": [{"script": "473044022025565fa72b39e18e9150ddfb28a1f319f13ecda507a87aa48895703c19aa110802200fa6b915064ce6c1de82a4aa6c6129c75d2ab0b61eaf7f7d5de42aef1323bb53014104cc9a9c754f14e342dd03527a5a18f58cbb835127861ea70f9e169354deb68470c16887fdfc00c2c1555ba2ddfc256549e3b50ac18a4d53fee13df5ff57d389d0", "outpoint": {"index": 0, "hash": "1cb46e822f31ea8f29a0db0cb7314baacb63e26cf5cfe8c772d9359c91583b38"}, "sequence": 4294967295}]}

Indented JSON string:
{
    "ins": [
        {
            "outpoint": {
                "hash": "1cb46e822f31ea8f29a0db0cb7314baacb63e26cf5cfe8c772d9359c91583b38", 
                "index": 0
            }, 
            "script": "473044022025565fa72b39e18e9150ddfb28a1f319f13ecda507a87aa48895703c19aa110802200fa6b915064ce6c1de82a4aa6c6129c75d2ab0b61eaf7f7d5de42aef1323bb53014104cc9a9c754f14e342dd03527a5a18f58cbb835127861ea70f9e169354deb68470c16887fdfc00c2c1555ba2ddfc256549e3b50ac18a4d53fee13df5ff57d389d0", 
            "sequence": 4294967295
        }
    ], 
    "locktime": 0, 
    "outs": [
        {
            "script": "76a91436e325a5fe02032c2b08624850b9ae582a7ea54288ac", 
            "value": 10377032
        }, 
        {
            "script": "76a9143cb419f785182f3112d5ba1e0b3df65c77630ddf88ac", 
            "value": 3444227
        }
    ], 
    "version": 1
}

JSON-encoded string:
{"jsonData":"{"locktime": 0, "outs": [{"value": 10377032, "script": "76a91436e325a5fe02032c2b08624850b9ae582a7ea54288ac"}, {"value": 3444227, "script": "76a9143cb419f785182f3112d5ba1e0b3df65c77630ddf88ac"}], "version": 1, "ins": [{"script": "473044022025565fa72b39e18e9150ddfb28a1f319f13ecda507a87aa48895703c19aa110802200fa6b915064ce6c1de82a4aa6c6129c75d2ab0b61eaf7f7d5de42aef1323bb53014104cc9a9c754f14e342dd03527a5a18f58cbb835127861ea70f9e169354deb68470c16887fdfc00c2c1555ba2ddfc256549e3b50ac18a4d53fee13df5ff57d389d0", "outpoint": {"index": 0, "hash": "1cb46e822f31ea8f29a0db0cb7314baacb63e26cf5cfe8c772d9359c91583b38"}, "sequence": 4294967295}]}"}

JSON-encoded string (backslash-escaped):
{"jsonData":"{\"locktime\": 0, \"outs\": [{\"value\": 10377032, \"script\": \"76a91436e325a5fe02032c2b08624850b9ae582a7ea54288ac\"}, {\"value\": 3444227, \"script\": \"76a9143cb419f785182f3112d5ba1e0b3df65c77630ddf88ac\"}], \"version\": 1, \"ins\": [{\"script\": \"473044022025565fa72b39e18e9150ddfb28a1f319f13ecda507a87aa48895703c19aa110802200fa6b915064ce6c1de82a4aa6c6129c75d2ab0b61eaf7f7d5de42aef1323bb53014104cc9a9c754f14e342dd03527a5a18f58cbb835127861ea70f9e169354deb68470c16887fdfc00c2c1555ba2ddfc256549e3b50ac18a4d53fee13df5ff57d389d0\", \"outpoint\": {\"index\": 0, \"hash\": \"1cb46e822f31ea8f29a0db0cb7314baacb63e26cf5cfe8c772d9359c91583b38\"}, \"sequence\": 4294967295}]}"}
```

Test data may be obtained from [blockchain.info](https://blockchain.info/). In particular, "?format=hex" may be placed at the end of a transaction URL. [Here's an example.](https://blockchain.info/tx/bb41a757f405890fb0f5856228e23b715702d714d59bf2b1feb70d8b2b4e3e08?format=hex)

# WebServerHashJSON
The second program (WebServerHashJSON) does two things. First, when given a POST request, the code accepts a JSON string and places it in a database, along with the SHA-256 hash of the string. Second, when given a GET request, the code checks to see if a JSON string with the given SHA-256 string resides in the database. If so, the server will return the JSON string. In both cases, errors will be returned if various standards aren't met.

**SOFTWARE REQUIREMENTS**:
Install the following packages in the following order but not before reading the installation instructions.

* [Python 2.7](https://www.python.org/)  (sudo apt-get install python-dev)
* [Apache2](https://httpd.apache.org/)  (sudo apt-get install apache2)
* [WSGI](https://code.google.com/archive/p/modwsgi/)  (sudo apt-get install libapache2-mod-wsgi)
* [SQLite](https://www.sqlite.org/)  (sudo apt-get install libsqlite3-0)
* [virtualenv](https://pypi.python.org/pypi/virtualenv)  (sudo apt-get install python-virtualenv)
* [Flask](http://flask.pocoo.org/)  (pip install Flask)  *venv*
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/)  (pip install flask-sqlalchemy)  *venv*
* [Whoosh](https://pypi.python.org/pypi/Whoosh/)  (pip install whoosh)  *venv*
* [Whoosh-Alchemy](https://pypi.python.org/pypi/Flask-WhooshAlchemy)  (pip install whoosh-alchemy (Ubuntu 15.10) *OR* pip install flask_whooshalchemy (Ubuntu 14.04))  *venv*
* [SQLAlchemy-migrate](https://pypi.python.org/pypi/sqlalchemy-migrate)  (pip install sqlalchemy-migrate)  *venv*

This code is tested only against 2.7. At least one piece of code may not run on Python 3, although this has not been tested. Ideally, code that runs on Python 2 should have a migration plan for when either Python 2 support is dropped or a decision is made to move to Python 3.

Note that all the *pip install* steps have a "venv" marking next to them. This is because it's highly recommended that these Python packages be installed only in a virtual environment. See the installation steps for more information.

**INSTALLATION STEPS (Linux)**:
The following steps apply to Linux. Run all the following commands in the same window. Note that this code has not yet been tested under Windows or OS X. In addition, note that usage of *virtualenv* is optional but [highly recommended by Flask's maintainers](http://flask.pocoo.org/docs/0.10/installation/).

* Ensure that Python, Apache, WSGI, and virtualenv are installed.
  * Once WSGI is installed, the command *sudo a2enmod wsgi* may need to be run to ensure that the module is picked up. Run it to be safe. In Ubuntu, this should be sufficient to ensure that Apache will pick up the module and start allowing it to be used.
* Follow the Flask recommendation to [set up virtualenv](http://flask.pocoo.org/docs/0.10/installation/). Run the following commands in order from this project's base directory.
  * *virtualenv venv*
  * *. venv/bin/activate*
* Use *pip* to install the aforementioned Python packages in the virtual environment.
* Run *python db_create.py* to create the SQLite database.
* Run *python WebServerHashJSON.py* to start the server.
* Once you're ready to quit the server, hit <CTRL+C> to quit.
* Execute *deactivate* to turn off the virtual environment created by *virtualenv*.
* If doing file cleanup once done with the server, executing *cleanup.sh* is the easiest thing to do.

By default the server runs at http://localhost:5000/ but can be deployed anywhere. This program is designed to partially complement *WebServerHashJSON*. In particular, this performs two functions.

### Send JSON data to the server ###
[cURL](http://curl.haxx.se/) is used to send JSON data to the server via a POST request. If the data doesn't already reside in the DB on the server, the JSON string will be added to the DB. The DB will also include a searchable key, which is a hex string of the SHA-256 hash of the JSON string. The following is an example of how to send the data.

`curl -X POST --data '{"jsonData":"{\"locktime\": 0, \"outs\": [{\"value\": 10377032, \"script\": \"76a91436e325a5fe02032c2b08624850b9ae582a7ea54288ac\"}, {\"value\": 3444227, \"script\": \"76a9143cb419f785182f3112d5ba1e0b3df65c77630ddf88ac\"}], \"version\": 1, \"ins\": [{\"script\": \"473044022025565fa72b39e18e9150ddfb28a1f319f13ecda507a87aa48895703c19aa110802200fa6b915064ce6c1de82a4aa6c6129c75d2ab0b61eaf7f7d5de42aef1323bb53014104cc9a9c754f14e342dd03527a5a18f58cbb835127861ea70f9e169354deb68470c16887fdfc00c2c1555ba2ddfc256549e3b50ac18a4d53fee13df5ff57d389d0\", \"outpoint\": {\"index\": 0, \"hash\": \"1cb46e822f31ea8f29a0db0cb7314baacb63e26cf5cfe8c772d9359c91583b38\"}, \"sequence\": 4294967295}]}"}' -H "Content-Type: application/json" http://localhost:5000/sendJSON`

The server expects JSON-encoded data. Note that the JSON key must be *jsonData*. In addition, due to command line escape requirements, you may have to backslash-escape single-and-double-quotations that are part of the JSON string. *HexTxToJSON* supplies such a string to simplify the process.

If the JSON string is successfully added to the DB, the following is an example of what will be seen.

```
Data added to the database.
Data = {"locktime": 0, "outs": [{"value": 10377032, "script": "76a91436e325a5fe02032c2b08624850b9ae582a7ea54288ac"}, {"value": 3444227, "script": "76a9143cb419f785182f3112d5ba1e0b3df65c77630ddf88ac"}], "version": 1, "ins": [{"script": "473044022025565fa72b39e18e9150ddfb28a1f319f13ecda507a87aa48895703c19aa110802200fa6b915064ce6c1de82a4aa6c6129c75d2ab0b61eaf7f7d5de42aef1323bb53014104cc9a9c754f14e342dd03527a5a18f58cbb835127861ea70f9e169354deb68470c16887fdfc00c2c1555ba2ddfc256549e3b50ac18a4d53fee13df5ff57d389d0", "outpoint": {"index": 0, "hash": "1cb46e822f31ea8f29a0db0cb7314baacb63e26cf5cfe8c772d9359c91583b38"}, "sequence": 4294967295}]}
SHA-256 hash = 71a6b7835f5c51ebc04f4e6ea5bbbf81b1ff33989aba22eb69e9fbd42511e122`
```

Due to time limitations, the only way to add data is via the *curl* command. Depending on an actual project's requirements, this may or may not be acceptable. A user-friendly web page is one example of a possible requirement. In such a case, Flask and other web frameworks are generally flexible enough to dynamically generate web pages that can successfully submit data to a DB.

If data already resides in the DB, successive adds will fail.

### Read JSON data from the server ###
The server may be queried for the JSON data via a GET request. In particular, going to */getJSON/<SHA-256 hash of the JSON string>* will return the accompanying JSON string or an error message. The following is an example of how to query the DB.

`curl http://localhost:5000/getJSON/52a0fed75416467ca26128b86702037f22203b2094f8ee80a34e71ffc2116de5`

For now, the returned JSON string isn't JSON-encoded, unlike what's required when sending the string to the DB. This may or may not be desirable depending on the project requirements.

# GENERAL NOTES #
Please note that this code isn't meant for a production environment, although the code has been kept clean and has been designed to simulate how production code might be deployed. As is, the code is simply a proof-of-concept designed to show the ability of Python to quickly and easily handle various tools in order to create useful programs, web pages, etc. Flask was chosen due to its simplicity and application in "microprojects" that require minimal server resources. In a production environment, a more robust web framework may be more desirable (e.g., Django), or possibly a framework written in a different language (e.g., Ruby on Rails). When considering a framework, many factors msut be considered, including but not limited to framework security, scalability, ability to interface with appropriate tools, and the compatibility of the framework with the overall design of the system. For example, if a [PostgreSQL/bcrypt combo](http://crafted-software.blogspot.com/2011/05/modern-way-to-store-passwords-bcrypt.html) is desired to support sensitive data, will the framework support PostgreSQL and bcrypt?

SQLite was chosen because it's a relatively simple DB that's portable and well-supported. It's also deployed in production environments where concurrency requirements aren't too critical. As such, SQLite is an excellent choice for this project. The DB is essentially "write-once," as the DB entries will never be altered once entries have been made. Again, in a production environment, it would be important to consider the system design and which DB would best interact with it.

Apache 2.x was chosen because it's the default deployment on Ubuntu. Some might argue that nginx is a better choice these days. Whether or not nginx is better, this project is designed to be deployable with as little manual operation by the user as possible.

A script (db_migrate.py) has been included to accommodate cases where the DB view is changed. It shouldn't be needed but is included as a courtesy.
