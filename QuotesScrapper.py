import requests 
import bs4
from rich.console import Console

console = Console()

def extracter(url, tag, tag_class):
    global bs, options
    r = requests.get(url)
    bs = bs4.BeautifulSoup(r.content, "html.parser")
    options = bs.body.find_all(tag, class_=tag_class)
    i = 1
    for option in options:
        console.print(f"{i}. {option.text}\n")
        i += 1
    console.print(f"0. Exit\n")

select_type = ""
extracter("https://quotes.toscrape.com/", "a", "tag")

while select_type != 0:

    select_type = int(input("Which type of thought [1-40]: "))
    if select_type != 0:
        type = options[select_type-1].text

        url = f"https://quotes.toscrape.com/tag/{type}/"

        extracter(url, "span", "text")
