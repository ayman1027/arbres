import pandas as pd

paris = pd.read_csv("data-raw/paris.csv", sep=";", encoding="utf-8-sig")
idf = pd.read_csv("data-raw/idf.csv", sep=";", encoding="utf-8-sig")

# Filtre remarquable DANS le code
paris = paris[paris["REMARQUABLE"].astype(str).str.upper() == "OUI"]
idf = idf[idf["CRITERE_GENERAL"].fillna("").astype(str).str.strip().ne("") | idf["CRITERE_AUTRE"].fillna("").astype(str).str.strip().ne("")]

# Harmonisation des colonnes
paris = paris[["ESPECE","HAUTEUR (m)","CIRCONFERENCE (cm)","geo_point_2d"]].copy()
paris["source"] = "Paris"
paris["commune"] = "Paris"
paris["code_insee"] = ""

idf = idf[["CODE_INSEE","COMMUNE","NOM_LATIN","HAUTEUR","CIRCONFERENCE","geo_point_2d"]].copy()
idf["source"] = "IDF"

paris.columns = ["nom_latin","hauteur_m","circonference_cm","localisation","source","commune","code_insee"]
idf.columns = ["code_insee","commune","nom_latin","hauteur_m","circonference_cm","localisation","source"]

pd.concat([paris, idf], ignore_index=True)[
    ["source","commune","code_insee","nom_latin","hauteur_m","circonference_cm","localisation"]
].to_json("data/arbres.json", orient="records", force_ascii=False, indent=2)

print("arbres.json généré ")
