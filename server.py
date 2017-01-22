from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://heroku_92mpb6t1:hu4m23dvt4sodep65s0ogid5nl@ds147167.mlab.com:47167/heroku_92mpb6t1')
    db = client.heroku_92mpb6t1
    return db