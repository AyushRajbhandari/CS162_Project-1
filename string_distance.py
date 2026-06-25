# Name: Ayush Rajbhandari
# Date: 6/24/26
# Assignment: Project 1
# Description: This script contains a function that calculates the Levenshtein distance similarity ratio between a list of strings and a target string.

from fuzzywuzzy import fuzz

def string_distance(string_list, target_string):
    """
    Takes a list of strings and a target string, and returns a dictionary where the keys are the strings
    from the list, and the values are the similarity ratio
    """

    similarity_dictionary = {}

    for list_item in string_list:

        similarity_score = fuzz.ratio(list_item, target_string) #calculates similarity ratio between current list and target list

        similarity_dictionary[list_item] = similarity_score #adds to dictionary list

    return similarity_dictionary

if __name__ == '__main__':
    my_list = ['red', 'yellow', 'blue']
    result = string_distance(my_list, 'green')
    print(result)
