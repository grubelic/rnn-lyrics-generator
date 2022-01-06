import pandas as pd

KAGGLE_150K_PATH = "../datasets/labeled_lyrics_cleaned.csv"
KAGGLE_POETRY_PATH = "../datasets/PoetryFoundationData.csv"
KAGGLE_LD = "../datasets/LYRICS_DATASET.csv"


def load_kaggle_150k(path: str = KAGGLE_150K_PATH) -> pd.DataFrame:
    """
    Load the Kaggle "150K Lyrics Labeled with Spotify Valence" dataset
    https://www.kaggle.com/edenbd/150k-lyrics-labeled-with-spotify-valence

    :param path: path to the dataset
    :return: dataframe with 3 columns: artist, lyrics, title
    """
    df = pd.read_csv(
        path,
        usecols=["artist", "seq", "song"],
        skipinitialspace=True
    )
    df.rename(columns={"seq": "lyrics", "song": "title"}, inplace=True)
    df.drop_duplicates(inplace=True, ignore_index=True)
    return df


def replace_in_file(path: str, old: bytes, new: bytes) -> None:
    """
    Replace all occurrences of old bytes with new bytes in a file whose path
    is provided. Currently, loads the whole file in RAM.

    :param path: path to the file whose content is being replaced
    :param old: bytes that need to be replaced
    :param new: bytes that need to be added
    :return:
    """
    with open(path, 'rb') as inf:
        data = inf.read().replace(old, new)
    with open(path, 'wb') as outf:
        outf.write(data)


def load_kaggle_poetry(path: str = KAGGLE_POETRY_PATH) -> pd.DataFrame:
    """
    Load the Kaggle "Poetry Foundation Poems" dataset
    https://www.kaggle.com/tgdivy/poetry-foundation-poems

    :param path: path to the dataset
    :return: dataframe with 3 columns: artist, lyrics, title
    """
    df = pd.read_csv(
        path,
        usecols=["Title", "Poem", "Poet"],
        skipinitialspace=True
    )
    df.rename(columns={"Poem": "lyrics", "Title": "title", "Poet": "artist"},
              inplace=True)
    df.title = df.title.str.strip()
    df.drop_duplicates(inplace=True, ignore_index=True)
    return df

# TODO u jednu funkciju koju pozivaju ostale
def load_kaggle_lyrics_dataset(path: str = KAGGLE_LD) -> pd.DataFrame:
    """
    Load the Kaggle "Poetry Foundation Poems" dataset
    https://www.kaggle.com/tgdivy/poetry-foundation-poems

    :param path: path to the dataset
    :return: dataframe with 3 columns: artist, lyrics, title
    """
    df = pd.read_csv(
        path,
        usecols=["Song Name", "Lyrics", "Artist Name"],
        skipinitialspace=True
    )
    df.rename(columns={"Lyrics": "lyrics", "Song Name": "title", "Artist Name": "artist"},
              inplace=True)
    # df.title = df.title.str.strip()
    df.drop_duplicates(inplace=True, ignore_index=True)
    return df

