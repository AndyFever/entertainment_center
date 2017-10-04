import media
import fresh_tomatoes

alien = media.Movie("Alien",
                    "In space no one can hear you scream",
                    'http://images.fromupnorth.com/216/54a2e3cb62f02.jpg',
                    'https://www.youtube.com/watch?v=bEVY_lonKf4',
                    "Sigourney Weaver",
                    "1979")

rear_window = media.Movie("Rear Window",
                          "In deadly danger...because they saw too much!",
                          "http://img.moviepostershop.com/rear-window-movie-poster-1954-1020143868.jpg",
                          "https://www.youtube.com/watch?v=Ob_Sq__g01E",
                          "James Stewart",
                          "1954")

school_of_rock = media.Movie("School of Rock",
                             "He just landed the gig of his life: 4th grade.",
                             "https://fanart.tv/fanart/movies/1584/movieposter/school-of-rock-53f7a862c918b.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
                             "Jack Black",
                             "2004")

inception = media.Movie("Inception",
                        "Your mind is the scene of the crime",
                        "http://www.impawards.com/2010/posters/inception.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM",
                        "Leonardo DiCaprio",
                        "2010")

wonder_woman = media.Movie("Wonder Woman",
                        "Power. Grace. Wisdom. Wonder.",
                        "http://www.joblo.com/posters/images/full/dianabrace.jpg",
                        "https://www.youtube.com/watch?v=VSB4wGIdDwo",
                        "Gal Gaddot",
                        "2017")

star_wars = media.Movie("Star Wars",
                        "A long time ago in a galaxy far, far away...",
                        "https://images-na.ssl-images-amazon.com/images/I/81P3lDJbjCL._SL1347_.jpg",
                        "https://www.youtube.com/watch?v=ce6BFgwazMg",
                        "Mark Hamill",
                        "1979")


movies = [alien, rear_window, school_of_rock, inception, wonder_woman, star_wars]

fresh_tomatoes.open_movies_page(movies)

# test = fresh_tomatoes.create_movie_tiles_content(movies)
# print(test)
