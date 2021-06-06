import unittest
from src.guess import scramble_word
from src.guess import score_calculator as original_score_calculator
from src.guess import has_invalid_characters
from src.guess import select_word
from functools import partial

score_calculator = partial(original_score_calculator, is_spelling_correct = lambda word: True)

class GuessTests(unittest.TestCase):
  def test_Canary(self):
    self.assertTrue(True)

  def test_scramble_apple(self):
    self.assertNotEqual("apple", scramble_word("apple"))

  def test_scramble_matter(self):
    self.assertNotEqual("matter", scramble_word("matter"))

  def test_scramble_apple_and_get_different_results(self):
    first = scramble_word("apple")
    second = scramble_word("apple")

    self.assertNotEqual(first, second)

  def test_scramble_empty_string(self):
    self.assertEqual("", scramble_word(""))

  def test_mixed_cases_return_lowercase(self):
    great_outcome = scramble_word("gReAt")

    self.assertTrue(great_outcome.islower())

  def test_scramble_has_same_characters(self):
    self.assertEqual(sorted("great"), sorted(scramble_word("great")))

  def test_score_for_one_letter(self):
    self.assertEqual(1, score_calculator("apple", "a"))

  def test_score_partial_guess(self):
    self.assertEqual(7, score_calculator("monkey", "monk"))

  def test_score_not_continuous(self):
    self.assertEqual(4, score_calculator("apple", "ape"))

  def test_score_no_vowel(self):
    self.assertEqual(5, score_calculator("banana", "ban"))

  def test_score_where_there_are_letters_not_in_word(self):
    self.assertEqual(0, score_calculator("banana", "bye"))

  def test_score_for_guess_with_repeat_letters(self):
    self.assertEqual(0, score_calculator("relate", "rear"))

  def test_score_with_equal_letters(self):
    self.assertEqual(9, score_calculator("relate", "relate"))

  def test_score_incorrect_spelling(self):
    self.assertEqual(0, original_score_calculator("monkey", "ney", lambda word: False))

  def test_score_incorrect_spelling2(self):
    self.assertEqual(0, original_score_calculator("apple", "app", lambda word: False))

  def test_score_incorrect_spelling3(self):
    self.assertEqual(0, original_score_calculator("apple", "ael", lambda word: False))

  def test_for_network_error(self):
    self.assertRaisesRegex(RuntimeError, "Network Error", original_score_calculator, "monkey", "monk", \
                      lambda faulty_spell_checker: exec("raise RuntimeError('Network Error')"))

  def test_pick_a_random_word(self):
    test_list = ["monkey", "fruit", "banana", "apple", "cosmopolitan", "relate", \
                 "snow", "rain", "sun", "beach", "spring", "break", "semester"]

    self.assertTrue(select_word(test_list) in test_list)

  def test_second_pick_returns_different(self):
    test_list = ["monkey", "fruit", "banana", "apple", "cosmopolitan", "relate", \
                 "snow", "rain", "sun", "beach", "spring", "break", "semester"]
    first_pick = select_word(test_list)
    second_pick = select_word(test_list)
    while second_pick == first_pick:
      second_pick = select_word(test_list)

    self.assertNotEqual(first_pick, second_pick)

  def test_pick_from_empty_list(self):
    test_list = []

    self.assertRaises(IndexError, select_word, test_list)
