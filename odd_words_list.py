# Create a program that stores a list of words. 
# THEN, use list comprehension to create a new list that contains ONLY the words that have an odd number of characters.

def main():
    # List of words
    word_list = [
        "apple", "banana", "orange", "grape", "kiwi", "strawberry", "melon"
    ]
    
    #  print original words
    print("\n Original Word List: ", word_list, '\n')

    # List comprehension to filter words with odd number of characters
    odd_length_words = [word for word in word_list if len(word) % 2 != 0]

    # Print the list of words with odd number of characters
    print("Words with odd number of characters:", odd_length_words)

if __name__ == "__main__":
    main()

