import Other.load_csv_file
import crawll_ids
import temp
from Extract.extract_comment import video_comments
from Load.save_to_cwd import save_file
from Transform.remove_Emoji import remove_emoji
from Transform.transform_to_df import basic_cleaning
from Other import load_csv_file
from Extract import extract_main

api_key = str(temp.getGoogleKey())
print(api_key)
link = load_csv_file.load_file('l.csv')
ids = crawll_ids.getID(link)

for count, id in enumerate(ids):
    nested_dict = extract_main.extractIt(str(api_key), id)
    df = basic_cleaning(nested_dict)
    df = remove_emoji(df)
    file_name = str(count + 1) + '.txt'
    df.to_csv(file_name)
    save_file(df, str(id), str(id) + '_' + str(count))


