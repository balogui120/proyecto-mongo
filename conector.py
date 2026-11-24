from pymongo import MongoClient
from dotenv import load_dotenv
import os

class ConectorMongoDB():

    
    def conectarse(self):
        load_dotenv()

        usuario= os.getenv("USUARIO_MONGODB")
        password = os.getenv("PASSWORD_MONGODB")
        cluster= os.getenv("CLUSTER_MONGODB")
        dominio= os.getenv("DOMINIO_MONGODB")

        uri =  'mongodb+srv://'+usuario+':'+password+'@'+cluster+'.'+dominio+'.mongodb.net/?retryWrites=true&w=majority&appName='+cluster

        cliente = MongoClient(uri,maxPoolSize=50)

        
        return cliente

    def coleccion(self):  

        libreriaBD = self.conectarse()["libreria"]
        librosColeccion = libreriaBD["libros"]

        return librosColeccion