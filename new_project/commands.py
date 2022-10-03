import webbrowser
import os

class Commands():

    def timetables_show():
        webbrowser.open_new("https://collegetsaritsyno.mskobr.ru/edu-news/721")

    def changes():
        webbrowser.open_new("https://collegetsaritsyno.mskobr.ru/search/result")    

    def help():
        html = "help.html"
        os.startfile(html)
