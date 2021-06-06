import random

def scramble_word(to_scramble):
  scrambled_word = "".join(random.sample(to_scramble, len(to_scramble))).lower()

  return scramble_word(to_scramble) \
    if scrambled_word == to_scramble.lower() and len(set(scrambled_word)) > 1 else scrambled_word

def has_invalid_characters(word, guess):
  return any(filter(lambda letter: guess.count(letter) > word.count(letter), guess))

def score_calculator(word, guess, is_spelling_correct):
  if has_invalid_characters(word, guess):
    return 0

  if not is_spelling_correct(guess):
      return 0

  return sum(map(lambda letter: 1 if letter in 'aeiou' else 2, guess))

def select_word(words):
  return random.choice(words)
