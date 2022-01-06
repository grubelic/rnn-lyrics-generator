import loader
import pandas as pd


def print_weird_stuff(df: pd.DataFrame) -> None:
    # work in progress
    for text in df.lyrics:
        for word in text.strip().split():
            w: str = word.replace('\'', '')
            if w.isalpha()\
                or w.endswith('.') or w.endswith(',') or w.endswith('?'):
                continue
            print(w)


def print_artists(df: pd.DataFrame) -> None:
    print("\n".join(sorted(set(df.artist))))


def get_lyrics(df: pd.DataFrame, artist: str, title: str) -> str:
    return next(iter(df[(df.artist == artist) & (df.title == title)].lyrics))


def get_song_names_by(df: pd.DataFrame, artist: str) -> pd.Series:
    return df[(df.artist == artist)].title


if __name__ == "__main__":
    # loader.replace_in_file(loader.KAGGLE_POETRY_PATH, b"\r", b"")
    # data = loader.load_kaggle_poetry()
    # lyrics = get_lyrics(data, "Connie Wanek", "Hartley Field")
    # print(lyrics)
    # print([it if it.isalpha() else ord(it) for it in lyrics])
    data = loader.load_kaggle_150k()
    # print(get_song_names_by(data, "Eminem"))
    # print(get_lyrics(data, "Eminem", "Infinite"))
    print_weird_stuff(data)


