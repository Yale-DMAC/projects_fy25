import time, requests, csv, re, os
from urllib.parse import urlparse
from collections import deque
from tqdm import tqdm

class WebScraper:
    def __init__(self):
        self.base_url_history = deque(maxlen=5)
        self.headers= {'Contact': 'KKH <kylene.hutchinson@yale.edu>'} #Allows webpage owners to contact you.
    
    def get_base_url(self, url):
        parsed_url = urlparse(url)
        base_url = parsed_url.netloc
        return base_url

    def adjust_sleep_time(self):
        base_url_count = {base_url: self.base_url_history.count(base_url) for base_url in set(self.base_url_history)}
        sleep_time_adjustment = max(base_url_count.values(), default=0)
        return sleep_time_adjustment
    
    def url_scraper(self, url):
        attempt = 0
        while attempt < 1:
            try:
                response = requests.get(url, headers=self.headers, timeout=30)
                reporter.processreport.writerow({'status': response.status_code, 'uri': row['uri'], 'url': url})
                if response.status_code == 200:
                    return response.status_code
                else:
                    reporter.brokenreport.writerow({'uri': row['uri'], 'title': row['title'], 'type': row['type'], 'note': row['note'], 'url': url, 'url_error': response.status_code})
                    return response.status_code
            except Exception as gen_ex:
                if 'HTTPSConnectionPool' in str(gen_ex):
                    if attempt == 0:
                        attempt += 1
                        time.sleep(5)
                    else:
                        reporter.brokenreport.writerow({'uri': row['uri'], 'title': row['title'], 'type': row['type'], 'note': row['note'], 'url': url, 'url_error': gen_ex})
                        return gen_ex
                else:
                    reporter.processreport.writerow({'status': gen_ex, 'uri': row['uri'], 'url': url}) 
                    reporter.brokenreport.writerow({'uri': row['uri'], 'title': row['title'], 'type': row['type'], 'note': row['note'], 'url': url, 'url_error': gen_ex})
                    return gen_ex

    def scrape_url(self, url):
        base_url = self.get_base_url(url)
        self.base_url_history.append(base_url)
        sleep_time = self.adjust_sleep_time()
        self.url_scraper(url)
        time.sleep(sleep_time)
    
    def scrape_multiple_urls(self, urls):
        for url in urls:
            self.scrape_url(url)

class Reports:
    def __init__(self, folder):
        self.file_limit = 2
        self.file_count = 0
        self.file_num = 0
        self.folder = folder
        if os.path.exists(f'{folder}'):
            pass
        else:
            os.makedirs(f'{folder}')
    
    def csvreporter(self):
        date_str = time.strftime("%y%m%d")
        updatefile = open(f'{self.folder}/{date_str}_urls_status.csv', 'a', encoding='utf8', newline='')
        self.processreport = csv.DictWriter(updatefile, fieldnames=['uri', 'status', 'url'])
        self.processreport.writeheader()
        reportfile = open(f'{self.folder}/{date_str}_broken_urls.csv', 'a', encoding='utf8', newline='')
        self.brokenreport = csv.DictWriter(reportfile, fieldnames=['uri', 'title', 'type', 'note', 'url', 'url_error'])
        self.brokenreport.writeheader()



reporter = Reports('files/broken_urls/files')
scraper = WebScraper()
for reporter.file_num in range(0, 28):
    urls_to_scrape = []
    reporter.file_num += 1
    if reporter.file_count == reporter.file_limit:
        print(time.strftime("%H:%M:%S"))
        time.sleep(1800)
        reporter.file_count = 0
    with open(f'files/broken_urls/files/250130_urls_{reporter.file_num}.csv', 'r', encoding='utf8', errors='replace') as infile:
        print(time.strftime("%H:%M:%S"))
        reader = csv.DictReader(infile)
        reporter.file_count += 1
        for row in reader:
            url_pattern = r'https?://[^\s"<>\\]+'
            urls = re.findall(url_pattern, row['note'])
            urls_to_scrape.append({'uri': row['uri'], 'note': row['note'], 'type': row['type'], 'title': row['title'], 'urls': urls})
    for row in tqdm(urls_to_scrape, desc=f"Processing urls for file {reporter.file_num}", unit="URL"):
        url = row['urls']
        scraper.scrape_multiple_urls(url)