import config
from Load.save_to_cwd import save_file
from Transform.remove_Emoji import remove_emoji
from Transform.transform_to_df import basic_cleaning
from Extract import extract_main, crawll_ids
from Analyze import extract_keywords, get_setiment
from config import apikey, url

api_key = apikey
ids = crawll_ids.getID(url)

for count, id in enumerate(ids):
    nested_dict = extract_main.extractIt(str(api_key), id)
    df = basic_cleaning(nested_dict)
    df = remove_emoji(df)

    df = extract_keywords.summarize(df, 'comment')
    df = extract_keywords.summarize(df, 'commentoncomment')
    df['commentoncomment_mean_score'] = 0
    df['commentoncomment_max_score'] = 0
    df['commentoncomment_min_score'] = 0
    df = get_setiment.get_sentiment(df)

    file_name = str(count + 1) + '.txt'
    df.to_csv(file_name)
    save_file(df, str(id), str(id) + '_' + str(count))