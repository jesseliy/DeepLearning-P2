import media
import fresh_tomatoes

# function definition:
# media.Movie(title,storyline,poster_image,trailer_youtube)

The_Shawshank_Redemption= media.Movie("The Shawshank Redemption",
                                      "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                                      "https://www.goldenglobes.com/sites/default/files/films/the-shawshank-redemption.jpg",
                                      "https://www.youtube.com/watch?v=6hB3S9bIaco")

 
The_GodFather=media.Movie("The Godfather",
                          "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BY2Q2NzQ3ZDUtNWU5OC00Yjc0LThlYmEtNWM3NTFmM2JiY2VhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY1200_CR105,0,630,1200_AL_.jpg",
                          "https://www.youtube.com/watch?v=sY1S34973zA")

Coco = media.Movie("Coco",
                   "A story of a boy enters the land of the dead to fine his great-great-grandfather, legendary singer.",
                   "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",
                   "https://www.youtube.com/watch?v=zNCz4mQzfEI")
					
# you can add you favorite movies here 

movies= [The_Shawshank_Redemption,The_GodFather,Coco]
fresh_tomatoes.open_movies_page(movies)
