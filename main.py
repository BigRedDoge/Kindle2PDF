from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import argparse
import json

from util import chrome_options, open_png_bytes, crop_page


def convert_book(book_url, headless, save_name, webdriver_path, cookies_path):
    print("Opening the book")
    cookies = json.load(open(cookies_path, "r"))
    with webdriver.Chrome(service=Service(webdriver_path), options=chrome_options(headless)) as driver:
        try:
            driver.get("https://google.com")
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.get(book_url)
            webdriver_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "kr-renderer-container-fullpage")))
            print("Book opened successfully")
            book_pages = scan_book(driver)
        except Exception as e:
            print("Failure opening book:", e)

    process_book(book_pages, save_name)


def scan_book(driver):
    print("Scanning the book")
    book_pages = []
    while True:
        try:
            book_page = driver.find_element(By.ID, "kr-renderer")
            book_pages.append(book_page.screenshot_as_png())
            next_page = driver.find_element(By.ID, "kr-chevron-right")
            next_page.click()
            time.sleep(0.25)
        except Exception as e:
            print("End of book")
            break
    book_pages = [crop_page(open_png_bytes(page)) for page in book_pages]
    print("Book scanned successfully")

    return book_pages


def process_book(book_pages, save_name):
    print("Analyzing the book pages")
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="Enter the url of the kindle book", required=True)
    parser.add_argument("--headless", help="Run the script in headless mode", action="store_true")
    parser.add_argument("--save_name", help="Output file name", default="book.pdf")
    parser.add_argument("--webdriver", help="Path to the webdriver", default="./chromedriver")
    parser.add_argument("--cookies", help="Path to the cookies json file", default="cookies.json")
    args = parser.parse_args()
    convert_book(*args)