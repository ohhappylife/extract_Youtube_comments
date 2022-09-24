import crawll_ids
import temp
from Extract.extract_comment import video_comments
from Load.save_to_cwd import save_file
from Transform.remove_Emoji import remove_emoji
from Transform.transform_to_df import basic_cleaning
from Other import load_csv_file

api_key = temp.getGoogleKey()
link = load_csv_file('l.txt')
ids = crawll_ids.getID(link)

for count, id in enumerate(ids):
    nested_dict = video_comments(id, api_key)
    df = basic_cleaning(nested_dict)
    df = remove_emoji(df)
    file_name = str(count + 1) + '.txt'
    df.to_csv(file_name)
    save_file(df, str(id), str(id) + '_' + str(count))


