from googleapiclient.discovery import build
import pandas as pd

api_key = 'XXXXXXXX'

def video_comments(video_id):
    all_data = []

    # youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey=api_key)

    # retrieve video results
    video_response=youtube.commentThreads().list(
    part='snippet,replies',
    videoId=video_id).execute()
    for i in range(len(video_response['items'])):
            data = dict(comments = video_response['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay'])
            all_data.append(data['comments'])
    
    # if there is nextPageToken, keep calling the API
    while video_response.get('nextPageToken', None):
        request = youtube.commentThreads().list(
            part='id,replies,snippet',
            videoId=video_id,
            pageToken=video_response['nextPageToken']
        )
        video_response = request.execute()
        
        for i in range(len(video_response['items'])):
            data = dict(comments = video_response['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay'])
            all_data.append(data['comments'])
    
    return all_data

# data_res = video_comments('jrwSo9ZDZEg')
# print(len(data_res))

# df = pd.DataFrame(data_res, columns = ['comments'])
# df.to_csv('comments.csv')