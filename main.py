import requests
import fake_useragent
from bs4 import BeautifulSoup

headers = {
    'User-Agent': fake_useragent.UserAgent().chrome
}

def start():
    for page in range(30):
        link = f"https://hh.ru/search/resume?experience=between3And6&experience=moreThan6&job_search_status=unknown&job_search_status=active_search&job_search_status=looking_for_offers&job_search_status=has_job_offer&relocation=living_or_relocation&skill=15098&skill=36694&gender=unknown&text=C%23+developer&isDefaultArea=true&ored_clusters=true&order_by=relevance&search_period=0&logic=normal&pos=full_text&exp_period=all_time&page={page}"
        resp = requests.get(link, headers=headers).text
        soup = BeautifulSoup(resp, "lxml")
        block = soup.find("main", id="a11y-main-content")
        href = block.find_all("a")
        for href1 in href:
            mini_link = href1.get("href")
            print(fr"{href1.text}: https://hh.ru/{mini_link}")
            with open("C#.txt", "a") as file:
                try:
                    file.write(fr"{href1.text}: https://hh.ru/{mini_link}")
                    file.write("\n")
                except UnicodeError:
                    continue
        print("\n",f"Страница: {page} <----------", "\n")
        with open("C#.txt", "a") as file1:
            file1.write("\n")
            file1.write(f"Страница: {page+2} <----------")
            file1.write("\n")

if __name__ == "__main__":
    start()