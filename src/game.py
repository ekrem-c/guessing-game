from guess import *
from spell_checker import *
import sys

def read_file(filename):
  with open(filename) as file:
    return file.read().split()

try:
  selected_word = select_word(read_file("words_list.txt"))
  scrambled_word = scramble_word(selected_word)

  guessed = input("The scrambled word is: " + scrambled_word + \
                  ".\nPlease make your guess and ensure it has correct spelling.\n")

  while guessed != selected_word:
    score = score_calculator(selected_word, guessed, is_spelling_correct)

    if score > 0:
      print("You have a close guess but not quite there yet! Your score is", \
            score, ".\nPlease try again!")
    else:
      print("You either have a wrong spelling or a way off guess, please try again!")

    guessed = input("The scrambled word is: " + scrambled_word + \
                    ".\nPlease make your guess and ensure it has correct spelling.\n")

  print("Congratulations! You won!")
except:
  print("Oops!", sys.exc_info()[0], "error!")