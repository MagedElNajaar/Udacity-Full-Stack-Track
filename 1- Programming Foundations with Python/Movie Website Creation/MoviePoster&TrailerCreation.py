import webbrowser

class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_poster(self):
        webbrowser.open(self.poster_image_url)
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
toy_story = Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.title)
print(toy_story.storyline)
toy_story.show_poster()
toy_story.show_trailer()
