import webbrowser

class Movie():
	"""This class provideds a way to store movie related information"""

	"""Static Class level variable not currently used"""
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	""" This method initializes the Movie class and it's instance variables"""

	def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	"""This method opens the youtube trailer for a given movie"""

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)