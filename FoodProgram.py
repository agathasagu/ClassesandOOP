import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

order_total = 0


customer1 = fc.Customer(
    570,
    "Danni Sellyar",
    "97 Mitchell Way Hewitt Texas 76712",
    "jdsellyarft@gmpg.org",
    "254-555-9362",
    False,
)


""" customer1 = fc.Customer(
    569,
    "Aubree Himsworth",
    "	1172 Moulton Hill Waco Texas 76710",
    "ahimsworthfs@list-manage.com",
    "254-555-2273",
    True,
) """


customer_trans = []

for key in dict:
    if dict[key][3] == customer1.get_customerid():
        customer_trans.append(
            fc.Transaction(dict[key][0], dict[key][1], dict[key][2], dict[key][3])
        )

# printing

print("Customer Name:", customer1.get_name())
print("Phone:", customer1.get_phone())


for trans in customer_trans:
    print(f"Order Item: {trans.get_item_name()} Price: {trans.get_cost()}")
    order_total += trans.get_cost()

print("Total Cost: $", format(order_total, ",.2f"), sep="")

if customer1.is_member():
    discount = 0.2 * order_total
    order_total -= discount

    print("Member Discount: ${:.2f}".format(discount))
    print("Total Cost after discount: ${:.2f}\n".format(order_total))
