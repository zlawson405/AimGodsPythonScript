from selenium import webdriver
import time

username = <username goes here>
password = <password goes here>

# Add the file path for your Chrome Driver or use PATH
# driver = webdriver.Chrome(
#     executable_path=r<path to your chromedriver>)


driver.get("https://aimgods.finalmouse.com/goldenKey")

username_button = driver.find_element_by_xpath(
    "/html/body/div/div/div/div/div/form/input[1]"
)
username_button.send_keys(username)
password_button = driver.find_element_by_xpath(
    "/html/body/div/div/div/div/div/form/input[2]"
)
password_button.send_keys(password)

time.sleep(0.001)

login_button = driver.find_element_by_xpath(
    "/html/body/div/div/div/div/div/form/button"
)
login_button.click()

time.sleep(4)

go_to_use_key_button = driver.find_element_by_xpath(
    "/html/body/div/div/div/div/div/div[3]/div[2]/div[1]/div[3]/a[3]"
)
go_to_use_key_button.click()

time.sleep(2)

while True:
    use_golden_key_button = driver.find_element_by_xpath(
        "/html/body/div/div/div/div/div/div[1]/div[1]/div[1]/div/button"
    )
    use_golden_key_button.click()

    # sleep for 30 seconds while the roll spins
    time.sleep(30)
    play_again = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div/div[1]/button'
    )
    play_again.click()

    time.sleep(2)
