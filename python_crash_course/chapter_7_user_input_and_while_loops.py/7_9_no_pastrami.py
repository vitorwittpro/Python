sandwich_orders = ['cheese', 'pastrami', 'meat', 'chicken', 'pastrami', 'egg', 'pastrami']
finished_orders = []

print("\nRun out of pastrami\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Preparing {current_sandwich} sandwich")
    finished_orders.append(current_sandwich)

print(f"\n--- Finished ---")
for order in finished_orders:
    print(f"\t{order.title()} sandwich")