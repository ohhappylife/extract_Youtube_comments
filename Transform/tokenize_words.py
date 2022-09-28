"""
  tokenize_words.py
  get sentence and return tokenized sentences
"""
__author__ = "Shon"
__version__ = "1.0.1"
__email__ = "sshon2@alumni.jh.edu"
__status__ = "Production"

from nltk.tokenize import word_tokenize

def tokenize_words(df, colName):
  """
  Tokenize news articles for analysis.
  :param dataframe df: dataframe to be cleaned.
  :return: dataframe with tokenized article
  :rtype: dataframe
  """
  new_name = colName + "_tokenized"
  df[new_name] = df[colName].apply(word_tokenize)
  return df