import media
import fresh_tomatoes  # A library for creating the web-page

# function definition:
# media.Movie(title,storyline,poster_image,trailer_youtube)

The_Shawshank_Redemption = media.Movie(
                            "The Shawshank Redemption",
                            "Two imprisoned men bond over a number of years, "
                            "finding solace and eventual redemption through "
                            "acts of common decency.",
                            "https://www.goldenglobes.com/sites/default/"
                            "files/films/the-shawshank-redemption.jpg",
                            "https://www.youtube.com/watch?v=6hB3S9bIaco")

The_GodFather = media.Movie(
                 "The Godfather",
                 "The aging patriarch of an organized crime dynasty transfers "
                 "control of his clandestine empire to his reluctant son.",
                 "http://img.zanda.com/item/57040290000061/1024x768/"
                 "The_Godfather.jpg",
                 "https://www.youtube.com/watch?v=sY1S34973zA")

Coco = media.Movie(
        "Coco",
        "A story of a boy enters the land of the dead to fine his great-gre"
        "at-grandfather, legendary singer.",
        "https://upload.wikimedia.org/wikipedia/en/9/98/"
        "Coco_%282017_film%29_poster.jpg",
        "https://www.youtube.com/watch?v=zNCz4mQzfEI")

""" you can add you favorite movies here
"""

# Creat the movie list for movie page
movies = [The_Shawshank_Redemption, The_GodFather, Coco]
# Creat the movie page
fresh_tomatoes.open_movies_page(movies)
