from __init__ import main as analyze
import pandas as pd


def main():
    df = pd.read_csv('corpus_textos_ensino.csv')
    content = {
        'letters': [],
        'characteres': [],
        'words': [],
        'sentences': [],
        'syllables': [],
        'complex_words': [],
        'flesch_pt': [],
        'gulpease': [],
        'flesch_kincaid': [],
        'gunning_pt': [],
        'automated_readability': [],
        'coleman_liau': []
    }

    for index, row in df.iterrows():
        content_unique = analyze(row['Texto'])

        for i in content_unique:
            for j in content_unique[i]:
                content[j].append(content_unique[i][j])

    for i in content:
        df[i] = content[i]

    print(df.head())
    df.to_csv("corpus_with_indexes.csv")


if __name__ == "__main__":
    main()
