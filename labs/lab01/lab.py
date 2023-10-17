# lab.py


import os
import io
import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# QUESTION 0
# ---------------------------------------------------------------------


def consecutive_ints(ints):
    if len(ints) == 0:
        return False

    for k in range(len(ints) - 1):
        diff = abs(ints[k] - ints[k+1])
        if diff == 1:
            return True

    return False


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def median_vs_mean(nums):
    mean = sum(nums) / len(nums)
    
    nums.sort()
    if len(nums) % 2 == 0: # if even length
        median = (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
    else: 
        median = nums[len(nums) // 2]
        
    if median <= mean: 
        return True
    else: 
        return False



# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def same_diff_ints(ints):
    if len(ints) == 0: 
        return False
    
    for i in range(len(ints)):
        for j in range(i + 1, len(ints)):
            if abs(ints[i] - ints[j]) == j - i:
                return True
    
    return False


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def n_prefixes(s, n):
    if len(s) == 0 or n == 0:
        return "" 
    
    result = ""
    for i in range(n, 0, -1): 
        result += s[:i]

    return result

# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def exploded_numbers(ints, n):
    if len(ints) == 0:
        return []
    elif n == 0:
        return ints
    
    digits = len(str(max(ints) + n))
    result = []
    
    for num in ints:
        exploded = [str(i).zfill(digits) for i in \
            range(num - n, num + n + 1)]
        result.append(' '.join(exploded))
    
    return result


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def last_chars(fh):
    result = ""
    content = fh.readlines()
    
    for line in content: 
        if len(line) > 1: 
            result += line[-2]
        
    return result


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def add_root(A):
    if len(A) < 2: 
        return A
    
    return A + np.sqrt(np.arange(len(A)))

def where_square(A):
    if len(A) == 0:
        return A
    
    root = np.sqrt(A)
    return root == root.astype(int)


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def growth_rates(A):
    if len(A) == 0:
        return np.array([])
    
    return np.round((A[1:] - A[:-1]) / A[:-1], 2)

def with_leftover(A):
    if len(A) == 0:
        return -1 
    
    leftover = 20 - (20 // A) * A
    cum = np.cumsum(leftover)
    days = np.where(cum >= A)[0]
    
    if len(days) > 0:
        return days[0]
    else: 
        return -1


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def salary_stats(salary):
    def func(name):
        n = name.split(' ')
        return n[1]

    results = {
        'num_players': salary.shape[0], 
        'num_teams': salary.groupby("Team").max().shape[0], 
        'total_salary': salary['Salary'].sum(), 
        'highest_salary': salary.sort_values(by="Salary", ascending=False) \
            .iloc[0]['Player'], 
        'avg_los': salary[salary['Team'] == "Los Angeles Lakers"] \
            ['Salary'].mean(), 
        'fifth_lowest': salary.sort_values(by="Salary").iloc[4]['Player'] + \
            ", " + salary.sort_values(by="Salary").iloc[4]['Team'], 
        'duplicates': salary['Player'].apply(func).unique().shape[0] != \
            salary.shape[0], 
        'total_highest': salary[salary['Team'] == salary.sort_values(by= \
        'Salary', ascending=False).iloc[0]['Team']]['Salary'].sum()
    }

    return pd.Series(results)


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def parse_malformed(fp):
    results = []
    with open('data/malformed.csv', 'r') as f_in:
            cols = f_in.readline().split(',')
            cols[-1] = cols[-1][:-1]
            for col in cols: 
                results.append([])
            
            lines = f_in.readlines()
            for line in lines: 
                line = line.replace(',,',',')
                line = line.replace('"','')
                line = line.strip(',')
                content = line.split(',')
                content[4] += "," + content[5][:-1]
                
                for i in range(len(results)):
                    results[i].append(content[i])

    df = pd.DataFrame.from_dict(dict(zip(cols, results)))
    convert_dict = {
        'first': str,
        'last': str,
        'weight': float,
        'height': float,
        'geo': str
    }
    df = df.astype(convert_dict)
    
    return df