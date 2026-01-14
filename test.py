import json

arbres = ["Paris", "Hauts-de-Seine"]

with open("data/arbres.json", "w") as f:
    json.dump(arbres, f)

print("Fichier arbres.json créé")
