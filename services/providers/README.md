# Providers

This microservice fetch several information sources to build the db.

## Setup from scratch

Install Chrome

1. Download the package

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

2. Install google-chrome-stable_current_amd64.deb package

```bash
sudo dpkg -i ./google-chrome-stable_current_amd64.deb
```
3. If an error occur, run this command and try step 2 again.

```bash
sudo apt-get install -f
```

Install a Selenium library

```bash
pip install selenium
```

Install undetected-chromedriver

1. Follow the project updates [here](https://github.com/ultrafunkamsterdam/undetected-chromedriver)

```bash
pip install undetected-chromedriver
```

Install browser drivers

Follow [this quick reference](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) for the links of the drivers you want to use.

1. For downloading [chromedriver](https://chromedriver.chromium.org/downloads) look for the latest supported version in [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) and proceed to download.

```bash
https://chromedriver.chromium.org/downloads
```

