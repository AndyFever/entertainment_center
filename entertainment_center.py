import media
import fresh_tomatoes

alien = media.Movie("Alien",
                    "A pissed off Alien against the crew of the Nostramo",
                    'http://images.fromupnorth.com/216/54a2e3cb62f02.jpg',
                    'https://www.youtube.com/watch?v=bEVY_lonKf4')

rear_window = media.Movie("Rear Window",
                          "Peeping Tom solves a murder",
                          "http://img.moviepostershop.com/rear-window-movie-poster-1954-1020143868.jpg",
                          "https://www.youtube.com/watch?v=Ob_Sq__g01E")

school_of_rock = media.Movie("School of Rock",
                             "A sub corrupts kids into Rock n Roll",
                             "https://fanart.tv/fanart/movies/1584/movieposter/school-of-rock-53f7a862c918b.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

inception = media.Movie("Inception",
                        "A dream within a dream within a dream (repeat as required)",
                        "http://www.impawards.com/2010/posters/inception.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

wonder_woman = media.Movie("Wonder Woman",
                        "Who new Ares was responsible for WW1?",
                        "http://www.joblo.com/posters/images/full/dianabrace.jpg",
                        "https://www.youtube.com/watch?v=VSB4wGIdDwo")

star_wars = media.Movie("Star Wars",
                        "A kid with daddy issues battles the empire",
                        "https://images-na.ssl-images-amazon.com/images/I/81P3lDJbjCL._SL1347_.jpg",
                        "https://www.youtube.com/watch?v=ce6BFgwazMg")


movies = [alien, rear_window, school_of_rock, inception, wonder_woman, star_wars]
fresh_tomatoes.open_movies_page(movies)
