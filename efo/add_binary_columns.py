import pandas as pd

main_df = pd.read_csv("EFO_classes.csv", sep=",")
subset_df = pd.read_csv("EFO_biological_entity.csv", sep=",")

main_df = main_df[~main_df.LABEL.str.startswith("obsolete_")]

main_df["biological_entity"] = main_df["ID"].isin(subset_df["ID"]).astype(bool)

main_df.to_csv("EFO_classes_with_biological_entities.csv", sep=",", index=False)