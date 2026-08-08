import numpy as np
import pandas as pd


def extract_surface_metrics(df):
    """Calculates character counts, word counts, average word lengths,

    and relative differences between response_a and response_b.
    """
    df = df.copy()

    # Fill missing values
    for col in ["prompt", "response_a", "response_b"]:
        df[col] = df[col].fillna("").astype(str)

    # Character lengths
    df["prompt_char_len"] = df["prompt"].str.len()
    df["response_a_char_len"] = df["response_a"].str.len()
    df["response_b_char_len"] = df["response_b"].str.len()

    # Word counts
    df["prompt_word_count"] = df["prompt"].apply(lambda x: len(x.split()))
    df["response_a_word_count"] = df["response_a"].apply(lambda x: len(x.split()))
    df["response_b_word_count"] = df["response_b"].apply(lambda x: len(x.split()))

    # Average word lengths
    df["response_a_avg_word_len"] = df["response_a_char_len"] / (
        df["response_a_word_count"] + 1e-5
    )
    df["response_b_avg_word_len"] = df["response_b_char_len"] / (
        df["response_b_word_count"] + 1e-5
    )

    # Relative difference features (Response A minus Response B)
    df["len_diff_char"] = df["response_a_char_len"] - df["response_b_char_len"]
    df["len_diff_word"] = df["response_a_word_count"] - df["response_b_word_count"]

    # Relative ratio features
    df["len_ratio_char"] = (df["response_a_char_len"] + 1) / (
        df["response_b_char_len"] + 1
    )
    df["len_ratio_word"] = (df["response_a_word_count"] + 1) / (
        df["response_b_word_count"] + 1
    )

    return df
