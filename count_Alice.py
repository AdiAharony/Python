# The program will find the word that appears the most in 'Alice In Wonderland' book.

def main_count_Alice():
    # Step 1: Read the text from the file
    alice_text = read_Alice_text()
    
    # Step 2: Clean the text and return a list of words
    alice_words = clean_alice(alice_text)
    
    # Step 3: Count the words and find the most frequent one    
    max_word_count = count_words_in_Alice(alice_words)
    
    # Step 4: Print the most frequent word
    print(f"The word that appears the most in 'Alice In Wonderland' book is: {max_word_count}")
    
def read_Alice_text():
    # Open the Alice.txt file and read the content
    f1 = open('Alice.txt')
    read_alice = f1.read()
    
    # Return the content of the file
    return read_alice

def clean_alice(alice_text):
    # Initialize an empty string to store cleaned text
    clear_text = ''
    
    # Loop through each character in the text
    for letter in alice_text:
         # If the character is a valid alphanumeric or space, keep it
         if letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ':
            clear_text += letter
         else:
             # Replace invalid characters with a space
             clear_text += ' '
    
    # Split the cleaned text into a list of words and return it
    alice_words = clear_text.split()
    return alice_words

def count_words_in_Alice(alice_words):
    # Initialize variables to keep track of the maximum word count and the most frequent word
    counter = 0
    num = alice_words[0]
    
    # Loop through each word in the list
    for word in alice_words:
        # Count how many times the word appears in the list
        max_word_count = alice_words.count(word)
        
        # If the current word's count is greater than the previous maximum, update it
        if(max_word_count > counter):
            counter = max_word_count
            num = word
    
    # Return the most frequent word
    return num

# Run the main function to execute the program
main_count_Alice()
