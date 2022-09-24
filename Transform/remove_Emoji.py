import demoji

def remove_emoji(df):
  l = list(df.columns)
  for li in l:
    df[li]=df[li].apply(str)

  df = df.applymap(lambda x: demoji.replace(x,''))
  return df