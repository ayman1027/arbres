import pandas as pd

paris = pd.read_csv("data-raw/paris.csv", sep=";", encoding="utf-8-sig")
idf = pd.read_csv("data-raw/idf.csv", sep=";", encoding="utf-8-sig")

paris = paris[paris["REMARQUABLE"].astype(str).str.upper() == "OUI"]
idf = idf[idf["CRITERE_GENERAL"].fillna("").astype(str).str.strip().ne("") | idf["CRITERE_AUTRE"].fillna("").astype(str).str.strip().ne("")]

paris = paris[["IDBASE","LIBELLE FRANCAIS","ESPECE","HAUTEUR (m)","CIRCONFERENCE (cm)","geo_point_2d","ARRONDISSEMENT","DOMANIALITE"]]
idf = idf[["MATRICULE","NOM_FRANCAIS","NOM_LATIN","HAUTEUR","CIRCONFERENCE","geo_point_2d","COMMUNE","DOMAINE"]]

paris.columns = idf.columns = ["id","nom","espece","hauteur","circonference","localisation","zone","domaine"]
paris["source"], idf["source"] = "Paris", "IDF"

pd.concat([paris, idf], ignore_index=True).to_json("data/arbres.json", orient="records", force_ascii=False, indent=2)
print("OK: data/arbres.json généré")
