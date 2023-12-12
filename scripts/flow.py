import scripts.tasks as ts
from priority_classes.interface.interface import Interface
from priority_classes.ssw.ssw import SswRequest
from priority_classes.datahandler.datahandler import Handler
from priority_classes.app.app import BotApp
from priority_classes.task_scheduler.task_scheduler import TaskManager
from priority_classes.decorators.decorators import time_out

mg = TaskManager()

hd = Handler()

app = BotApp()

app.set_bot(
    bot_name='bot_name',
    bot_description='This bot do this',
    bot_version='1.0.0',
    bot_department='department'
)


@time_out(3)
def init_credentials():
    """
    Initialize SSW Credentials.

    This function initializes SSW credentials by opening a browser, logging in, and extracting the user information.

    :return: The user's information.
    :rtype: str
    """
    ssw = SswRequest()
    ssw.init_browser()
    ssw.login()
    user = ssw.credentials[2]
    app.set_user(user)
    return user


@app.task
def task1():
    """This task do this"""
    ts.task1()


@app.task
def task2():
    """This task do this"""
    ts.task2()


def main_ui():
    while True:
        ui = Interface(user=init_credentials())
        buttons_name = ['task1', 'task2']
        buttons_func = [task1, task2]
        ui.ui(buttons_name, buttons_func)


def main():
    mg.create_task_scheduler(app.bot_name)
    init_credentials()
    task1()
    task2()


if __name__ == '__main__':
    pass
