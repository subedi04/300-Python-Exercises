def sort_colors(color_codes, ascending=True):
    """
    Sorts a list of color codes in ascending or descending order.
    
    Parameters:
        color_codes (list): List of color codes to be sorted.
        ascending (bool): True to sort in ascending order, False to sort in descending order.
    
    Returns:
        list: Sorted list of color codes.
    """
    sorted_colors = sorted(color_codes, reverse=not ascending)
    return sorted_colors


if __name__=="__main__":
    # Sample color codes
    color_codes = ["Orange", "Green", "Blue", "Yellow", "Black"]

    # Sort in ascending order
    ascending_order = sort_colors(color_codes, ascending=True)
    print("Ascending Order:", ascending_order)

    # Sort in descending order
    descending_order = sort_colors(color_codes, ascending=False)
    print("Descending Order:", descending_order)
