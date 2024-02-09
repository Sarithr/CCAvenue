from CryptographyAES import *
import hashlib
from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode
import os
from Cryptodome.Random import get_random_bytes
import pyaes, pbkdf2, binascii, os, secrets
from flask import Flask, request
import json
import logging

logging.basicConfig(level = logging.DEBUG)

class CCAvenueConnector:
	def billing(self, pname, request):
		merchant_id = "2193"
		access_code = "F94007DF1640D69A" 
		enc_key = "FABE114254BDBC7823534894FFFCCC1" 
		ccaRequest = ""
		pname = ""
		pvalue = ""	
		pvalue = pname
		ccaRequest = ccaRequest + pname + "=" + pvalue + "&"
		aesUtil = encrypt(enc_key)
		encRequest = aesUtil.encrypt(ccaRequest)
		logging.debug(encRequest)

ccavenueObject = CCAvenueConnector()		
ccavenueObject.billing("Bill 1", "POST")
'''app = Flask(__name__)
ccavenueObject = CCAvenueConnector()

@app.route('/billing', methods = ['POST'])
def doBilling():
	return json.dumps(ccavenueObject.billing())

if __name__ == '__main__':
	logging.basicConfig(level = logging.DEBUG)
	app.run(debug = True)'''		