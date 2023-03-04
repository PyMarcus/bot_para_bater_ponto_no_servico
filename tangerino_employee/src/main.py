from scheduler_bot import SchedulerBot


def main() -> None:
    bot = SchedulerBot()
    bot.start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        ...
