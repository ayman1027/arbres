import pandas as pd

paris = pd.read_csv("data-raw/paris.csv", sep=";", encoding="utf-8-sig")
idf = pd.read_csv("data-raw/idf.csv", sep=";", encoding="utf-8-sig")

paris = paris[paris["REMARQUABLE"].astype(str).str.upper() == "OUI"]
idf = idf[
    idf["CRITERE_GENERAL"].fillna("").astype(str).str.strip().ne("")
    | idf["CRITERE_AUTRE"].fillna("").astype(str).str.strip().ne("")
]

paris = paris[["ARRONDISSEMENT", "ESPECE", "HAUTEUR (m)", "CIRCONFERENCE (cm)", "geo_point_2d"]].copy()

paris["arr_num"] = paris["ARRONDISSEMENT"].astype(str).str.extract(r"PARIS\s+(\d+)")[0]
paris["code_insee"] = "75" + paris["arr_num"].fillna("").astype(str).str.zfill(3)

paris_out = pd.DataFrame({
    "source": "Paris",
    "commune": "Paris",
    "code_insee": paris["code_insee"],
    "nom_latin": paris["ESPECE"],
    "hauteur_m": paris["HAUTEUR (m)"],
    "circonference_cm": paris["CIRCONFERENCE (cm)"],
    "localisation": paris["geo_point_2d"],
})

idf = idf[["CODE_INSEE", "COMMUNE", "NOM_LATIN", "HAUTEUR", "CIRCONFERENCE", "geo_point_2d"]].copy()
idf_out = pd.DataFrame({
    "source": "IDF",
    "commune": idf["COMMUNE"],
    "code_insee": idf["CODE_INSEE"],
    "nom_latin": idf["NOM_LATIN"],
    "hauteur_m": idf["HAUTEUR"],
    "circonference_cm": idf["CIRCONFERENCE"],
    "localisation": idf["geo_point_2d"],
})

final = pd.concat([paris_out, idf_out], ignore_index=True)
final.to_json("data/arbres.json", orient="records", force_ascii=False, indent=2)

print("OK : data/arbres.json généré")
print("records:", len(final))
