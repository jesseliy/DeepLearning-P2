import webbrowser


class Movie():
    """Class describe the main info of movie

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Either form is acceptable, but the two should not be mixed. Choose one
    convention to document the __init__ method and be consistent with it.

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        movie_title (str): movie's title.
        movie_storyline (str): movie's storyline.
        poster_image (str): poster image's url.
        trailer_youtube (str): trailer's url

    Attributes:
        movie_title (str): movie's title.
        movie_storyline (str): movie's storyline.
        poster_image (str): poster image's url.
        trailer_youtube (str): trailer's url

    Methods:
        show_trailer(): Open trailer in webbrower
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        elf.trailer_url = trailer_youtube

    # Open trailer in webbrower
    def show_trailer(self):
        webbrowser.open(self.trailer_yotube_url)
