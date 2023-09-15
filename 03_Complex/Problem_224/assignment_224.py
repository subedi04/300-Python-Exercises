def english_to_arabic():
    # Sample dictionary with English words and their Arabic translations.
    dictionary = {
        "hello": "مرحبا",
        "book": "كتاب",
        "computer": "كمبيوتر",
        "friend": "صديق",
        "school": "مدرسة"
    }

    # Prompt user for input
    word = input("Enter an English word: ").lower()

    # Check if word exists in dictionary
    if word in dictionary:
        print(f"The Arabic translation for '{word}' is: {dictionary[word]}")
    else:
        print(f"Sorry, I don't have a translation for '{word}'.")

if __name__=="__main__":
    english_to_arabic()
