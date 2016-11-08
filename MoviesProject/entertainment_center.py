import fresh_tomatoes
import media

"""Creating movie instances with movie_title, movie_storyline, poster_image_url and youtube_trailer_url"""

toy_story = media.Movie("Toy Story",
						"A story of toys coming to life",
						"https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRf3y3XLmg1ywR-I16XSDR9adON-_L_pgjwABc4-V2CPwDD-PsE",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
						"James cameron james cameron",
						"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnrUM_4A1tI_WxsWWMf0tOf76qcEH4bxDBQs0w1NOswo7MRIUL9Hy12Jo",
						"https://www.youtube.com/watch?v=5PSNL1qE6VY")

oceans_eleven = media.Movie("Oceans Eleven",
							"Classic heist movie with lots of stars",
							"https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQx6NJIHgo0knRGbA6Rr2QWSHBVXXYbqytTWpYI8ZiWrg3VMzUgV1lVDA",
							"https://www.youtube.com/watch?v=u7VTkceSsEw")

tenacious_d = media.Movie("Tenacious D",
							"Funny jack black music",
							"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQipfWAGeRwJlpc9Ap3WHVtkaduWlqnUBZVSv7fo4DMreeKRI7ETDtnVA",
							"https://www.youtube.com/watch?v=fpYbhXAFkIo")


"""creates a list of all the movies call 'movies'"""
movies = [toy_story, avatar, oceans_eleven, tenacious_d]

"""Running fresh_tomatoes function to open web browser displaying the movies and functionality"""
fresh_tomatoes.open_movies_page(movies)
