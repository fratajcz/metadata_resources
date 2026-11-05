import pandas as pd

main_df = pd.read_csv("fbbi-classes.csv", sep=",")
subset_df = pd.read_csv("fbbi-imaging-methods.csv", sep=",")

main_df["imaging_method"] = main_df["ID"].isin(subset_df["ID"]).astype(bool)

main_df.to_csv("fbbi-classes-with-imaging-methods.csv", sep=",", index=False)