import requests
from bs4 import BeautifulSoup
import json

def word_frequency(url):
    # Fetch the web page content
    response = requests.get(url)
    html = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Get all the text from the HTML content
    text = soup.get_text()

    # Split the text into words and remove any punctuation
    words = text.lower().split()
    words = [word.strip('.,!?"\'') for word in words]

    # Create a dictionary to store the frequency of each word
    frequency = {}

    # Count the frequency of each word
    for word in words:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1

    # Convert the frequency dictionary to a list of tuples
    word_list = [(word, frequency[word]) for word in frequency]

    # Sort the word list by frequency (descending)
    word_list = sorted(word_list, key=lambda x: x[1], reverse=True)

    # Convert the word list to a JSON string
    json_string = json.dumps(word_list)

    # Return the JSON string
    return json_string
url = 'https://www.example.com'
result = word_frequency(url)
print(result)
