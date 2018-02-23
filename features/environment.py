from configparser import ConfigParser


def before_all(context):
    parser = ConfigParser()
    parser.read("conf/conf.ini")
    context.url=parser.get("Default","baseUrl")
    context.browser=parser.get("Default","browser")
    context.driverPath=parser.get("Default","driverPath")


