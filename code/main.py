from pprint import pprint

import loader
import pandas as pd
from keras.preprocessing.text import Tokenizer
import re


def print_weird_stuff(df: pd.DataFrame) -> None:
    # work in progress
    for index, row in df.iterrows():
        for word in row.lyrics.strip().split():
            w: str = word.replace('\'', '')
            if w.isalpha() or w.endswith('.') or w.endswith(',') or w.endswith('?'):
                continue
            print(w, row.artist)


def print_artists(df: pd.DataFrame) -> None:
    print("\n".join(sorted(set(df.artist))))


def get_lyrics(df: pd.DataFrame, artist: str, title: str) -> str:
    return next(iter(df[(df.artist == artist) & (df.title == title)].lyrics))


def get_song_names_by(df: pd.DataFrame, artist: str) -> pd.Series:
    return df[(df.artist == artist)].title


def clean_lyrics(df: pd.DataFrame) -> None:
    in_brackets = re.compile(r"\[[^\n\]]*]")
    """
    for lyrics in df.lyrics:
        found = in_brackets.findall(lyrics)
        if found: print(found)"""
    df.lyrics = df.lyrics.apply(lambda x: in_brackets.sub('\n', x))


if __name__ == "__main__":
    # loader.replace_in_file(loader.KAGGLE_POETRY_PATH, b"\r", b"")
    # loader.replace_in_file(loader.KAGGLE_150K_PATH, b"\r", b"")
    # data = loader.load_kaggle_poetry()
    # lyrics = get_lyrics(data, "Connie Wanek", "Hartley Field")
    # print(lyrics)
    # print([it if it.isalpha() else ord(it) for it in lyrics])
    data = loader.load_kaggle_150k()
    clean_lyrics(data)
    lyrics = get_lyrics(data, "LL Cool J", "#1 Fan")
    t = Tokenizer()
    t.fit_on_texts([lyrics])
    print(lyrics)
    pprint(t.word_index)
    # print(get_song_names_by(data, "Eminem"))
    # print(get_lyrics(data, "Eminem", "Infinite"))
    # print([it if it.isalpha() else ord(it) for it in get_lyrics(data, "Phoebe Bridgers", "Motion Sickness")])
    # print_weird_stuff(data)


