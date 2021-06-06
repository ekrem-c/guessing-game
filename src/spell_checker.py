from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_response(word):
  return BeautifulSoup(\
    urlopen((f"http://agilec.cs.uh.edu/spell?check={word}"))
    .read().decode("utf-8"), "html.parser").get_text()

def parse_text(word):
  if word not in ['true', 'false']:
    raise RuntimeError("Got an unexpected output from the server!")

  return word == "true"

def is_spelling_correct(word):
  return parse_text(get_response(word))
