import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline, _
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        elf.trailer_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_yotube_url)
	
