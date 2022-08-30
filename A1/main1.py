import math

"""Get 1 line of input and Returns Count of Items, item name, item price, if imported and if taxes"""
def getStringAttr(text):
    imported = False
    taxes = True
    text_helper = text.split()
    last = len(text_helper) - 1
    count = text_helper[0]
    price = text_helper[last]
    if text.find("imported") > 0:
        imported = True
    if text.find("book") > 0 or text.find("chocolate") > 0 or text.find("pills") > 0:
        taxes = False
    text_helper.remove("at")
    text_helper.remove(count)
    text_helper.remove(price)
    item = ' '.join(text_helper)
    return count, item, price, imported, taxes


"""Get price and boolean for Imported and taxes; Returns total item price and total item taxes """
def calc_total(r):
    tax = 0
    importTax = 0
    price = float(r[2])
    imported = r[3]
    taxes = r[4]
    if taxes:
        tax = price * 0.1
        tax = myRound(tax)
    if imported:
        importTax = price * 0.05
        importTax = myRound(importTax)
    sumTaxes = float("{:.2f}".format(tax + importTax))
    total = float("{:.2f}".format(price + sumTaxes))
    return total, sumTaxes


"""round on x.x5 or x.x0"""
def myRound(x, base=0.05):
    return float("{:.2f}".format(float(base * math.ceil(x / base))))


input1 = ["1 book at 12.49", "1 music CD at 14.99", "1 chocolate bar at 0.85"]
input2 = ["1 imported box of chocolates at 10.00", "1 imported bottle of perfume at 47.50"]
input3 = ["1 imported bottle of perfume at 27.99", "1 bottle of perfume at 18.99", "1 packet of headache pills at 9.75",
          "1 box of imported chocolates at 11.25"]
input = [input1, input2, input3]

"""   Loop on all inputs and print Output"""
for j in range(len(input)):
    priceSum = 0
    taxSum = 0
    print("Output " + str(j+1) + ":")
    for i in range(len(input[j])):
        item_list = getStringAttr(input[j][i])
        tax_list = calc_total(item_list)
        priceSum += tax_list[0]
        taxSum += tax_list[1]
        print("> " + str(item_list[0]) + " " + item_list[1] + ": " + "{:.2f}".format(tax_list[0]))
    print("> " + "Sales Taxes: " + "{:.2f}".format(taxSum) + "\n> Total: " + "{:.2f}".format(priceSum))