from pymongo import MongoClient
import config

client = MongoClient(config.mongo)
db = client[config.bdd]
col = db[config.nom]

for arbre in col.find().limit(10):
    print(arbre["nom_latin"], arbre["hauteur_m"], arbre["commune"])
