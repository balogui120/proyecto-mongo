from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()
librosColeccion = conector.coleccion()

miquery = { "precio": 14.5 }
nuevosValores = { "$set": { "precio": 10.99 } }

resultado = librosColeccion.update_one(miquery, nuevosValores)
 
miquery = { "titulo": "1984" }
nuevosValores = { "$set": { "titulo": "Reina Roja" } }

resultado = librosColeccion.update_many(miquery, nuevosValores)

for libro in librosColeccion.find({ "titulo": "Reina Roja" }):
    print(libro)

