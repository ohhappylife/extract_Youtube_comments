"""
  create_Ngram.py
  Generating N-gram from sentences
"""
__author__ = "Shon"
__version__ = "1.0.1"
__email__ = "sshon2@alumni.jh.edu"
__status__ = "Production"

import pandas as pd
import re
import unicodedata
import nltk
from Load import save_to_s3

def basic_clean(text):
  """
  Clean text data for generating N-gram
  :param str text: original text
  :return: cleaned text for N-gram
  :rtype: list
  """
  wnl = nltk.stem.WordNetLemmatizer()
  text = (unicodedata.normalize('NFKD', text)
    .encode('ascii', 'ignore')
    .decode('utf-8', 'ignore')
    .lower())
  words = re.sub(r'[^\w\s]', '', text).split()
  return [wnl.lemmatize(word) for word in words]

def Ngram(df, name, col_name):
  """
  Create N-gram based on input and store result into given S3 path.
  :param dataframe df: dataframe to be cleaned.
  :return: none
  :rtype: none
  """
  title = basic_clean(''.join(str(df[col_name].tolist())))

  for i in range(1,4): # file name = {source_name}_title_n.csv
    ftitle = name + "_title_" + '_' + str(i) + '.csv'

    ngram_title = (pd.Series(nltk.ngrams(title, i)).value_counts()).reset_index()

    save_to_s3.savetoBucket(ngram_title, 'ngram', ftitle)


