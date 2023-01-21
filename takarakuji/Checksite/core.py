import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

Agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'

class ProxyTable:
    IP: str = None
    PORT: str = None
    def __init__(self, ip: str, port: str):
        self.IP = ip
        self.PORT = port

    def __str__(self):
        return self.IP + ":" + self.PORT

class ProxyRotation(object):
    def __init__(self, proxy: str=None):
        self.proxy = proxy
        self.Url = 'http://www.cybersyndrome.net/search.cgi?q=&a=ABCD&f=s&s=new&n=500'

    def Check(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument(f'--user-agent={Agent}')
        if self.proxy is not None:
            options.add_argument(f'--proxy-server=http://{self.proxy}')
        service = Service(executable_path=ChromeDriverManager().install())
        Driver = webdriver.Chrome(service=service, options=options)
        Driver.get(self.Url)
        soup = BeautifulSoup(Driver.page_source)
        table = soup.find('table').find_all('tr')

        # Table Index 0
        tableTitle = table.pop(0)
        tableTitle = tableTitle.getText(',').split(',')
        tableTitle.insert(0, 'index')

        proxyInfoTable = []
        for tr in table:
            item = tr.getText(',').split(',')
            if len(item) == 4:
                item.insert(2, '')
            try:
                ret = requests.get(
                    'https://ipinfo.io',
                    proxies={'http': f'http://{item[1]}', 'https': f'http://{item[1]}'}
                )
                if ret.status_code == 200:
                    proxyInfoTable.append(item)
            except requests.exceptions.Timeout as error:
                print(f"Proxy: {item[1]} TimeOut")
            except requests.exceptions.ProxyError as error:
                print(f"Proxy: {item[1]} ProxyError")

        proxtable = pd.DataFrame(proxyInfoTable, columns=tableTitle)

        proxlist = None
        if os.path.isfile('../config/proxy.tbl'):
            proxylist = pd.read_pickle('../config/proxy.tbl')
        else:
            proxtable.to_pickle('../config/proxy.tbl')

        if proxlist is not None:



    def Update(self):
        pass

if __name__ == '__main__':
    # proxytable1 = ProxyTable()
    # proxytable1.IP = '118.27.113.167'
    # proxytable1.PORT = '8080'
    # IP, PORT = str(proxytable1).split(":")
    #
    # proxies = {
    #     'http': f'http://{IP}:{PORT}',
    #     'https': f'http://{IP}:{PORT}',
    # }
    # try:
    #     ret = requests.get('https://ipinfo.io', proxies=proxies)
    #     print(ret.text)
    # except requests.exceptions.ProxyError as proxyError:
    #     print(proxyError)
    ProxyRotation().Check()