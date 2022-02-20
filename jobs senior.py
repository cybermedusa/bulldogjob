from bs4 import BeautifulSoup
import requests
from csv import writer

with open('jobs_data_senior.csv', 'w', encoding='utf-8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Company', 'Location', 'Salary', 'Skills', 'Experience level']
    thewriter.writerow(header)

    pages = range(10)

    for page in pages:
        url = 'https://bulldogjob.pl/companies/jobs/s/experience_level,senior?page=' + str(page)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        jobs_list = soup.find_all('a', class_='search-list-item')
        for j in jobs_list:
            experience_lvl = 'Senior'
            titles = j.find('div', class_='title').text.replace('\n', '')
            companies = j.find('div', class_='company').text.replace('\n', '')
            locations = j.find('div', class_='location').text.replace('\n', '')
            if not j.find('ul', class_='tags'):
                skill1 = ''
            else:
                skill1 = j.find('ul', class_='tags').text.replace('\n', ' ')

            if not j.find('h4', class_='addon-stand-out'):
                skill2 = ''
            else:
                skill2 = j.find('h4', class_='addon-stand-out').text.replace('\n', ' ')
            if not j.find('div', class_='salary'):
                salary = ''
            else:
                salary = j.find('div', class_='salary').text.replace('\n', ' ')
            info = [titles, companies, locations, salary, skill1 + skill2, experience_lvl]
            thewriter.writerow(info)
