import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(PROJECT_ROOT, "conf/conf.ini")
CHROME_DRIVER_PATH=os.path.join(PROJECT_ROOT, "conf/drivers/chromedriver_2.35.exe")
IE_DRIVER_PATH=os.path.join(PROJECT_ROOT, "conf/drivers/IEDriverServer3.8.0.exe")
GECKO_DRIVER_PATH=os.path.join(PROJECT_ROOT, "conf/drivers/geckodriver-v0.19.1.exe")
DRIVER=None
HELPER=None