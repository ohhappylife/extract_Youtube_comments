from transformers import pipeline

def get_sentiment(df):
    sentimentAnalysis_pipeline = pipeline("sentiment-analysis")
    df['comment_sentiment'] = df['comment'].apply(sentimentAnalysis_pipeline)
    counter = 0
    scores = []
    min_score = 0
    max_score = 0
    mean_score = 0
    for index, row in df.iterrows():
        if len(row['commentoncomment']) > 0:
            l = row['commentoncomment'].split("||||")
            for i in range (0, (len(l)-1)):
                scores.append((sentimentAnalysis_pipeline(l[i])[0]['score']))
            mean_score = round(sum(scores) / len(scores),4)
            min_score = round(min(scores),4)
            max_score = round(max(scores),4)
        else:
            pass
        scores = []
        print(df)
        df.iloc[counter, df.columns.get_loc('commentoncomment_mean_score')] = mean_score
        df.iloc[counter, df.columns.get_loc('commentoncomment_min_score')] = min_score
        df.iloc[counter, df.columns.get_loc('commentoncomment_max_score')] = max_score
        counter = counter + 1
        min_score = 0
        max_score = 0
        mean_score = 0
    return df