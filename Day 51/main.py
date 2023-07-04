import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

DOWNLOAD_MBPS = 190
UPLOAD_MBPS = 35
email = os.environ.get("tuser")
password = os.environ.get('tpass')