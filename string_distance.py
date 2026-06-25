# Author: Ayush Rajbhandari
# Date: 6/24/26
# Assignment: Project 1
# Description: This script contains a function that calculates the Levenshtein distance similarity ratio between a list of strings and a target string.

from fuzzywuzzy import fuzz

def string_distance(str1, str2):
    # takes a list of strings, and a target string, returning a dictionary where the keys are the strings from the list and the values are the similarity ratios

    similarity_dictionary = {}

    for list_item in str1:

        similarity_score = fuzz.ratio(list_item, str2) #calculates similarity ratio between current list and target list

        similarity_dictionary[list_item] = similarity_score #adds to dictionary list

    return similarity_dictionary

if __name__ == '__main__':
    my_list = ['red', 'yellow', 'blue']
    result = string_distance(my_list, 'green')
    print(result)
