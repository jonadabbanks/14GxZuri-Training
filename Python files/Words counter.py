#python script that  counts and returns the number of words in a given text.
#creating user input
user_words = input("Enter a Text: ")
#using the split method to split the recieved input
statement = user_words.split()
#using the len method to count number of words
words_count = len(statement)
print("Total Words: " + str(words_count))