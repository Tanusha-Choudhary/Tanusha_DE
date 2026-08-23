import json

data  = {
    "user": {
        "id": 101,
        "name": "John Doe",
        "email": "john@example.com"
    },
    "orders": [
        {
            "order_id": "ORD001",
            "total_amount": 500.00,
            "items": [
                {"product": "Laptop", "quantity": 1, "price": 400.00},
                {"product": "Mouse", "quantity": 2, "price": 25.00},
                {"product": "Keyboard", "quantity": 1, "price": 50.00}
            ],
            "status": "delivered"
        },
        {
            "order_id": "ORD002",
            "total_amount": 300.00,
            "items": [
                {"product": "Monitor", "quantity": 1, "price": 200.00},
                {"product": "HDMI Cable", "quantity": 2, "price": 20.00},
                {"product": "USB Hub", "quantity": 1, "price": 60.00}
            ],
            "status": "shipped"
        }
    ]
}
# with open('orders.json', 'w') as f:
    # json.dump(data, f, indent=4)
def view_expenses(filename):
    try:
        with open(filename, 'r') as outfile:
            # list1=[]
            total =0
            orders = json.load(outfile)
            print(orders)
            for order in orders["orders"]:
                # print(order["total_amount"])
                total += float(order["total_amount"])
            # list1.append(order["total_amount"])
        # print(list1)
        return total
    except Exception as e:
        return (f"An error occured:{e}")
print(view_expenses('orders.json'))

    # sum = sum(list1)
    # print(sum)
    # sum=0
    # for i in list1:
    #     sum+=i
    # print(sum)