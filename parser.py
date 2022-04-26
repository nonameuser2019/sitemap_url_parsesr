import requests
from bs4 import BeautifulSoup


def get_html(url):
    page = requests.get(url)
    print(page)
    if page.status_code == 200:
        return page.content


def get_content(page):
    urls_list = []
    soup = BeautifulSoup(page, 'html.parser')
    urls = soup.find_all('loc')
    for url in urls:
        urls_list.append(url.string)
    return urls_list


def write_result(urls_list):
    with open('request.csv', 'a') as f:
        for url in urls_list:
            f.write(f'{url}\n')


if __name__ == '__main__':
    url = 'https://steinwaygrand.com/sitemap_blogs_1.xml'
    urls_list = get_content(get_html(url))
    write_result(urls_list)



