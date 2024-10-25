from selenium.webdriver.chrome.options import Options
import numpy as np
import cv2


def chrome_options(headless):
    chrome_options = Options()
    if headless:   
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("window-size=1280,800")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--log-level=3")
    return chrome_options


def open_png_bytes(png_bytes):
    np_arr = np.frombuffer(png_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    return img

def crop_page(image, percentage=5):
    height, width = image.shape[:2]
    crop_pixels = int(height * (percentage / 100.0))

    cropped_image = image[crop_pixels:height-crop_pixels, :]
    
    return cropped_image
