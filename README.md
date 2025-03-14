# WiFi Login Automation for ISM Campus

Hey there! 👋 Tired of manually logging into ISM-Campus-Wi-Fi every time? This script has got you covered! It automatically handles the login process, so you can focus on what matters.

## What does it do?
- Automatically connects to ISM-Campus-Wi-Fi
- Handles the login process in the background
- Runs silently when you start your PC
- Keeps you connected throughout the day

## Getting Started 🚀

### You'll need:
- Python 3.x installed on your PC
- Chrome browser
- A few minutes to set things up

### Quick Setup:
1. Get the code:
   ```bash
   git clone https://github.com/shajith240/WIFI-AUTOMATION.git
   cd WIFI-AUTOMATION
   ```

2. Set up Python environment (copy-paste these commands):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # for Windows
   pip install -r requirements.txt
   ```

3. Create your config file:
   - Copy `config.ini.template` and rename it to `config.ini`
   - Open it and put in your WiFi credentials:
   ```ini
   [WiFi]
   login_url = https://wifilogin.iitism.ac.in/
   ssid = ISM-Campus-Wi-Fi

   [Credentials]
   username = your_username    # Replace with your username
   password = your_password    # Replace with your password
   ```

### Make it run on startup (Windows) 🔄
Want it to work automatically when you turn on your PC? Here's how:

1. Find `start_hidden.vbs` in the project folder
2. Right-click → Create shortcut
3. Press `Win + R`, type `shell:startup`, and hit Enter
4. Move the shortcut to this startup folder
5. That's it! It'll run automatically next time you start your PC

### How to check if it's running? 🔍
Just double-click `check_status.bat` - it'll show you if the script is active.

## Having Problems? 🤔

Try these quick fixes:
- Make sure Chrome is up to date
- Double-check your username and password in `config.ini`
- Restart your PC if it's acting weird
- Still stuck? Open an issue on GitHub!

## Pro Tips 💡
- Keep your `config.ini` safe - it has your login info!
- The script runs silently, so don't worry if you don't see anything
- Check Task Manager if you want to see it running (look for `pythonw.exe`)

## Want to Help? 🤝
Found a bug? Have a cool idea? Feel free to:
- Open an issue
- Submit a pull request
- Share it with your friends!

---
Made with ☕ by a fellow ISM student who was tired of logging in manually!
