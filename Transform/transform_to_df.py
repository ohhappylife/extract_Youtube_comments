import pandas as pd
def basic_cleaning(nestedDict):
  df = pd.DataFrame(nestedDict)
  df = df.T
  df.commentoncomment = df.commentoncomment.apply(', '.join)
  return df