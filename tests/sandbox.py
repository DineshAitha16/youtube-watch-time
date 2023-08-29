import re
import requests
from bs4 import BeautifulSoup
import json


def get_links(playlist_link):
    """ Test basic logic. """

    all_videos = []
    headers = {"Accept-Language": "en"}
    response = requests.get(playlist_link, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    script_tag = soup.find('script', string=re.compile(r'var ytInitialData = {'))

    # Extract the JSON data from the script tag
    json_data = re.search(r'var ytInitialData = ({.*?});', script_tag.text, re.DOTALL)

    # Parse the JSON data
    data = json.loads(json_data.group(1))

    video_entries = data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][0]["tabRenderer"][
        "content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]
    for video_entry in video_entries:
        playlist_video_renderer = video_entry["playlistVideoListRenderer"]["contents"]

        for renderer in playlist_video_renderer:
            video_id = renderer['playlistVideoRenderer']['videoId']
            title = renderer['playlistVideoRenderer']['title']['runs'][0].get("text")
            title_label = renderer['playlistVideoRenderer']['title']['accessibility']['accessibilityData'].get("label")
            video_index = renderer['playlistVideoRenderer']['index'].get("simpleText")
            views = renderer['playlistVideoRenderer']['videoInfo']['runs'][0].get("text")
            thumbnail_url = renderer['playlistVideoRenderer']['thumbnail']['thumbnails'][0].get("url")
            video_url = renderer[
                'playlistVideoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata'].get("url")
            length_seconds = renderer['playlistVideoRenderer']['lengthSeconds']

            video = {
                    "Video ID": video_id,
                    "Title": title,
                    "Title label": title_label,
                    "Video Index": video_index,
                    "Views": views,
                    "Thumbnail URL": thumbnail_url,
                    "Video URL": video_url,
                    "Length (Seconds)": length_seconds,
                }

            all_videos.append(video)
    return all_videos


link = 'PLAYLIST_URL'
playlist_videos = get_links(link)

print(playlist_videos)


