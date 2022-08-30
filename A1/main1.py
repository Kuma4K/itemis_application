def getStringAttr(text):
    imported = False
    noTaxes = False
    text_helper = text.split()
    last = len(text_helper) - 1
    count = text_helper[0]
    price = text_helper[last]

    if text.find("imported") > 0:
        imported = True
    if text.find("book") > 0 or text.find("chocolate") > 0 or text.find("pills") > 0:
        noTaxes = True
    text_helper.remove("at")
    text_helper.remove(count)
    text_helper.remove(price)
    item = ' '.join(text_helper)
    print(count + " " + item + ": " + price + "   imported: " + str(imported) + "   No taxes: " + str(noTaxes))
    return count, item, price, imported, noTaxes


def calc_total(r):
    pass


input1 = ["1 book at 12.49", "1 music CD at 14.99", "1 chocolate bar at 0.85"]
input2 = ["1 imported box of chocolates at 10.00", "1 imported bottle of perfume at 47.50"]
input3 = ["1 imported bottle of perfume at 27.99", "1 bottle of perfume at 18.99", "1 packet of headache pills at 9.75",
          "1 box of imported chocolates at 11.25"]

input = [input1, input2, input3]
print(input)

for i in range(len(input1)):
    result = getStringAttr(input1[i])
    calc_total(result)

print("")

for i in range(len(input2)):
    result = getStringAttr(input2[i])
    calc_total(result)
