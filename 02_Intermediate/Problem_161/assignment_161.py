'''
Write a Python Numpy Program to Find the number 
of occurrences of a sequence in a array
'''

import numpy as np

def count_sequence_occurrences(arr, sequence):
    arr_len = len(arr)
    seq_len = len(sequence)

    if arr_len < seq_len:
        return 0

    # Convert the sequence and the array to NumPy arrays
    arr_np = np.array(arr)
    seq_np = np.array(sequence)

    # Create a sliding window view of the array with the same length as the sequence
    window_view = np.lib.stride_tricks.sliding_window_view(arr_np, window_shape=seq_len)

    # Compare each window with the sequence and get a boolean array
    # indicating where the sequences match
    match_indices = np.all(window_view == seq_np, axis=1)

    # Count the number of True occurrences in the boolean array
    occurrences = np.count_nonzero(match_indices)

    return occurrences

if __name__ == "__main__":
    array = [1, 2, 3, 2, 1, 4, 5, 1, 2, 3, 2, 1]
    sequence = [1, 2, 3]

    occurrences = count_sequence_occurrences(array, sequence)
    print(f"The sequence {sequence} occurs {occurrences} times in the array.")
