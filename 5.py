from TikTokApi import TikTokApi

api = TikTokApi()
n_videos = 100
username = 'washingtonpost'
user_videos = api.byUsername(username, count =n_videos)
