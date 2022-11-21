from transformers import pipeline

def get_keyword(df):
  summarizer = pipeline("summarization")
  df['comment_key'] = [x['summary_text'] for x in summarizer(df['comment'].tolist(), min_length=0 ,max_length=150)]
  df['commentoncommentkey'] = [x['summary_text'] for x in summarizer(df['commentoncomment'].tolist(), min_length=0 ,max_length=150)]
  return df