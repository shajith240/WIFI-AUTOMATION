import time
import subprocess
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
import os
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, WebDriverException
import sys

class WiFiLoginAutomation:
    def __init__(self):
        self.config = self.load_config()
        self.login_url = self.config['WiFi']['login_url']
        self.username = self.config['Credentials']['username']
        self.password = self.config['Credentials']['password']
        self.previous_state = True
        
    def load_config(self):
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        if not os.path.exists(config_path):
            self.create_default_config(config_path)
        config = configparser.ConfigParser()
        config.read(config_path)
        return config
    
    def create_default_config(self, config_path):
        config = configparser.ConfigParser()
        config['WiFi'] = {
            'login_url': 'https://wifilogin.iitism.ac.in/',
            'ssid': 'ISM-Campus-Wi-Fi'
        }
        config['Credentials'] = {
            'username': 'your_username',
            'password': 'your_password'
        }
        with open(config_path, 'w') as f:
            config.write(f)
        print(f"Default config created at {config_path}")
        print("Please update the config.ini file with your credentials and WiFi details")
        sys.exit(1)

    def check_internet_connection(self):
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
            
            subprocess.check_output(
                ["ping", "-n", "1", "8.8.8.8"],
                startupinfo=startupinfo
            )
            return True
        except subprocess.CalledProcessError:
            return False

    def is_connected_to_college_wifi(self):
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
            
            result = subprocess.check_output(
                ["netsh", "wlan", "show", "interfaces"],
                startupinfo=startupinfo
            ).decode()
            return self.config['WiFi']['ssid'] in result
        except:
            return False

    def show_connection_prompt(self):
        root = tk.Tk()
        root.withdraw()
        response = messagebox.askyesno(
            "WiFi Connection Lost",
            "Would you like to reconnect to college WiFi?"
        )
        return response

    def wait_for_captive_portal(self, driver, timeout=30):
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                driver.get(self.login_url)
                time.sleep(2)
                if "wifilogin.iitism.ac.in" in driver.current_url:
                    return True
            except:
                try:
                    for url in [
                        "http://captive.apple.com",
                        "http://www.msftconnecttest.com/redirect",
                        "http://www.gstatic.com/generate_204"
                    ]:
                        driver.get(url)
                        time.sleep(2)
                        if "wifilogin.iitism.ac.in" in driver.current_url:
                            return True
                except:
                    continue
        return False

    def perform_login(self):
        try:
            print("Setting up Chrome...")
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            options.add_argument('--disable-web-security')
            options.add_argument('--allow-running-insecure-content')
            options.add_argument('--disable-dev-shm-usage')
            
            chromedriver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver.exe')
            print(f"Using ChromeDriver at: {chromedriver_path}")
            
            service = Service(executable_path=chromedriver_path)
            driver = webdriver.Chrome(service=service, options=options)
            driver.set_page_load_timeout(30)
            
            print("Waiting for captive portal...")
            if not self.wait_for_captive_portal(driver):
                print("Could not access login page")
                driver.quit()
                return False
            
            print(f"Current URL: {driver.current_url}")
            
            if "status" in driver.current_url.lower():
                print("Already logged in")
                driver.quit()
                return True
            
            wait = WebDriverWait(driver, 20)
            try:
                username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
                password_field = driver.find_element(By.NAME, "password")
                
                username_field.clear()
                username_field.send_keys(self.username)
                password_field.clear()
                password_field.send_keys(self.password)
                
                login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
                login_button.click()
                
                time.sleep(5)
                
                if "status" in driver.current_url.lower():
                    print("Login successful!")
                    driver.quit()
                    return True
                    
            except Exception as e:
                print(f"Error during login: {str(e)}")
            
            driver.quit()
            return False
            
        except Exception as e:
            print(f"Login failed: {str(e)}")
            return False

    def run(self):
        while True:
            try:
                print("\n=== Checking WiFi Status ===")
                wifi_connected = self.is_connected_to_college_wifi()
                print(f"Connected to college WiFi: {wifi_connected}")
                
                if not wifi_connected:
                    print("Please connect to college WiFi first!")
                    time.sleep(30)
                    continue
                
                internet_connected = self.check_internet_connection()
                print(f"Internet connected: {internet_connected}")
                
                if internet_connected:
                    print("Internet is working")
                    time.sleep(30)
                    continue
                
                print("\nStarting login process...")
                max_attempts = 3
                for attempt in range(max_attempts):
                    print(f"\nAttempt {attempt + 1} of {max_attempts}")
                    if self.perform_login():
                        break
                    time.sleep(2)
                
                time.sleep(30)
                
            except Exception as e:
                print(f"Error in main loop: {str(e)}")
                time.sleep(30)

if __name__ == "__main__":
    automation = WiFiLoginAutomation()
    automation.run()
