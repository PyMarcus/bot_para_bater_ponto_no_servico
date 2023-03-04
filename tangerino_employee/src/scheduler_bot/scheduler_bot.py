import time
import schedule
from bot import Bot


class SchedulerBot:

    def __scheduler_this(self) -> None:
        for times in ["09:00", "12:00", "13:15", "18:00"]:
            print(times)
            schedule.every().monday.at(times).do(self.__instance_from_bot_as_job)
            schedule.every().tuesday.at(times).do(self.__instance_from_bot_as_job)
            schedule.every().wednesday.at(times).do(self.__instance_from_bot_as_job)
            schedule.every().thursday.at(times).do(self.__instance_from_bot_as_job)
            schedule.every().friday.at(times).do(self.__instance_from_bot_as_job)

    def start(self) -> None:
        while True:
            self.__scheduler_this()
            schedule.run_pending()
            print("aguardando...")
            time.sleep(10)

    @staticmethod
    def __instance_from_bot_as_job() -> None:
        bot = Bot()
        bot.start()
