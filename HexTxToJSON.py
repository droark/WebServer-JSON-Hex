# (c) 2016 Douglas Roark (joroark@vt.edu)
# Copy far and wide, intrepid coder.
#
# The following is a simple program designed to take a hex-encoded Bitcoin
# transaction and translate the hex encoding into JSON encoding. The following
# is an abbreviated example of how to use the program.
#
# python HexTxToJSON.py 0100000001383b58919c35d972c7e8cff56c.....
#
# There are various assumptions, explicit and implicit, described in README.md.
#
# Usage of sys.argv isn't optimal but it can be deployed universally. argpoint
# is far better but also more complicated to use.
import sys
import string
import json
import decimal
from bitcoin.transaction import deserialize

# Max Bitcoin Tx is technically 999,919 bytes (1000000-80-1).
BITCOIN_MAX_TX_LEN     = 999919
BITCOIN_MAX_TX_LEN_HEX = BITCOIN_MAX_TX_LEN * 2

# Borrowed from Armory (https://github.com/etotheipi/BitcoinArmory - armoryd.py).
# Some non-twisted json imports from jgarzik's code and his UniversalEncoder
class UniversalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

# Check the # of inputs.
if len(sys.argv) != 2:
    print "Please execute the program as follows: python Prob1-HexTxToJSON.py " \
        "*hex-encoded transaction*"
    sys.exit()

# For now, Bitcoin enforces a ~1,000,000 byte Tx limit (100,000 bytes is
# "standard" but larger transactions have been seen.) Enforce it here. It also
# acts as a way to prevent the input length from crushing the system. A
# production system may want to perform further input validation to ensure that
# the Tx input isn't malicious, malleable, etc.
if len(sys.argv[1]) > BITCOIN_MAX_TX_LEN_HEX:
    print "The transaction is larger than 999,919 bytes. Therefore, the " \
        "transaction is not a valid Bitcoin transaction."
    sys.exit()

# Check to make sure the input string is actually a hex string.
if all(txChars in string.hexdigits for txChars in sys.argv[1]) == False:
    print "The hex Tx string has non-hex characters. Please check the string."
    sys.exit()

# Ideally, there would be a function that would make sure the incoming hex
# string would be validated to make sure that it's an actual Bitcoin
# transaction. Unfortunately, pybitcointools doesn't appear to have this
# functionality. So, we have to fly blind. We'll account for this as best we can
# by catching any errors and just assuming it's a bad input string. This isn't
# ideal. It works for now, though.
#
# Call the function that generates the JSON output, and then output the JSON
# string as one line and as a more readable, tab-delimited piece of text.
try:
    txResult = deserialize(sys.argv[1])
    print '\nRaw JSON string:'
    print json.dumps(txResult)
    print '\nIndented JSON string:'
    print json.dumps(txResult, indent=4, sort_keys=True, cls=UniversalEncoder)
    print '\nJSON-encoded string:'
    print '{\"jsonData\":\"%s\"}' % json.dumps(txResult)
    print '\nJSON-encoded string (backslash-escaped):'
    print '{\"jsonData\":\"%s\"}' % json.dumps(txResult).replace('"', r'\"')
except:
    print 'The hex input string isn\'t a valid Bitcoin Tx. Please double ' \
        'check the input string.'
