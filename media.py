import webbrowser
class Movie():
    #create instances
    def __init__(self, title, storyline, cover_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.cover_url = cover_url
        self.trailer_youtube_url = trailer_youtube_url
    # open the thriller url
    def open_thriller(self):
        webbrowser.open(self.trailer_youtube_url)
