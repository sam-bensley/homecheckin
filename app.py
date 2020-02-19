from flask import Flask
import pickle
from homeModel import *
import json

app = Flask(__name__)

@app.route('/set/<name>/<home>')
def setHome(name, home):
    try:
        pickledFile = open("home.pickle","rb")
        homeDB = pickle.load(pickledFile)
        pickledFile.close()
    except:
        homeDB = homeModel()

    if (name == "Sam"):
        if (home == "T"):
            homeDB.setSam(True)
        else:
            homeDB.setSam(False)
    elif (name == "Isaac"):
        if (home == "T"):
            homeDB.setIsaac(True)
        else:
            homeDB.setIsaac(False)
    elif (name == "Toby"):
        if (home == "T"):
            homeDB.setToby(True)
        else:
            homeDB.setToby(False)
    elif (name == "Oli"):
        if (home == "T"):
            homeDB.setOli(True)
        else:
            homeDB.setOli(False)

    #save file
    outFile = open("home.pickle","wb")
    pickle.dump(homeDB, outFile)
    outFile.close()

    return "DONE"

@app.route('/get/<name>')
def getHome(name):
    try:
        pickledFile = open("home.pickle","rb")
        homeDB = pickle.load(pickledFile)
        pickledFile.close()
    except:
        return json.dumps(False)

    if (name == "Sam"):
        return json.dumps(homeDB.getSam())
    elif (name == "Isaac"):
        return json.dumps(homeDB.getIsaac())
    elif (name == "Oli"):
        return json.dumps(homeDB.getOli())
    elif (name == "Toby"):
        return json.dumps(homeDB.getToby())
    else:
        return "Dunno"
    
app.run()
