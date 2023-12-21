#! python3
from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    courses_cards = soup.findAll('div', class_ ='cards' )
    
    for card in courses_cards:
        print(card.h5)