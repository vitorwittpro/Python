sandwich_orders = ['cheese', 'meat', 'chicken', 'egg']
finished_orders = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Preparing {current_sandwich} sandwich")
    finished_orders.append(current_sandwich)

print(f"\n--- Finished ---")
for order in finished_orders:
    print(f"\t{order.title()} sandwich")