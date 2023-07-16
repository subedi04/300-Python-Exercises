'''
Write a Python program to find 
less occurring element in a given 
list of numbers.
'''

from collections import Counter

def Find_least_occurring_element(numbers):
    counts = Counter(numbers)
    min_count = min(counts.values())
    least_occurrences = [num for num, count in counts.items() if count == min_count]
    return least_occurrences

if __name__=="__main__":
    numbers = [1, 2, 3, 2, 4, 1, 3, 5, 4, 5, 1, 2]
    least_occurrences = Find_least_occurring_element(numbers)
    print("Least occurring elements:", least_occurrences)
