import os
import sys

from googleapiclient.discovery import build
def video_comments(api_key, video_id):
  nesteddict = {}

  youtube = build('youtube', 'v3',
                  developerKey=api_key)

  video_response = youtube.commentThreads().list(
    part='snippet,replies',
    videoId=video_id
  ).execute()
  replies = []

  count = video_response['pageInfo']['totalResults']
  i = 0

  for c, item in enumerate(video_response['items']):
    thisdict = {
      "author": "",
      "comment": "",
      "time": "",
      "replycount": "",
      "likecount": "",
      "commentoncomment": []
    }
    thisdict['comment'] = (item['snippet']['topLevelComment']['snippet']['textOriginal'])
    thisdict['replycount'] = (item['snippet']['totalReplyCount'])
    thisdict['author'] = (item['snippet']['topLevelComment']['snippet']['authorDisplayName'])
    thisdict['time'] = (item['snippet']['topLevelComment']['snippet']['publishedAt'])
    thisdict['likecount'] = (item['snippet']['topLevelComment']['snippet']['likeCount'])

    replycount = item['snippet']['totalReplyCount']

    if replycount > 0:
      for reply in item['replies']['comments']:
        replies.append((reply['snippet']['textDisplay'])  + "||||")
    thisdict['commentoncomment'] = replies

    nesteddict[c] = thisdict
    i = i + 1
    replies = []

  if i == count:
    return nesteddict

