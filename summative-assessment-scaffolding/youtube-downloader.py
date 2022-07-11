from pytube import YouTube
import os
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def root():
    return '''
    <form action="/download" method="post">
        <input type="text" name="yt-link" />
        <input type="submit" />
    </form>
    '''

@app.route('/download', methods=['POST'])
def download():
    yt_link = request.form['yt-link']
    video = YouTube(yt_link)
    video_folder = os.getcwd()
    file_name = f'{os.urandom(24).hex()}.mp4'
    video.streams.filter(file_extension='mp4').first().download(video_folder, file_name)
    file_path = os.path.join(video_folder, file_name)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')