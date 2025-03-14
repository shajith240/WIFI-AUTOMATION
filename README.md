# WiFi Login Automation

Automated WiFi login system for ISM-Campus-Wi-Fi network.

## Prerequisites
- Python 3.x
- Chrome browser installed (for Selenium automation)

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/shajith240/WIFI-AUTOMATION.git
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up configuration:
   - Copy `config.ini.template` to `config.ini`
   - Edit `config.ini` and update with your credentials:
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

## Auto-start Setup (Windows)
To make the script run automatically when Windows starts:

1. Create a shortcut to `start_hidden.vbs`:
   - Right-click on `start_hidden.vbs`
   - Select "Create shortcut"

2. Move the shortcut to Windows Startup folder:
   - Press `Win + R`
   - Type `shell:startup`
   - Press Enter
   - Move the created shortcut to this folder

3. Verify the setup:
   - Restart your PC
   - The script will run automatically in the background
   - To check if it's running:
     - Run `check_status.bat`
     - Look for `pythonw.exe` in the list

## Troubleshooting
- If you encounter WebDriver issues, ensure Chrome browser is up to date
- The script automatically manages ChromeDriver through webdriver-manager
- If auto-start isn't working:
  - Check if the paths in `start_hidden.vbs` match your installation
  - Ensure the virtual environment is properly set up
  - Verify all dependencies are installed
  - Check Windows Task Manager for any error messages

## Important Files
- `start_hidden.vbs`: Script to run the automation silently in background
- `check_status.bat`: Utility to verify if the automation is running
- `config.ini`: Your configuration file (create from template)
