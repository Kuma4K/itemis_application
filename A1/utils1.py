import math


def read_input_from_file():
    f = open('input1.txt')
    content = f.read()
    f.close()

    content_list = content.splitlines()
    content_list.pop(0)
    content_list.pop(0)

    input1 = [content_list[0], content_list[1], content_list[2]]
    input2 = [content_list[4], content_list[5]]
    input3 = [content_list[7], content_list[8], content_list[9], content_list[10]]
    input = [input1, input2, input3]
    return input


# Get 1 line of input and Returns number of Items, item name, item price, if imported and if taxes
def getStringAttr(text):
    imported = False
    taxes = True
    text_helper = text.split()
    last = len(text_helper) - 1
    price = text_helper[last]
    if text.find("imported") > 0:
        imported = True
    if text.find("book") > 0 or text.find("chocolate") > 0 or text.find("pills") > 0:
        taxes = False
    text_helper.remove("at")
    text_helper.remove(price)
    item = ' '.join(text_helper)
    return item, price, imported, taxes


# Get price and boolean for Imported and taxes; Returns total item price and total item taxes
def calc_total(r):
    tax = 0
    importTax = 0
    price = float(r[1])
    imported = r[2]
    taxes = r[3]
    if taxes:
        tax = price * 0.1
        tax = myRound(tax)
    if imported:
        importTax = price * 0.05
        importTax = myRound(importTax)
    sumTaxes = float("{:.2f}".format(tax + importTax))
    total = float("{:.2f}".format(price + sumTaxes))
    return total, sumTaxes


# round on x.x5 or x.x0
def myRound(x, base=0.05):
    return float("{:.2f}".format(float(base * math.ceil(x / base))))
