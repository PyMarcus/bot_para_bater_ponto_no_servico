import configparser
import sys
import time
from configparser import SectionProxy
from platform import system
from typing import Tuple
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from dataclasses import field, dataclass
from selenium.webdriver.remote.webelement import WebElement


if system() != "Windows":
    print(f"Identified {system()}.Version avaiable only on Windows")
    sys.exit(1)


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False,
           match_args=True, kw_only=False, slots=False)
class Bot:
    __url: str = field(default="https://app.tangerino.com.br/Tangerino/pages/baterPonto/")
    __path_to_driver: str = r"../../driver/chromedriver.exe"

    @staticmethod
    def __keep_open() -> Options:
        option = Options()
        option.add_experimental_option('detach', True)
        return option

    @staticmethod
    def __close(driver: WebDriver) -> None:
        driver.close()
        sys.exit(0)

    @staticmethod
    def read_config() -> SectionProxy:
        read = configparser.RawConfigParser()
        read.read('../settings/config.cfg')
        return read["ACCESS"]

    def __open_browser(self) -> WebDriver:
        driver = webdriver.Chrome(executable_path=self.__path_to_driver, options=self.__keep_open())
        return driver

    def __access_tangerino(self) -> WebDriver:
        driver = self.__open_browser()
        driver.get(self.__url)
        driver.fullscreen_window()
        driver.implicitly_wait(30)
        return driver

    def __find_target(self) -> Tuple[WebElement, WebElement, WebDriver]:
        driver = self.__access_tangerino()
        driver.implicitly_wait(30)
        code = driver.find_element(by=By.ID, value="codigoEmpregador")
        pin = driver.find_element(by=By.ID, value="codigoPin")
        return code, pin, driver

    def __action(self) -> None:
        code, pin, driver = self.__find_target()
        code.send_keys(self.read_config().get("CODE"))
        pin.send_keys(self.read_config().get("PIN"))
        btn = driver.find_element(by=By.ID, value="registraPonto")
        btn.click()
        time.sleep(5)
        self.__close(driver=driver)

    def start(self) -> None:
        self.__action()


if __name__ == '__main__':
    bot = Bot()
    print(bot)
    bot.start()
