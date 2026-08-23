from utils.transform import transform_order
sample_data = [{"order_id": 1, "amount":450,"country": "us"},
               {"order_id": 2, "amount":450,"country": "ind"},
               {"order_id": 3, "amount":450,"country": "as"},
               {"order_id": 4, "amount":450,"country": "us"}
               ]
T1= transform_order(sample_data)
print(T1)