import pandas as pd

#TODO: add a proper doc-comment

# Loads dataset from path into a pandas dataframe
# returns pd.DataFrame with 3 columns: artist, seq and song
def load_dataset(path="datasets/labeled_lyrics_cleaned.csv"):
    return pd.read_csv(path).drop(columns=["label", "Unnamed: 0"])
    

