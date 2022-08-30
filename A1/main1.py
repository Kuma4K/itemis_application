def getStringAttr(text):
    text_helper = text.split()
    last = len(text_helper) - 1
    count = text_helper[0]
    price = text_helper[last]

    text_helper.remove("at")
    text_helper.remove(count)
    text_helper.remove(price)
    item = ' '.join(text_helper)
    print(count + " " + item + ": " + price)


input = ["1 book at 12.49", "1 music CD at 14.99", "1 chocolate bar at 0.85"]

[getStringAttr(input[i]) for i in range(len(input))]
