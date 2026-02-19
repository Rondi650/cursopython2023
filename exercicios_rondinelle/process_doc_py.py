from concurrent.futures import (ThreadPoolExecutor, as_completed, Future)
import requests
import os

os.system('cls')

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://nonexistent-subdomain.python.org/']


def load_url(url, timeout) -> str:
    response = requests.get(url=url, timeout=timeout)
    return f'{url} → {response.content}'


with ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url: dict[Future[str], str] = {}

    for url in URLS:
        t1 = executor.submit(load_url, url, 60)
        print(t1.__class__)
        future_to_url[t1] = url

    for future in as_completed(future_to_url):
        url = future_to_url[future]
        print(future_to_url,'\n')
        print(future,'\n')
        try:
            data = future.result()
            print(f'{url} page is {len(data)} bytes')
        except Exception as exc:
            print(f'{url} generated an exception: {exc}')
