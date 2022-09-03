import input_conv


def get_data():
    data1 = input_conv.prepare_input()
    print(data1)


def get_data1():
    topic, time = input_conv.manipulated_input()
    if len(topic) == len(time):
        print(topic)
        print(time)


get_data()
get_data1()
