__author__ = "Shon"
__version__ = "1.0.1"
__email__ = "sshon2@alumni.jh.edu"
__status__ = "Development"

import nltk
from nltk.corpus import stopwords

def remove_stopwords(df, colName):
  """
  Remove stop words from collected news article.
  :param dataframe df: dataframe to be cleaned.
  :return: dataframe with cleaned text.
  :rtype: dataframe
  """
  stop = set(stopwords.words('english'))
  newName = str(colName) + '_wout_stopwords'
  df[newName] = df.apply(lambda row: nltk.word_tokenize(row[colName]), axis=1)

  df[newName] = df[newName].apply(
    lambda words: [word for word in words if word not in stop])

  df[newName] = [' '.join(map(str, l)) for l in df[newName]]

  return df
