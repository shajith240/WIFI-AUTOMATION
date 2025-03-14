# WiFi Login Automation

Automated WiFi login system for ISM-Campus-Wi-Fi network.

## Prerequisites
- Python 3.x
- Chrome browser installed (for Selenium automation)

## Setup
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `config.ini` file with your credentials:
   ```ini
   [WiFi]
   login_url = https://wifilogin.iitism.ac.in/
   ssid = ISM-Campus-Wi-Fi

   [Credentials]
   username = your_username
   password = your_password
   ```

## Usage
Run `python wifi_login_automation.py` to start the automation.
## Troubleshooting
- If you encounter WebDriver issues, ensure Chrome browser is up to date
- The script automatically manages ChromeDriver through webdriver-manager
