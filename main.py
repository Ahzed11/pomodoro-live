import datetime
import time
import yaml


def fprint(message):
    file = open("txt/timer.txt", "w")
    file.write(message)
    file.close()


def loop(duration):
    end = datetime.datetime.now() + datetime.timedelta(
        minutes=duration
    )
    while datetime.datetime.now() < end:
        fprint(str(end - datetime.datetime.now())[:-7])
        time.sleep(1)


if __name__ == '__main__':
    config = None

    with open("config/config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)

    while True:
        # Beginning message
        fprint(config["messages"]["start"])
        time.sleep(5)

        # Pomodoro loop
        loop(config["duration"]["pomodoro"])

        # Break message
        fprint(config["messages"]["break"])
        time.sleep(5)

        # Break loop
        loop(config["duration"]["break"])

        # End message
        fprint(config["messages"]["end"])
        time.sleep(5)
