from src.common.driver_configure import driver_configure
from src.common.base_page import Base_page
from src.util.before_case import Before_Case
from appium.webdriver.common import mobileby

drive=driver_configure ().get_driver ()
base_drive=Base_page ( drive )
by=mobileby.MobileBy ()


case=Before_Case(base_drive=base_drive,by=by)
case.before_test_check()

