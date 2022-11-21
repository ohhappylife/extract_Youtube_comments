import crawll_ids
from Load.save_to_cwd import save_file
from Transform.remove_Emoji import remove_emoji
from Transform.transform_to_df import basic_cleaning
from Other import load_csv_file
from Extract import extract_main
from Analyze import create_Ngram, extract_keywords, summarize_texts, get_setiment

api_key = str("AIzaSyBa7u0sBZnBbO9_0xo__M_b_Vl7kB7sM10")
link = load_csv_file.load_file('url.txt')
ids = crawll_ids.getID(link)

for count, id in enumerate(ids):
    nested_dict = extract_main.extractIt(str(api_key), id)
    df = basic_cleaning(nested_dict)
    df = remove_emoji(df)

    df = extract_keywords.summarize(df, 'comment')
    df = extract_keywords.summarize(df, 'commentoncomment')
    df['mean_score'] = 0
    df['max_score'] = 0
    df['min_score'] = 0
    df = get_setiment.get_sentiment(df)

    file_name = str(count + 1) + '.txt'
    df.to_csv(file_name)
    save_file(df, str(id), str(id) + '_' + str(count))