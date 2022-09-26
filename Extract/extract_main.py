from Extract import extract_comment

def extractIt(api_key, video_id):
  thisdict = extract_comment.video_comments(api_key, video_id)
  return thisdict