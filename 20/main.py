from datetime import datetime


def inner_function():
    print("I will be invoked inside my parent function")


def parent_function(func):
    print("I will be invoked before passed function")
    func()


parent_function(inner_function)

def lights_out(func):
    def wrapper():
        if 22 <= datetime.now().hour < 7:
            func()
        else:
            print("Alarm shouldn't be raised")
    return wrapper

def invoke_alarm():
    print("Alaram ringing")

night_time = lights_out(invoke_alarm)
night_time()


@lights_out
def invoke_multiple_alarm():
    print("Multiple alaram ringing")

invoke_multiple_alarm()
