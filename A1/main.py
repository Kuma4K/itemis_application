import utils1

def main():
    input = utils1.read_input_from_file()
    #Loop on all inputs and print Output
    for j in range(len(input)):
        priceSum = 0
        taxSum = 0
        print("Output " + str(j+1) + ":")
        for i in range(len(input[j])):
            item_list = utils1.getStringAttr(input[j][i])
            tax_list = utils1.calc_total(item_list)
            priceSum += tax_list[0]
            taxSum += tax_list[1]
            print(str(item_list[0]) + ": " + "{:.2f}".format(tax_list[0]))
        print("> " + "Sales Taxes: " + "{:.2f}".format(taxSum) + "\n> Total: " + "{:.2f}".format(priceSum))


if __name__ == '__main__':
    main()
