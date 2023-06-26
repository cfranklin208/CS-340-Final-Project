from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        
        USER = 'root'
        PASS = 'Gdpn1lerK3'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30008
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            success = self.database.animals.insert(data)  # data should be dictionary   
            if success != 0:
                return True
            else:
                return False    
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Read method to implement the R in CRUD. 
    def read(self, search):
        if search is not None:
            data = self.database.animals.find(search, {"_id" : False})
        else:
            data = self.database.animals.find( {}, {"_id" : False})
        return data
        
# Update method to implement the U in CRUD.
    def update(self, sData, uData):
        if sData is not None:
            uResult = self.database.animals.update_many(sData, {"$set" : uData})
        else:
            return "{}"
        return uResult
    
# Delete method to implement the D in CRUD.
    def delete(self, dData):
        if dData is not None:
            dResult = self.database.animals.delete_many(dData)
        else:
            return "{}"
            print("No Data Found")
        return dResult