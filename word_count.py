"""Taller evaluable"""

import glob

import pandas as pd


def load_input(input_directory):

    filesnames: list = glob.glob(f"{input_directory}/*.txt")

    dataframes: list = [
        pd.read_csv(filename, sep='\t', header=None, names=['text'])
        for filename in filesnames
        ]
    concatenated_df: pd.DataFrame = pd.concat(dataframes, ignore_index=True)
    return concatenated_df


def clean_text(dataframe):

    """Text cleaning"""

    dataframe: pd.DataFrame = dataframe.copy()
    dataframe['text'] = dataframe['text'].str.lower()
    dataframe['text'] = dataframe['text'].str.replace(',', '')
    dataframe['text'] = dataframe['text'].str.replace('.', '')
    return dataframe


def count_words(dataframe):
    """Word count"""

    dataframe: pd.DataFrame = dataframe.copy()
    dataframe['text'] = dataframe['text'].str.split()
    dataframe = dataframe.explode('text')
    dataframe = dataframe['text'].value_counts().reset_index()
    # ----> Manera alternativa para contar los valores de las palabras:
    #dataframe['count'] = 1  
    #dataframe = dataframe.groupby('text').agg({'count':'sum'})
    return dataframe


def save_output(dataframe, output_filename):
    """Save output to a file."""

    dataframe.to_csv(output_filename, sep='\t', index=False, header=False)



def run(input_directory, output_filename):
    """Call all functions."""

    df = load_input(input_directory)
    df = clean_text(df)
    df = count_words(df)
    save_output(df, output_filename)


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
