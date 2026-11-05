import pandas as pd

main_df = pd.read_csv("NCBITAXON.csv", sep=",")

#main_df["Class ID"] = "NCBITAXON:" + main_df["Class ID"].str.split("/").str[-1]

main_df = main_df[main_df["RANK"].isin(["species", "subspecies"])]
main_df = main_df[main_df["Obsolete"] == False]
main_df = main_df[main_df["DIV"].isin(["Vertebrates", "Mammals", "Primates", "Rodents"])]
main_df.drop(columns=["RANK", "Synonyms","Obsolete", "DIV","CUI","Parents","Authority name", "Semantic type UMLS property", "Definitions", "Semantic Types"], inplace=True)

english_df = pd.read_csv("species-english-mapping.tsv", sep="\t")

main_df = main_df.merge(english_df, left_on="Preferred Label", right_on="latin_species_name", how="left")
main_df.drop(columns=["latin_species_name"], inplace=True)
main_df.to_csv("NCBITAXON-species.csv", sep=",", index=False)