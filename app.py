from flask import Flask, render_template, request, redirect, url_for

from services.scrapping_services import get_soup, extract_json, parse_json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video', methods=['GET'])
def redirect_link():
    """ Get the actual URL to redirect to from the query parameters. """

    actual_url = request.args.get('url')
    return redirect(actual_url)


@app.route('/process_playlist', methods=['POST'])
def process_playlist():
    """ Fetch data from a given playlist. Returns dictionary.
    Generate list of links_to_open sorted by longest duration and sliced by given num_videos. """

    if request.method == 'POST':
        playlist_url = request.form.get('playlist_url')
        num_videos = request.form.get('num_videos')

        html = get_soup(playlist_url)
        video_data = extract_json(html)
        playlist_info = parse_json(video_data)

        sorted_playlist_info = sorted(playlist_info, key=lambda x: x['Length'], reverse=True)[:int(num_videos)]
        links_to_open = [
            url_for('redirect_link', url=f"https://youtube.com{link['Video URL']}&autoplay=1&mute=1&shuffle=1")
            for link in sorted_playlist_info
        ]

        return render_template('result.html',
                               playlist_videos=playlist_info,
                               links_to_open=links_to_open)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
