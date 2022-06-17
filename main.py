
#TURING MACHINE SIMULATOR BY SRIKAR AND JAYANT
import sys

from pal import check_palindrome

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("python test.py word")
        print("where word is the word to be tested as a palindrome")

    word = str(input('enter a word'))
    check_palindrome(word)