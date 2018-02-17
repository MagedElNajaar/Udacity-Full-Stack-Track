import urllib

def read_text():
    quotes = open("E:\WORK&STUDY\project\Udicty FULL STACK\Course 1\Profanity_Editor\movie_quotes.txt")
    contents_of_file = quotes.read()
    print (contents_of_file)
    quotes.close()
    
read_text()
