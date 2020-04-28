import requests
from bs4 import BeautifulSoup

PAGE = 1
URL = "http://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword=%ED%8C%8C%EC%9D%B4%EC%8D%AC&recruitPage="

def extract_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class":"pagination"})
  links = pagination.find_all('a')
  pages = []
  for link in links[:-1] :
    pages.append(int(link.string))
  max_page = pages[-1]
  return max_page
  
def extract_job(html):
   h2 = html.find('h2',{"class":"job_tit"})
   title = h2.find('a')['title']
   company = html.find('strong',{'class':'corp_name'})
   company = company.find('a').string
   condition = html.find('div',{'class':'job_condition'})
   location = condition.find('a').string
   link = h2.find('a')['href']
   return {'title':title, 'company':company,'location':location,'link':f'http://www.saramin.co.kr{link}'}

def extract_saram_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f'scrapping page {page}')
    result = requests.get(f"{URL}{page}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div",{"class":"item_recruit"})
    for result in results : 
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs() :
  last_extracted_page = extract_pages()

  saram_jobs = extract_saram_jobs(last_extracted_page)
  
  return saram_jobs

