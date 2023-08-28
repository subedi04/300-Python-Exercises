'''
Write A Python Program To Find Union , 
Intersection And Difference Of Two Set. 
Find Sum Of All Items Of Union, 
Intersection And Difference.
'''

def main():
    set1 = set(input("Enter elements of the first set (comma-separated): ").split(","))
    set2 = set(input("Enter elements of the second set (comma-separated): ").split(","))

    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set = set1.difference(set2)

    union_sum = sum(map(int, union_set))
    intersection_sum = sum(map(int, intersection_set))
    difference_sum = sum(map(int, difference_set))

    print("Union:", union_set)
    print("Intersection:", intersection_set)
    print("Difference:", difference_set)

    print("Sum of elements in union:", union_sum)
    print("Sum of elements in intersection:", intersection_sum)
    print("Sum of elements in difference:", difference_sum)

if __name__ == "__main__":
    main()
