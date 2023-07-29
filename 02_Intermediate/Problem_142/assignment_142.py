'''
Write Python Program Convert array elements from float to integer
'''

def convert_float_to_integer_m1(input_array):
    # Using a list comprehension to convert elements from float to integer
    integer_array = [int(element) for element in input_array]
    return integer_array

def convert_float_to_integer_m2(input_array):
    # Using the map() function to convert elements from float to integer
    integer_array = list(map(int, input_array))
    return integer_array



if __name__=="__main__":
    float_array = [3.14, 2.718, 1.414, 0.5, 10.0]
    integer_array_m1 = convert_float_to_integer_m1(float_array)
    print(integer_array_m1)

    integer_array_m2 = convert_float_to_integer_m1(float_array)
    print(integer_array_m2)
