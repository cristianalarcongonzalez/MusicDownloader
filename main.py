from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        url = request.form['url']
        quality = request.form['quality']
        
        current_folder = os.getcwd()
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=current_folder)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

