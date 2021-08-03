from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


URL_MST = 'https://news.mit.edu/'
URL_CAM = 'https://www.cam.ac.uk/research?ucam-ref=home-menu/'
HOST_CAM = 'https://www.cam.ac.uk'
URL_RISE = 'https://news.rice.edu/tag/research/'


news_mst = []
news_cam = []
news_rise = []


def get_mst():
    r = requests.get(URL_MST).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all(class_='front-page--news-article--teaser--title--link')

    for item in posts:
        data_mst = {'title': item.text, 'link': URL_MST + item['href']}
        news_mst.append(data_mst)







def get_cam():
    r = requests.get(URL_CAM).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all(class_='cam-listing-title')
    for item in posts:
        data_cam = {'title': item.text, 'link': HOST_CAM + item.find('a').get('href')}
        news_cam.append(data_cam)


get_cam()



def get_rise():
    r = requests.get(URL_RISE).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all(class_='entry-title')
    for item in posts:
        data_rise = {'title': item.text, 'link': item.find('a').get('href')}
        news_rise.append(data_rise)



get_rise()
get_mst()
get_cam()



def home(requests):
    context = {
        'news_mst': news_mst,
        'news_cam': news_cam,
        'news_rise': news_rise,

    }
    return render(requests, 'news_app/home.html', context)







