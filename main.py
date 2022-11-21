from Load import store_to_s3
from Load.save_to_cwd import save_file
from Transform.remove_Emoji import remove_emoji
from Transform.transform_to_df import basic_cleaning
from Extract import extract_main, crawll_ids
from Analyze import extract_keywords, get_setiment
from config import apikey, url, bucket_csv,bucket_excel\
    ,bool_store_merged_csv_s3,bool_store_merged_csv,bool_store_merged_excel, \
    bool_store_merged_excel_s3, bool_store_merged_excel_cwd, bool_store_merged_csv_cwd
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
    df['comment_sentiment'] = 'Not Available'
    df['comment_sentiment_Score'] = 0
    df = get_setiment.get_sentiment(df)

    if bool_store_merged_csv == True:
        fname_csv = "merged_" + str(id) + '.csv'
    if bool_store_merged_excel == True:
        fname_excel = "merged_" + str(id) + '.xlsx'
    if bool_store_merged_csv_s3 == True:
        store_to_s3.savetoBucket_csv(df, bucket_csv, fname_csv)
    if bool_store_merged_excel_s3 == True:
        store_to_s3.savetoBucket_excel(df, bucket_excel, fname_excel)
    if bool_store_merged_excel_cwd == True:
        df.to_excel(fname_excel)
        save_file(df, str(id), str(id) + '_' + str(count))
    if bool_store_merged_csv_cwd == True:
        df.to_csv(fname_csv)
        save_file(df, str(id), str(id) + '_' + str(count))
