#! python3
from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.indeed.com/jobs?q=full+stack+developer&l=New+York%2C+NY&from=searchOnHP&vjk=ea2a34b0cf2515cc')

# with open('home.html', 'r') as html_file:
#     content = html_file.read()
    
#     soup = BeautifulSoup(content, 'lxml')
#     courses_cards = soup.find_all('div', class_ ='card' )
    
#     for card in courses_cards:
#         course_name = card.h5.text
#         course_price = card.a.text.split()[-1]

#         print(f'{course_name} costs {course_price}')