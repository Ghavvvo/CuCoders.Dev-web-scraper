import json
from bs4 import BeautifulSoup
import requests

page_num = 1

job_postings = []

while True:

    if page_num == 1:
        url = "https://cucoders.dev/empleos/"
    else:
        url = f"https://cucoders.dev/empleos/{page_num}/"

    response = requests.get(url)

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = soup.find_all('div', class_='inline-flex items-center w-full p-4 pb-1 md:pb-2 text-gray-500 dark:text-gray-100 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg astro-TUHLWDKK')

    for job in jobs:
        title = job.find('a', class_='w-full text-base md:text:lg text-gray-800 dark:text-gray-300 font-semibold line-clamp-2 md:line-clamp-1 astro-TUHLWDKK')
        description = job.find('a', class_='w-full my-2 text-sm md:text:base text-gray-600 dark:text-gray-300 line-clamp-3 md:line-clamp-2 astro-TUHLWDKK')


        categories_div = job.find('div', class_='flex categories flex-wrap -ml-2 justify-center md:justify-start border-t pt-2 mt-2 md:border-none md:pt-0 md:mt-0 astro-TUHLWDKK')


        categories = [tag.text.strip() for tag in categories_div.find_all(True) if tag.text.strip()]


        categories = list(set(categories))

        job_postings.append({
            "Title": title.text if title else 'N/A',
            "Description": description.text if description else 'N/A',
            "Categories": categories
        })


    page_num += 1


with open('job_postings.json', 'w', encoding='utf-8') as file:
    json.dump(job_postings, file, ensure_ascii=False, indent=4)

print(len(job_postings))