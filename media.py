import webbrowser

""" The Movie class will build an instance of a movie with the relevant
    details. It includes the Movie title, the movie tagline,
    the trailer, the lead actor and the release date.
"""


class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image_url,
                 trailer_youtube, lead_actor, movie_year):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube
        self.lead_actor = lead_actor
        self.movie_year = movie_year

    def show_trailer(self):
        # Open the trailer and play in the default browser.
        webbrowser.open(self.trailer_youtube_url)
