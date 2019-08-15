# Program extracting first colum

import os
from flask import Flask
from flask import request

from vkservices.vk import *

app = Flask(__name__)

@app.route('/vkosha/findwordold/<wordtofind>',methods=['GET'])
def findwordold(wordtofind):
	retstring = ", "
	print('The given word is : ' + wordtofind)
	vkObj = get_synonyms(wordtofind)
	retstring = vkObj.synset
	return retstring

@app.route('/vkosha/findwordold2/<wordtofind>',methods=['GET'])
def findwordold2(wordtofind):
	retstring = ", "
	print('The given word is : ' + wordtofind)
	vkObj = get_synonyms(wordtofind)
	retstring = printJsonOutput(vkObj)
	return retstring

@app.route('/vkosha/findword/<wordtofind>',methods=['GET'])
def findword(wordtofind):
	retstring = ", "
	print('The given word is : ' + wordtofind)
	vkArrayOutput = get_synonyms(wordtofind, "null")
	retstring = printJsonOutput(vkArrayOutput)
	return retstring

@app.route('/vkosha/helloworld',methods=['GET'])
def vkHello():
	return "Hello World!"

if __name__ == '__main__':
	app.run()
