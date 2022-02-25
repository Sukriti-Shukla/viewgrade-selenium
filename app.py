from flask import Flask, jsonify, request
from flask_cors import CORS
import pymongo
from scrap.Scraper import scraper
import os

connection_url = 'mongodb+srv://sukriti-shukla:sukriti1@cluster0.rku1g.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
app = Flask(__name__)
client = pymongo.MongoClient(connection_url)

# Database
Database = client.get_database('Example')
# Table
SampleTable = Database.SampleTable

@app.route('/scrape', methods=['POST'])
def scrapeRoute()->str:
    rollNumber:str = None
    password:str = None
    data:str = None
    try:
        rollNumber = str(request.json["rollnumber"])
        password = str(request.json["password"])
        data = scraper(rollNumber, password)
    except KeyError:
        return "credentials not found"
    except Exception:
        return "server error"
    return data

@app.route('/', methods=['GET'])
def route()->str:
    content:str = None
    try:
        file = open("./index.html", 'r')
        content = file.read()
        file.close()
    except Exception as error:
        return str(error)
    return content

if __name__ == '__main__':
	app.run(debug=True)

