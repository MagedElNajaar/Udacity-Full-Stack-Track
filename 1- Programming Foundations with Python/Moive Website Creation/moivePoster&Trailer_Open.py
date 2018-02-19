import webbrowser

class Movie():
    def __init__(self,title,storyline,poster,trailer):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
    def show_poster(self):
        webbrowser.open(self.poster)


toy_story = Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(toy_story.title)
print(toy_story.storyline)
toy_story.show_poster()
toy_story.show_trailer()
