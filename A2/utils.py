import datetime

# Read input from File input2.txt and reformat it to list for further use
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

        time = e.pop(e_len - 1)
        time = time.rsplit("min")
        time = time[0]
        e.pop(0)
        if time == "lightning":
            time = 5
        else:
            time = int(time)
        lightning = int(time / 5)
        name = " ".join(e)
        e_list = [name, time, lightning]
        result_list.append(e_list)

    return result_list

# Create two list form one result_list of prepare_input function
def manipulated_input():
    input = prepare_input()
    topic = []
    time = []
    for x in input:
        topic.append(x[0])
        time.append(x[1])
    return topic, time

# add time of this topic to global timestamp in minutes
def get_timestamp(ts, tl):
    tl = tl
    ts = ts + tl
    return ts

# Format daytime in minutes to HH:MM AM/PM format
def ts_to_str(timestamp):
    if timestamp == 0:
        timestamp = 540
    h = int(timestamp / 60)
    m = timestamp % 60
    t = datetime.time(h, m)
    return t.strftime("%I:%M%p")
