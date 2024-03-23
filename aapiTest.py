import requests
from bs4 import BeautifulSoup
import time
import random
i=0
a = [
    "apple", "banana", "orange", "grape", "pineapple",
    "strawberry", "kiwi", "watermelon", "pear", "peach",
    "car", "bus", "train", "bicycle", "motorcycle",
    "dog", "cat", "rabbit", "hamster", "parrot",
    "house", "apartment", "building", "castle", "cottage",
    "computer", "phone", "tablet", "laptop", "keyboard",
    "book", "newspaper", "magazine", "dictionary", "novel",
    "pen", "pencil", "marker", "crayon", "eraser",
    "teacher", "student", "school", "university", "classroom",
    "football", "basketball", "soccer", "volleyball", "tennis",
    "cake", "cookie", "candy", "chocolate", "ice cream",
    "ocean", "river", "lake", "pond", "stream",
    "tree", "flower", "grass", "bush", "plant",
    "sun", "moon", "star", "sky", "cloud",
    "mountain", "hill", "valley", "canyon", "plateau",
    "bird", "fish", "lion", "tiger", "elephant",
    "apple", "banana", "orange", "grape", "pineapple",
    "strawberry", "kiwi", "watermelon", "pear", "peach",
    "carrot", "potato", "tomato", "cucumber", "lettuce"
]
while True:
     print(i)
     i+=1
     wait_time = random.randint(3, 4)
     time.sleep(wait_time)
     print(a[i//len(a)]);
     url = 'https://www.google.com/search?q='+  a[i//len(a)]+'&num=100&ie=UTF-8&sourceid=chrome'  # Replace this with the actual API endpoint

     # Sending a GET request
     response = requests.get(url)

     # Check if the request was successful (status code 200)
     if response.status_code == 200:
         # Accessing the response data (assuming the API returns JSON)
         
         soup = BeautifulSoup(response.text, 'html.parser')
         
         div_with_class = soup.find_all('div', class_='Gx5Zad fP1Qef xpd EtOod pkphOe')  # Replace 'your-class-name' with the desired class
         for div in div_with_class:
              
              first_a_tag = div.find('a')
              href = first_a_tag.get('href')
              print(href)
              print("-------")
         
     else:
         print('Failed to retrieve data from the API:', response.status_code)
