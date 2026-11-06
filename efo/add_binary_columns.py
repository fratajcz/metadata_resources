import pandas as pd

main_df = pd.read_csv("EFO_classes.csv", sep=",")
subset_df = pd.read_csv("EFO_biological_entity.csv", sep=",")

main_df = main_df[~main_df.LABEL.str.startswith("obsolete_")]

main_df["biological_entity"] = main_df["ID"].isin(subset_df["ID"]).astype(bool)
print("Biological entities before adding UBERON, CLO and CL: ", main_df["biological_entity"].sum())
helper = []
for i, row in main_df.iterrows():
    if row["ID"].startswith("UBERON:") or row["ID"].startswith("CLO:") or row["ID"].startswith("CL:"):
        helper.append(True)
    else:
        helper.append(row["biological_entity"])
main_df["biological_entity"] = helper
print("Biological entities after adding UBERON, CLO and CL: ", main_df["biological_entity"].sum())

main_df.to_csv("EFO_classes_with_biological_entities.csv", sep=",", index=False)