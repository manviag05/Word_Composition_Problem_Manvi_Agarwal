# Word_Composition_Problem_Manvi_Agarwal
Overview:
This Python program identifies the longest and second-longest compound words from a given list of words. The core logic lies in the recursive comp function, which checks if a word is a compound word by recursively breaking it into prefixes and suffixes, and checking their existence in the word set.

Design Decisions:
The program utilizes a recursive approach to efficiently identify compound words by breaking them into smaller parts.
It reads input from a text file where each line contains a word.
The main function (__main__) calculates the execution time and prints the longest and second-longest compound words along with the processing time.

Function comp(W, orig_W, W_set):
This function determines whether a given word W is a compound word or not.
It takes three parameters:
W: The word to be checked.
orig_W: The original word being checked for compoundness.
W_set: A set containing all words for efficient lookup.
If W is in the set W_set and is not the original word (orig_W), it returns True, indicating that W is a compound word.
It then iterates over all possible prefixes P and suffixes S of W, recursively calling itself with these substrings.
The function returns True if any of the recursive calls indicate that S is a compound word.

Function longest_compword(Ws):
This function finds the longest compound word from a list of words Ws.
It initializes an empty string ans to store the current longest compound word.
It iterates through each word in the list and checks if it is a compound word using the comp function.
If the word is a compound word and its length is greater than the length of the current ans, it updates ans.

Function secon_longcomp(Ws, long_W):
This function finds the second-longest compound word from a list of words Ws, excluding the longest one (long_W).
It follows a similar approach to longest_compword, but it skips the longest word while searching for the second longest.

Main Block:
The script reads input from a file and stores the words in a list W_list.
It measures the execution time using the time module.
It calls the longest_compword and secon_longcomp functions to find the longest and second-longest compound words.
Finally, it prints the results along with the execution time.

Performance:
The script may take varying amounts of time to process based on the number of words and their lengths. The complexity of finding compounded words increases with the size and complexity of the input word list.
