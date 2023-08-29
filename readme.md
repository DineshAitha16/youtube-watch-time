# Description

To apply for YouTube monetization you have to reach 4000 hours of watch time. That's a pretty big milestone for a beginner. So let's help with this.

**Disclaimer**: This is for educational purposes only. It is NOT for cheating views.

# Requirements

- Python 3.7.x - 3.11.x
- Ready playlists on YouTube

# Installation
Pipenv environment:
```
pipenv install
```

Virtual Environments: 
```
pip install -r requirements.txt
```

## Run Flask
```
python3 app.py
```
- This will run a development server on http://127.0.0.1:5000

# How it works

- Enter YouTube playlist URL
- Enter number of videos to open from playlist
- You will get a button that will open all links at once in separate tabs
- Depending on the browser, you may need to go through and hit the play button on each video
- After that leave the tabs in the background and let them watch your videos

# Specifics

- YouTube allows one account to watch a video a certain number of times (from 5 to 10 in a day) which goes into statistics
- So opening the playlist in several tabs allows you to quickly watch it all multiple times
- After that you can change account and try again. Or you can watch in parallel from multiple accounts

# Roadmap

- Insert several playlists
- More accurate and organized playlist details 
- Log playlist/video stats to correlate it with the internal YouTube stats
