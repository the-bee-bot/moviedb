class Movie(object):
    """
    Movie class to store favourite movie's details.
    """

    def __init__(self, title, story_line, poster, trailer_link):
        """
        inits the class object.
        Args:
            title (str): title of the movie
            story_line (str): short story of the movie.
            poster (str): url to poster image of that movie
            trailer_link (str): youtube link to the trailer of the movie.
        """

        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_link

    def playTrailer(self):
        """
        didn't do much as of now a popup and plays trailer
        :return:
        """
        print(self.trailer_youtube_url)
