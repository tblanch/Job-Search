import xlwt
from xlwt import Workbook
import requests
from bs4 import BeautifulSoup
wb = Workbook()
URL = 'https://www.indeed.com/jobs?q=computer+science+intern&l=Boston%2C+MA'
page = requests.get(URL)
#print(page.text)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='resultsCol')

#print(results.prettify())

job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')

row = 1
c1 = 1
c2 = 2
c3 = 3
c4 = 4

sheet1 = wb.add_sheet('sheet1')

sheet1.write(0,c1,'Job Title')
sheet1.write(0,c2,'Company Name')
sheet1.write(0,c3,'Location')
sheet1.write(0,c4,'Salary')

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('span', class_='company')
    location_elem = job_elem.find('div', class_='location accessible-contrast-color-location')
    if location_elem is None:
        location_elem = job_elem.find('span', class_='location accessible-contrast-color-location')
    salary = job_elem.find('span', class_ = 'salaryText')
    print(title_elem.text)
    sheet1.write(row,c1,title_elem.text)
    print(company_elem.text)
    sheet1.write(row, c2, company_elem.text)
    if location_elem is not None:
        print(location_elem.text)
        sheet1.write(row, c3, 'none')
    else:
        print('none Location')
        sheet1.write(row, c3, title_elem.text)
    if salary is not None:
        print(salary.text)
        sheet1.write(row, c4, salary.text)
    else:
        print('none salary')
        sheet1.write(row, c4,'none')
    print()
    row = row+1

wb.save('trial2.xls')




