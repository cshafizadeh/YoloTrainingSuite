import os
import random
import requests
from bs4 import BeautifulSoup as bs
import urllib.request
from urllib.request import Request, urlopen
from PIL import Image
import PIL
from icrawler.builtin import GoogleImageCrawler, BingImageCrawler

def collectImagesUnsplash(query: str):
    URL = f"https://unsplash.com/s/photos/{query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    req = Request(URL, headers=headers)
    page = urlopen(req).read()

    soup = bs(page, 'html.parser')
    image_tags = soup.find_all('img', class_="DVW3V")
    links = []
    for image_tag in image_tags:
        if image_tag['src'].startswith('http'):
            links.append(image_tag['src'])

    return links

def collectImagesGoogle(query: str):
    URL = f"https://www.google.co.in/search?q={query}&source=lnms&tbm=isch"
    page = requests.get(URL)

    soup = bs(page.content, 'html.parser')

    image_tags = soup.find_all('img')
    links = []
    for image_tag in image_tags:
        if image_tag['src'].startswith('http'):
            links.append(image_tag['src'])

    return links

def downloadImages(links: list[str], query: str, limit : int):
    #shuffle images to get mix from different sources
    random.shuffle(links)
    # Create the directory if it doesn't exist
    output_dir = f"images/{query}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for idx, link in enumerate(links):
        if idx >= limit:
            break
        urllib.request.urlretrieve(link, f"images/{query}/img_{idx}.jpg")
        dimensions = (140, 220)
        i = Image.open(f'images/{query}/img_{idx}.jpg')
        i.thumbnail(dimensions)

def main(query: str = "tiger", numImages: int = 100):
    limit = numImages
    imageSize = (416, 416)
    links = []
    #links.extend(collectImagesGoogle(query))
    links.extend(collectImagesUnsplash(query))
    google_crawler = GoogleImageCrawler(storage={'root_dir': f'./images/{query}'})
    google_crawler.crawl(keyword=f'{query}', max_num=limit)
    bing_crawler = BingImageCrawler(downloader_threads=4, storage={'root_dir': f'./images/{query}'})
    bing_crawler.crawl(keyword=F'{query}', max_num=limit)

    downloadImages(links, query, limit)
    print("Images downloaded")

if __name__ == "__main__":
    main()