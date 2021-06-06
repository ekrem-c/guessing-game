import unittest
import mock
from src.spell_checker import *

class RemoteServiceTests(unittest.TestCase):
  def test_get_response_works(self):
    self.assertIsNotNone(get_response("monkey"))

  def test_spell_check_for_true(self):
    self.assertTrue(parse_text("true"))

  def test_spell_check_for_false(self):
    self.assertFalse(parse_text("false"))

  def test_spell_check_for_sth_else(self):
    self.assertRaisesRegex(RuntimeError, "Got an unexpected output from the server!",
                           parse_text, "something else")

  @mock.patch("src.spell_checker.get_response", return_value="true")
  def test_spellcheck_true(self, myMock):
    self.assertTrue(is_spelling_correct("right"))

  @mock.patch("src.spell_checker.get_response", return_value="false")
  def test_spellcheck_false(self, myMock):
    self.assertFalse(is_spelling_correct("rigth"))

  @mock.patch("src.spell_checker.get_response", return_value="false")
  def test_spellcheck_haha(self, myMock):
    self.assertFalse(is_spelling_correct("haha"))

  @mock.patch("src.spell_checker.get_response", side_effect=RuntimeError)
  def test_spellcheck_handle_exception(self, myMock):
    self.assertRaises(RuntimeError, is_spelling_correct, "monkey")

  def test_first_integration_test_returns_true(self):
    self.assertTrue(is_spelling_correct("correct"))

if __name__ == '__main__':
    unittest.main()
