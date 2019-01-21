from pathlib import Path

from selenium import webdriver
from selenium.webdriver import FirefoxProfile, Proxy
import os, time

from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.firefox.options import Options


p = Proxy()
p.proxy_type = ProxyType.MANUAL
p.httpProxy = "1.1.1.1:8080"

x = Options()
x.accept_insecure_certs = True

# x.headless = True
# x.proxy = p
# x.accept_insecure_certs = True
# x.set_preference("browser.download.defaultFolder", str(Path(os.getcwd()).parent) + os.path.sep +  "AutomationDownloads")

# myProxy = "86.111.144.194:3128"
# proxy = Proxy({
#     'proxyType': ProxyType.MANUAL,
#     'httpProxy': myProxy,
#     'ftpProxy': myProxy,
#     'sslProxy': myProxy,
#     'noProxy':''})


fp = FirefoxProfile()
fp.assume_untrusted_cert_issuer = False
fp.accept_untrusted_certs = True
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/msword,application/vnd.ms-powerpoint,application/vnd.openxmlformats-officedocument.presentationml.presentation,application/octet-stream,application/msexcel,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,text/csv,text/txt,application/pkcs10,application/x-msdownload,application/csv,text/html,application/force-download,application/pkix-cert")
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.useDownloadDir", True)
fp.set_preference("browser.download.defaultFolder", str(Path(os.getcwd()).parent) + os.path.sep +  "AutomationDownloads")
fp.set_preference("browser.startup.homepage", "http://www.google.com")
fp.set_proxy(p)

# driver = webdriver.Firefox(firefox_profile=fp)
driver = webdriver.Firefox(options=x)
driver.maximize_window()
time.sleep(60)
driver.quit()
