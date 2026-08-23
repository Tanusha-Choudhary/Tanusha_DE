def transform_order(row_orders):
    transform =[]
    for order in row_orders:
        transform.append({
            "order_id":order["order_id"],
            "amount":float(order["amount"]),
            "countrty":order["country"].upper()
        })
    return transform