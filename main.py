from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

try:
    driver.get('https://www.instagram.com/accounts/login/')
    driver.maximize_window()
    print("Opened Instagram login page")

    # Wait for the presence of the username field
    waiter = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    print("Username field located")

    # Find the username and password fields and the login button
    text_box = driver.find_element(By.NAME, 'username')
    text_box.send_keys('@helloworld1262')
    password = driver.find_element(By.NAME, 'password')
    password.send_keys('shch21is')
    btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    btn.submit()
    print("Submitted login form")

    # not now button
    save_not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'x1yc6y37')))
    save_not_now.click()
    print("Clicked 'Save Not Now' button")

    # Wait for some element to ensure the page has fully loaded
    not_now_buttons = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '_a9_1')))
    not_now_buttons.click()
    print("Login complete, waiting for user to press Enter")

    # Wait for the search box to be clickable and interact with it
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Search')))
    element.click()
    print("Activated the search box")
    #
    # Wait for the search input box and enter a query
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'x1lugfcp')))
    search_box.send_keys('food')
    print("Entered 'food' in the search box")

    #Wait for the search results to load
    #Wait for the search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/explore/tags/food/")]')))

    # Find all links in the search results
    links = driver.find_elements(By.XPATH, '//a[contains(@href, "food")]')

    # Iterate over each link to extract the span text
    for link in links:
        # Find the span element within the link
        try:
            span = link.find_element(By.XPATH, './/span')
            span_text = span.text.strip()
            print(span_text)
        except NoSuchElementException:
            continue

    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'x1lugfcp')))
    search_box.clear()
    search_box.send_keys('abhitrip.in')

    # Wait for the search result to appear and click on it
    account_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/abhitrip.in/')]"))
    )
    account_link.click()
    print("mealmitra opened")  #_ap3a _aaco _aacw _aad6 _aade

    ####
    # # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_acan"))
    )

    # Click on the Follow button
    follow_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button._acan"))
    )
    if "Follow" in follow_button.text:
        follow_button.click()
        print("Page successfully followed!")
    else:
        print("Page already followed!")

    # Wait for the follow button to change to "Following"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "button._acan div._ap3a"), "Following")
    )
    print("Follow button changed to 'Following'")
    # print("Successfully unfollowed the page!")

    # try:
    #     # Wait for the div containing the image to load
    #     div_xpath = '//div[@class="_aagv"]'
    #     div_element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, div_xpath))
    #     )
    #
    #     # Find the image element within the div
    #     img_xpath = './img'
    #     image_element = div_element.find_element(By.XPATH, img_xpath)
    #
    #     # Click on the image to like the post
    #     image_element.click()

        # Wait for the like button to load and click on it
        # like_button_xpath = '//span[@class="fr66n"]/button'
        # like_button_element = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, like_button_xpath))
        # )
        # like_button_element.click()
        #
        # # Optional: Wait a few seconds after liking
        # time.sleep(2)
        #
        # # Click on the comment button to open the comment section
        # comment_button_xpath = '//svg[@aria-label="Comment"]'
        # comment_button_element = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, comment_button_xpath))
        # )
        # comment_button_element.click()
        #
        # # Wait for the comment textarea to load and enter your comment
        # comment_textarea_xpath = '//textarea[@aria-label="Add a comment…"]'
        # comment_textarea_element = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, comment_textarea_xpath))
        # )
        # comment_textarea_element.send_keys("Great post! Keep up the good work!")
        #
        # # Click on the 'Post' button to submit the comment
        # post_comment_button_xpath = '//div[@class="x1i10hfl"]/span[contains(text(), "Post")]'
        # post_comment_element = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, post_comment_button_xpath))
        # )
        # post_comment_element.click()
        #
        # # Optional: Wait a few seconds to see the comment posted
        # time.sleep(2)

    # except Exception as e:
    #     print(f"Error: {e}")







except NoSuchElementException as e:
    print(f"Element not found: {e}")
except ElementNotInteractableException as e:
    print(f"Element not interactable: {e}")
except StaleElementReferenceException as e:
    print(f"Stale element reference: {e}")
except TimeoutException as e:
    print(f"Timeout while waiting for element: {e}")
# finally:
#     driver.quit()
#     print("Browser closed")