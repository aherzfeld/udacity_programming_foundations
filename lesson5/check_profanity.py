import os
import urllib


def read_text():

    # this will work only for files in the same dir as this script
    file = open(os.path.abspath('movie_quotes.txt'))
    text = file.read()
    print(text)
    file.close()
    check_profanity(text)


def check_profanity(txt_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" +
                                txt_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This document is clean.")
    else:
        print("Could not scan document properly.")


read_text()
