from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd


load_dotenv()
WEBSITE = os.getenv("WEBSITE")
LOCAL_PATH = os.getenv("LOCAL_PATH")


service = Service(executable_path=LOCAL_PATH)
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.get(WEBSITE)


container = driver.find_element(By.CLASS_NAME, "adbl-impression-container ")
products = container.find_elements(By.XPATH,'.//li[contains(@class, "productListItem")]')

titles = []
authors = []
runtimes = []


for product in products:
    title = product.find_element(By.XPATH, ".//h3[contains(@class, 'bc-heading')]").text
    author = product.find_element(By.XPATH, ".//li[contains(@class, 'authorLabel')]").text
    runtime = product.find_element(By.XPATH, ".//li[contains(@class, 'runtimeLabel')]").text
    titles.append(title)
    authors.append(author)
    runtimes.append(runtime)


df = pd.DataFrame(
    {
        'titles': titles,
        'authors': authors,
        'runtimes': runtimes
    }
)
df.to_csv('./output/output.csv', index=False)


