import urllib.request


def read_text():
    quotes = open("/Users/luxuzheng/Leander/Python/Learning Python/Test/movie_quotes.txt")
    contents_of_file = quotes.read()
    # print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert!!!")
    else:
        print("This document has no curse words!")

read_text()
