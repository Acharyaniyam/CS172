#Programmer and userID = Niyam Acharya & nka42
#Program date = Dec 7, 2023
#Description =   This script compares the efficiency of searching operations between lists and Binary Search Trees (BSTs).
#                It implements functions to create a shuffled list, perform searches in lists, convert lists to BSTs, and compare search lengths.
#                The 'populateList' function generates a shuffled list of elements.
#                'searchLength' function finds the position of an element in a list or returns the length of the list if not found.
#                'listToBST' converts a list into a Binary Search Tree (BST).
#                The main logic runs iterations for varying numbers of elements, comparing search lengths between lists and BSTs.
#                It computes the average number of comparisons required to find elements in both data structures and outputs the results.

import random
from BST import BST

def populateList(n, s):
    lst = list(range(n))
    random.shuffle(lst)
    return lst[:s]

def searchLength(lst, n):
    if n in lst:
        return lst.index(n) + 1
    return len(lst)

def listToBST(lst):
    bst = BST()
    for item in lst:
        bst.append(item)
    return bst

if __name__ == "__main__":
    average_search_length_list = []
    average_search_length_bst = []

    for n in range(1, 1000, 100):
        sum_count_list = 0
        sum_count_bst = 0
        num_runs = 0

        for s in range(5):  # Run 5 iterations for more reliable average
            lst = populateList(n, n)
            bst = listToBST(lst)

            for v in range(n):
                sum_count_list += searchLength(lst, v)
                sum_count_bst += bst.searchLength(v)
                num_runs += 1

        avg_list = sum_count_list / num_runs
        avg_bst = sum_count_bst / num_runs

        average_search_length_list.append(avg_list)
        average_search_length_bst.append(avg_bst)

    print("Average Search Length for List:", average_search_length_list)
    print("Average Search Length for BST:", average_search_length_bst)
