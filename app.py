from flask import Flask
from waitress import serve
import pymongo

client = pymongo.MongoClient("mongodb+srv://atlas-db-user-1641158466980233578:NvS08*=y@cluster0.brwd1.mongodb.net/mystrj?retryWrites=true&w=majority")
db = client.mystrk

app = Flask(__name__)

@app.route('/')
def hello():
    return db.tracks.find_one()

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
