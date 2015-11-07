import media
import fresh_tomatoes

"""Main entry of the program. Builds the list of my favorite movies """
the_matrix = media.Movie("The Matrix", "The Matrix is a science fiction action media franchise created by The Wachowskis and distributed by Warner Bros. Pictures.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                        "https://www.youtube.com/watch?v=m8e-FF8MsqU")

toy_story = media.Movie("Toy Story", "A story of a boy and his toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
  

castle_in_the_sky = media.Movie("Castle in the Sky", "A young boy and a girl with a magic crystal must race against pirates and foreign agents in a search for a legendary floating castle.",
                        "https://upload.wikimedia.org/wikipedia/en/4/40/Castle_in_the_Sky_%28Movie_Poster%29.jpg",
                        "https://www.youtube.com/watch?v=McM0_YHDm5A")


forrest_gump = media.Movie("Forrest Gump", "forrest_gump",
                        "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                        "https://www.youtube.com/watch?v=uPIEn0M8su0")


mulan = media.Movie("Mulan", "To save her father from death in the army, a young maiden secretly goes in his place and becomes one of China's greatest heroines in the process.",
                        "https://upload.wikimedia.org/wikipedia/en/a/a3/Movie_poster_mulan.JPG",
                        "https://www.youtube.com/watch?v=wAbGAkkOgcM")


movies = [the_matrix, toy_story, castle_in_the_sky, forrest_gump, mulan]
fresh_tomatoes.open_movies_page(movies)
