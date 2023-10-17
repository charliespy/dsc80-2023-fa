# project.py


import pandas as pd
import numpy as np
import os


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def get_assignment_names(grades):
    dict = {}
    category = ['lab', 'project', 'midterm', 'final', 'disc', 'checkpoint']
    for elem in category:
        dict[elem] = []
    for col in grades.columns:
        for elem in category:
            if elem in col.lower():
                if len(col)- len(elem) < 3:
                    dict[elem].append(col)
    return dict
    
    

# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def projects_total(grades):
    grades_PID = grades.set_index('PID')
    grade_col = (grades_PID[[elem for elem in grades.columns 
                         if 'project' in elem 
                         and 'checkpoint' not in elem 
                         and 'Max' not in elem 
                         and 'Late' not in elem]])
    max_col = grades_PID[[elem for elem in grades.columns if 'project' in elem and 'Max' in elem]]
    late_col = grades_PID[[elem for elem in grades.columns if 'project' in elem and 'Late' in elem]]
    max_grade = sum(max_col.iloc[0])
    dict = {}
    for PID in grades_PID.index:
        grade_sum = 0
        for i in range(len(grade_col.columns)):
            if late_col[late_col.columns[i]].loc[PID] == '00:00:00':
                if np.isnan(grade_col[grade_col.columns[i]].loc[PID]):
                    grade_sum += 0
                else:
                    grade_sum += grade_col[grade_col.columns[i]].loc[PID]
        dict[PID] = grade_sum/max_grade
    dict
    return pd.Series(dict)
    
    


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def last_minute_submissions(grades):
    assignments = pd.Series(np.ones(9), index=['lab01', 'lab02', 'lab03', \
        'lab04', 'lab05', 'lab06', 'lab07', 'lab08', 'lab09'])
    labs = grades[[lab for lab in grades.columns if 'Lateness' in lab]]
    for i in range(1, 10):
        late_df = labs[labs['lab0' + str(i) + ' - Lateness (H:M:S)'] != \
            "00:00:00"]
        late_series = late_df['lab0' + str(i) + ' - Lateness (H:M:S)'] 
        assignments['lab0' + str(i)] = sum(np.array([ int(t.split(':')[0]) \
            for t in late_series]) < 10)
    return assignments  


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def lateness_penalty(series):
    def lateness_multiplier(time):
        hour = int(time.split(':')[0])
        if hour < 10:
            return 1.0
        elif hour <= 168:
            return 0.9
        elif hour <= 336:
            return 0.7
        else:
            return 0.4
        
    return series.apply(lateness_multiplier)
        
        
# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def process_labs(grades):
    ...


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def lab_total(processed):
    ...


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def total_points(grades):
    ...


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def final_grades(total):
    ...
    
def letter_proportions(total):
    ...


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def raw_redemption(final_breakdown, question_numbers):
    ...
    
def combine_grades(grades, raw_redemption_scores):
    ...


# ---------------------------------------------------------------------
# QUESTION 10
# ---------------------------------------------------------------------


def z_score(ser):
    ...
    
def add_post_redemption(grades_combined):
    ...


# ---------------------------------------------------------------------
# QUESTION 11
# ---------------------------------------------------------------------


def total_points_post_redemption(grades_combined):
    ...
    
def proportion_improved(grades_combined):
    ...
