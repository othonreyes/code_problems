import string
from datetime import datetime
from enum import Enum
import logging
import os

# logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
# log = logging.getLogger(__name__)


# Native Python 3 solutions -> doesn't work well with windows.
# https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
# class CustomFormatter(logging.Formatter):
#     """Logging Formatter to add colors and count warning / errors"""
#
#     grey = "\x1b[38;21m"
#     yellow = "\x1b[33;21m"
#     red = "\x1b[31;21m"
#     bold_red = "\x1b[31;1m"
#     reset = "\x1b[0m"
#     format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
#
#     FORMATS = {
#         logging.DEBUG: grey + format + reset,
#         logging.INFO: grey + format + reset,
#         logging.WARNING: yellow + format + reset,
#         logging.ERROR: red + format + reset,
#         logging.CRITICAL: bold_red + format + reset
#     }
#
#     def format(self, record):
#         log_fmt = self.FORMATS.get(record.levelno)
#         # print(fr"{record.levelno} - {log_fmt}\n")
#         print(repr(log_fmt))
#         formatter = logging.Formatter(log_fmt)
#         return formatter.format(record)
#
# create logger with 'spam_application'
# LOG_LEVEL = os.environ.get("LOGLEVEL", logging.DEBUG)
# LOG_LEVEL = logging.DEBUG
# log = logging.getLogger(__name__)
# log.setLevel(LOG_LEVEL)
#
# # create console handler with a higher log level
# colored_handler = logging.StreamHandler()
# colored_handler.setLevel(LOG_LEVEL)
# colored_handler.setFormatter(CustomFormatter())
#
# log.addHandler(colored_handler)

# Native Python 3 solutions -> using color log
LOG_LEVEL = os.environ.get("LOGLEVEL", logging.DEBUG)
LOGFORMAT = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
from colorlog import ColoredFormatter
logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOGFORMAT)
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
log = logging.getLogger(__name__)
log.setLevel(LOG_LEVEL)
log.addHandler(stream)

class Type(Enum):
    Project = 1
    Task = 2
    Comment = 3


class InvalidValueError(Exception):

    def __init__(self, message="We are fucked"):
        self.message = message


class Meta:
    # class variable
    total = 0

    def __init__(self, name, type, parent):
        self.name = name
        self._creation_date = datetime.now()
        self.type = type
        self.parent = parent
        log.info("meta constructor is over\n")

    # add a get method with the total of projects
    @staticmethod
    def get_project_count():
        return Meta.total_projects

    # override string to log.debug the name of the project and the creation date.
    def __str__(self):
        return f"{self.name} -> {self._creation_date.strftime('%b %d %Y')}"

    # a readonly property
    @property
    def creation_date(self):
        return self._creation_date

    # a regular property
    @property
    def last_update_date(self):
        return self._last_update_date

    @last_update_date.setter
    def last_update_date(self, value: datetime):
        if value is None:
            raise InvalidValueError("creation_date can't be null")
        self._last_update_date = value


class Project(Meta):

    def __init__(self, name, parent: Meta = None):
        super().__init__(name, Type.Project, parent)
        # super().parent = parent -> DOESN'T WORK: Can't call the parent until the class is created.

    def __str__(self):
        # note: can refer to the type as self even when its declared on the parent
        return f"[{self.type}] {Meta.__str__(self)}"


class Task(Meta):
    def __init__(self, name, priority, parent: Meta = None):
        super().__init__(name, Type.Task, parent)
        self.children = []

    def __str__(self):
        return f"[{self.type}] {Meta.__str__(self)}"

    def add(self, text):
        new_task = Task(1, self)
        self.children.append(new_task)


import abc


class Storage(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def insert(self, task: Task):
        pass

    @abc.abstractmethod
    def find(self, name: string):
        pass

    @abc.abstractmethod
    def update(self, task: Task):
        pass


class Notifications(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def notify(self, msg: string, *_, **kwargs):
        pass


class InMemoryNotification(Notifications):
    def __init__(self):
        self._events = []
        self._creation_date = datetime.now()
        log.info("Hello, world")

    def notify(self, msg: string, *args, **kwargs):
        timestamp = datetime.now()
        record = {"ts": timestamp, "msg": msg, **kwargs}
        self._events.append(record)

    @property
    def events(self):
        return self._events

    # This can be called but as a method because is not decorated with a descriptor like @property
    # def goku(self):
    #     return self._creation_date

    # This doesn't work. For some reason adding @property is causing the failure
    # https://stackoverflow.com/questions/13369051/why-is-aclass-aproperty-not-callable
    # UPDATE: @property works, is just that you don't have to use a method anymore
    @property
    def goku(self):
        return self._creation_date


class InMemoryStorage(Storage):
    def __init__(self):
        self.storage = dict()

    def insert(self, task: Task):
        assert task is not None
        try:
            assert task.name is not None
            self.storage[task.name] = task
        except ZeroDivisionError as error:
            log.debug(f"This shouldn't be possible {error}")
            raise
        else:
            log.debug(f"Sending a notification to another system that everything went well")
        finally:
            log.debug(f"Finishing processing task {task}")

    def find(self, name: string):
        return None

    def update(self, task: Task):
        pass


class TasksDao():
    def __init__(self, storage):
        self.storage = storage

    def saveTask(self, task: Task):
        result = self.storage.find(task.name)
        log.debug(f"\nResult: {result}")
        if result is None:
            self.storage.insert(task)
        else:
            self.storage.update(task)
        return "Saul goodman"


if __name__ == '__main__':
    travel = Project("Travel")
    log.debug(travel)
    # book_tickets = Task(1)
