'''
Write A Python Program To Sort Student Name 
In Ascending Order In List And Student Should 
Display Which Contain Only 5 Character
'''
def sort_and_filter_names(names):
    filtered_names = [name for name in names if len(name) == 5]
    sorted_names = sorted(filtered_names)
    return sorted_names

# Example usage
student_names = ["Christopher", "Beatriz", "Alexander", "Kate", "Mikel", "Sara", "Adamo"]
sorted_filtered_names = sort_and_filter_names(student_names)

print("Sorted names with 5 characters:")
for name in sorted_filtered_names:
    print(name)
