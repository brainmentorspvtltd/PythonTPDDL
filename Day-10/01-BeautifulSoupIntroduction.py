# Beautiful Soup / Scrapy
import bs4 as bs
import urllib.request

# url = urllib.request.urlopen('https://in.bookmyshow.com/delhi')

user_input = input("Enter product name : ")
url = urllib.request.urlopen('https://www.flipkart.com/search?q='+user_input)
soup = bs.BeautifulSoup(url, 'lxml')
# print(url)

# data = soup.find_all('p')
# data = soup.find_all('li', class_='dropdown1')
# print(data)

data = soup.find_all('div', class_='_1-2Iqu')
for d in data:
    print(d.text)