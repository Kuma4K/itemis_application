def prepare_input():
    f = open('input2.txt')
    content = f.read()
    f.close()

    content_list = content.splitlines()
    content_list.pop(0)

    result_list = []
    for x in content_list:
        e = x.split()
        e_len = len(e)
        time = e.pop(e_len-1)
        time = time.rsplit("min")
        time = time[0]
        if time == "lightning":
            time = 5
        else:
            time = int(time)
        lightning = int(time / 5)
        name = " ".join(e)
        e_list = [name, time, lightning]
        result_list.append(e_list)

    return result_list


def manipulated_input():
    input = prepare_input()
    topic = []
    time = []
    for x in input:
        topic.append(x[0])
        time.append(x[1])
    return topic, time




