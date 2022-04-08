import random

def traffic_lights():
    test_list = random.choice(["Red", "Yellow", "Green"])

    if test_list == "Red":
        print("Stop")
    elif test_list == "Green":
        print("Go")
    elif test_list == "Yellow":
        print("Wait")

traffic_lights()