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
        name = " ".join(e)
        e_list = [name, time]
        result_list.append(e_list)

    return result_list




