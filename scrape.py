from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

from random import randint
from time import sleep
import threading
import time

display = Display(visible=0, size=(800, 600))
display.start()

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)

def print_function(stop_event, message):
    dots = "."
    while not stop_event.is_set():
        print("\033[K", f"{message}{dots}", end='\r', flush=True)
        sleep(1)
        dots = dots + "."

while True:
    should_stop = threading.Event()
    thread = threading.Thread(target=print_function, args=[should_stop, "Requesting data from XC3 SE webpage"])
    thread.start() # Start printing the status message in its own thread

    # Get the data from the page.
    driver.get('https://www.nintendo.com/store/products/xenoblade-chronicles-3-special-edition-switch/')
    # item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//script[@type='text/javascript']"))).get_attribute('innerHTML')
    item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__NEXT_DATA__"))).get_attribute('innerHTML')
    data = json.loads(item)

    # Data has been retrieved
    should_stop.set() # Signal to the status message to stop printing
    print("\nData has been received.")

    releaseDate = data["props"]["pageProps"]["product"]["releaseDateDisplay"]

    if releaseDate != "TBD":
        print(f"Posted release date: {releaseDate} - STATUS: GAME IS OUT BUY NOW!\n")
    else:
        print(f"Posted release date: {releaseDate} - STATUS: Not yet... :(\n")

    start_time = time.time()
    seconds_to_next = randint(60,360);
    elapsed_seconds = 0

    while elapsed_seconds < seconds_to_next:
        sleep(1)
        elapsed_seconds = int(time.time()) - int(start_time)
        countdown = int(seconds_to_next) - elapsed_seconds
        print("\033[K", f"Checking for release of XC3 SE in {countdown}s.", end='\r', flush=True)
    print("\n")
