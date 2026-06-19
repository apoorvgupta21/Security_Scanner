import requests
import ssl, socket
import logging
from security_header import SECURITY_HEADERS

logging.basicConfig(
    filename="security_report.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class SecurityScanner:

    def __init__(self, url):
        self.url = url

    def fetch_site(self):
        self.response = requests.get(self.url)
        self.header = self.response.headers
        self.status_code = self.response.status_code
        return self.header, self.status_code  

    def check_headers(self, header):
        for header in SECURITY_HEADERS:
            if header in self.response.headers:
                print(f"{header}: PASS")
                logger.info(f"{header}: PASS")
            else:
                print(f"{header}: FAIL")
                logger.info(f"{header}: FAIL")

with open("sites.txt", 'r') as sites:
    for site in sites:
        site = site.strip()
        runscan = SecurityScanner(site)
        list1 = runscan.fetch_site()
        runscan.check_headers(list1[1])

#url = "https://google.com"
#print(response.status_code)
#print(response.headers)
#response = requests.get(url)

#runscan = SecurityScanner(url)
#list1 = runscan.fetch_site()
#runscan.check_headers(list1[1])



        
        


