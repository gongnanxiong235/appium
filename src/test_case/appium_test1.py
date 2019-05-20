from src.common.driver_configure import driver_configure
from src.common.base_page import Base_page
from src.common.before_case import before_test_check
from appium.webdriver.common import mobileby

drive=driver_configure ().get_driver ()
base_drive=Base_page ( drive )
by=mobileby.MobileBy ()


before_test_check ( base_drive=base_drive, by=by )

