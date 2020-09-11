rom tkinter import *
from bs4 import BeautifulSoup
import requests

# variables
URL = "https://www.instagram.com/{}/"
# Functions
def getdata():
    r = requests.get(URL.format(url.get()))
    # converting the text
    s = BeautifulSoup(r.text, "html.parser")
    # finding meta info
    meta = s.find("meta", property="og:description")
    # Collecting meta Data
    list_of_contents = meta.attrs["content"].split()
    # Displaying Output
    notif.config(
        fg="green",
        text=" {username} has {post} posts. \n Followers: {followers}  & \n Follows {following} profiles.".format(
            username=url.get(),
            followers=list_of_contents[0],
            following=list_of_contents[2],
            post=list_of_contents[4],
        ),
    )


# Main screens
master = Tk()
master.title("Freeloc - Insta Tracker")
# labels
Label(master, text="Insta Tracker", fg="red", font=("Calibiri", 15)).grid(
    sticky=N, padx=100, row=0
)
Label(master, text="Enter Username to Scrape Details :", font=("Calibiri", 12)).grid(
    sticky=N, pady=15, row=1
)
notif = Label(master, font=("Calibiri", 12))
notif.grid(sticky=N, pady=1, row=4)
# Vars
url = StringVar()
# Entry
Entry(master, width=50, textvariable=url).grid(sticky=N, row=2)
# Button
Button(master, width=20, text="GET DATA", font=("Calibiri", 12), command=getdata).grid(
    sticky=N, pady=15, row=3
)
master.mainloop()

""" FOLLOW  instagram page - @free_lines_of_code """
