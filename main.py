from selenium import webdriver
import time
import os

PROMISED_DOWN = 28.0
PROMISED_UP = 7.0

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

TWITTER_URL = "https://twitter.com/?lang=en-gb"
TWITTER_EMAIL = os.environ["EMAIL"]
TWITTER_PASSWORD = os.environ["PASSWORD"]

SPEED_URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self, url):
        self.driver.get(url)
        time.sleep(1)
        self.driver.maximize_window()

        print("clicked and agreed to cookies")
        consent_to_cookies = self.driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]')
        consent_to_cookies.click()

        print("Given permit to collect data")
        collect_data_ok = self.driver.find_element_by_class_name('svg-icon')
        collect_data_ok.click()

        time.sleep(2)

        print("Clicked GO button")
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        time.sleep(50)

        self.down = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print("Download speed is: ", self.down)

        self.up = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
        print("Upload speed is: ", self.up)

    def tweet_at_provider(self):

        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.driver.get(TWITTER_URL)
            print("I am on Twitter")
            time.sleep(2)
            sign_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div[1]/div/div[3]/div[4]/span/span')
            sign_in.click()

            print("I pressed on sign_in button")
            time.sleep(2)

            print("I pressed on sign_with_google button")

            sign_in_with_email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div[1]/div/div[3]/a/div/span/span')
            sign_in_with_email.click()

            time.sleep(2)

            email_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
            email_input.send_keys(TWITTER_EMAIL)
            time.sleep(2)
            password_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
            password_input.send_keys(TWITTER_PASSWORD)
            log_in_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
            print("Log In")
            log_in_button.click()

            time.sleep(2)

            print("Clicked button 5")
            lets_go_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[4]/div/div/div/a/div/span/span')
            lets_go_button.click()

            time.sleep(2)

            close = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div[2]/div/span/span')
            close.click()

            # @BTGroup
            print("pressed 7")
            search_twitter = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')
            search_twitter.send_keys('@bt_uk')
            search_twitter.submit()
            time.sleep(2)
            print("7 is good")

            twitt_receiver = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[3]/div/div/div/div/div[2]/div[1]')
            twitt_receiver.click()

            print("I am on BT page")
            time.sleep(2)

            messege_icon = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div')
            messege_icon.click()

            time.sleep(2)

            messege_input = self.driver.find_element_by_css_selector('[data-block="true"]')
            message = f"Hey internet provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            messege_input.send_keys(message)

            time.sleep(3)

            # Don't forget to uncoment next 2 lines to actually send the complaint

            # send_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div/aside/div[2]/div[3]')
            # send_button.click()

            time.sleep(3)
            print("Complaint is delivered")
            self.driver.quit()

        else:
            print("Your speed is Good, no complaints are necessary")
            self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

bot.get_internet_speed(SPEED_URL)

bot.tweet_at_provider()