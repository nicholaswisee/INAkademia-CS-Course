"""
Filename: main.py
Nama: Nicholas Wise Saragih
Description: INAkademia Summer Bridge Computer Science Course Assignment 2 
"""

import statistics
import matplotlib.pyplot as plt


def zip_to_lists(*items):
    return [list(item) for item in zip(*items)] 
""""
To easily join functions together by zipping them and then turning the tuple into a string
"""

def get_scores_list():
    """"
    To make a list that stores the score of every student
    """
    
    with open('\exam1.txt', 'r') as file1:
        
        scores1 = []
        student_names = []        
        for line in file1:
            student_data1 = line.strip().split()
            scores1.append(student_data1[1])
            student_names.append(student_data1[0])
        
    
    with open('\exam2.txt', 'r') as file2:
        
        scores2 = []        
        for line in file2:
            student_data2 =  line.strip().split()
            scores2.append(student_data2[1])
        
        
    with open('\exam3.txt', 'r') as file3:
        
        scores3 = []        
        for line in file3:
            student_data3 =  line.strip().split()
            scores3.append(student_data3[1])
            
    student_scores = zip_to_lists(scores1, scores2, scores3)
    return(student_scores)

print(get_scores_list())
def get_student_names():
    """
    To get a list that contains the name of all students
    """
    
    with open('\exam1.txt', 'r') as file1:
        
        student_names = []        
        for line in file1:
            student_data1 =  line.strip().split()
            student_names.append(student_data1[0])
            
        return(student_names)


# Part A
def build_data(names, scores):
    """"
    Build a dictionary by taking in the list of names (key) and the list of scores (value)
    """
    
    student_data = {}
    i = 1

    while i < len(names):
        student_data[names[i]] = scores[i]
        i += 1
    
    return student_data

# print(build_data(get_student_names(), get_scores_list()))
    
# Part B
def calc_final_score(scores):
    """ 
    Calculate the final scores and put it into a list
    """
    final = []
    for score in scores:
        if score[0] != "Score":
            score1 = float(score[0])
            score2 = float(score[1])
            score3 = float(score[2])
        
            final_score = round(0.3 * score1 + 0.3 * score2 + 0.4 * score3, 2)
            final.append(final_score)
    
    return final
    
    
def build_data_final(names, scores):
    """ 
    Build a dictionary from the names (key) list and the final scores (value) list
    """
    
    student_data = {}
    i = 1
    final_scores = calc_final_score(scores)
    while i < len(names):
        student_data[names[i]] = final_scores[i - 1]
        i += 1
    
    return student_data
# print(build_data_final(get_student_names(), get_scores_list()))


# Part C
def calculate_average(grades):
    """" 
    Generate a new list that contains the average of a score every student
    """
    
    average_list = []
    for score in grades:
            if score[0] != "Score":
                score1 = float(score[0])
                score2 = float(score[1])
                score3 = float(score[2])
                average_score = round(score1 / 3 + score2 / 3 + score3 / 3, 2)
                average_list.append(average_score)
    
    return average_list

# print(calculate_average(get_scores_list()))

# Part D
def calculate_std(grades):
    """ 
    Generate a list that contains the standard deviation of every student
    """
    
    average = calculate_average(grades)
    i = 0
    std_list = []
    for score in grades:
        if score[0] != "Score":
                score1 = float(score[0])
                score2 = float(score[1])
                score3 = float(score[2])
                float_list = [score1, score2, score3]
                std_calc = statistics.stdev(float_list, xbar = average[i])
                std_list.append(std_calc)
                i += 1
    return std_list

# print(calculate_std(get_scores_list()))

# Part E
def plot_final_grades():
    
    """ 
    Plot a histogram according to the acquired final scores
    """
    grades = calc_final_score(get_scores_list())
    
    plt.hist(grades, edgecolor= "black")
    
    plt.title('Histogram of Final Scores')
    plt.xlabel('Final Scores')
    plt.ylabel('Frequency')
    
    plt.show()
     
# plot_final_grades()
# Part F

def get_letter_grade():
    
    """" 
    Determine the letter grade based on the given parameters associated with final grades, average, and standard deviation  
    """

    final_grades = calc_final_score(get_scores_list())
    average = calculate_average(get_scores_list())
    std = calculate_std(get_scores_list())
    
    letter_grades = []
        
    grade_std_average = zip_to_lists(final_grades, average, std)
    for data in grade_std_average:
        grade = data[0]
        avg = data[1]
        std_dev = data[2] 
        
        if avg + 1.5 * std_dev >= 100:
            letter_grades.append("A") 
        elif (avg + 0.5 * std_dev) <= grade < (avg + 1.5 * std_dev):
            letter_grades.append("B")
        elif avg - 0.5 * std_dev <= grade < avg + 0.5 * std_dev:
            letter_grades.append("C")
        elif avg - 1.5 * std_dev <= grade < avg - 0.5 * std_dev:
            letter_grades.append("D")
        elif grade < avg - 1.5 * std_dev:
            letter_grades.append("F") 
            
    return letter_grades

# print(get_letter_grade())
    
def determine_letter_grades():
    
    """" 
    Create a dictionary containing the names (key) and the letter grade (value) of every student
    """
    student_data = {}
    names = get_student_names()
    letter_grades = get_letter_grade()
    i = 1   
        
    while i < len(names):
    
        student_data[names[i]] = letter_grades[i - 1]
        i += 1
    return student_data

# print(determine_letter_grades())


    



