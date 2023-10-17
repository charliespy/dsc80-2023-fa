# lab.py


import pandas as pd
import numpy as np
import os


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def data_load(scores_fp):
    df = pd.read_csv('data/scores.csv')
    df = (df[['name', 'tries', 'highest_score', 'sex']]
        .drop(columns=['sex'])
        .rename(columns={'name': 'firstname', 'tries': 'attempts'})
        .set_index('firstname')
    )
    return df

def pass_fail(scores):
    def determine_pass(row): 
        att = row['attempts']
        sc = row['highest_score']
        
        if att > 1 and sc < 60:
            return 'No'
        elif att > 4 and sc < 70: 
            return 'No'
        elif att > 6 and sc < 90:
            return 'No'
        elif att > 8:
            return 'No'
        else: 
            return 'Yes'
    
    df_copy = (scores.copy()
               .assign(hi = scores.apply(determine_pass, axis=1))
               .rename(columns={'hi':'pass'})
    )
    return df_copy


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def med_score(scores):
    return np.median(scores[scores['pass'] == 'Yes']['highest_score'])

def highest_score_name(scores):
    max_score = scores.sort_values(
        by='highest_score', ascending=False).iloc[0]['highest_score']
    names_list = list(scores[scores['highest_score'] == max_score].index)
    return (max_score, names_list)


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def idx_dup():
    return 6


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def trick_me():
    return 3

def trick_bool():
    return [4, 10, 13]


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def change(x):
    if np.isnan(x):
        return 'MISSING'
    else:
        return x
    
def correct_replacement(df_with_nans):
    def c(x):
        if np.isnan(x):
            return 'MISSING'
        else:
            return x
        
    result = df_with_nans.copy()
    return result.applymap(c) 
    
def missing_ser():
    return 2
    
def fill_ser(df_with_nans):
    for c in df_with_nans.columns:
        df_with_nans.loc[df_with_nans[c].isna(), c] = 'MISSING'


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def population_stats(df):    
    num_nonnull = df.count()
    prop_nonnull = num_nonnull/len(df)
    num_distinct = df.nunique()
    prop_distinct = num_distinct/df.count()
    
    result_df = pd.DataFrame({
        'num_nonnull': num_nonnull,
        'prop_nonnull': prop_nonnull,
        'num_distinct': num_distinct,
        'prop_distinct': prop_distinct
    })
    
    return result_df


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def most_common(df, N=10):
    result_df = pd.DataFrame(index=range(N))

    for col in df.columns:
        common_values = df[col].value_counts().head(N)
        if len(common_values) < N:
            for i in range(N - len(common_values)): 
                common_values.append(pd.Series({np.NaN: np.NaN}))
        
        temp_df = pd.DataFrame({f'{col}_values': common_values.index, 
                                f'{col}_counts': common_values.values})

        result_df = pd.concat([result_df, temp_df], axis=1)

    return result_df


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def super_hero_powers(powers):
    powers = powers.set_index('hero_names')
    
    first = powers.sum(axis=1).idxmax()

    fly = powers[powers['Flight'] == True]
    fly = fly.drop(columns=['Flight'])
    second = fly.sum().idxmax()

    one = powers[powers.sum(axis=1) == 1]
    third = one.sum().idxmax()
    
    return [first, second, third]


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def clean_heroes(heroes):
    return heroes.replace(['-', -99.0, ' '], np.NaN)


# ---------------------------------------------------------------------
# QUESTION 10
# ---------------------------------------------------------------------


def super_hero_stats():
    return ['Onslaught', 'George Lucas', 'bad', 'Marvel Comics', \
        'NBC - Heroes', 'Groot']
