import threading
import requests


def fetch_data(url):
    print(f"start downloading from {url}\n")
    response = requests.get(url)
    # print(response.text)
    print(f"finished download from {url}, status code {response.status_code}")

# List of URLs to scrape
urls = [
    'https://google.com',
    'https://facebook.com',
    'https://youtube.com',
    'https://pinterest.com',
    'https://tinyzonetv.to',
]


# create and start thread
threads = []

for url in urls:
    thread = threading.Thread(target=fetch_data, args=(url,))
    thread.start()
    threads.append(thread)

# wait for all threads to complete
for thread in threads:
    thread.join()

print("All download completed.")
