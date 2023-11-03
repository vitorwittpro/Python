import time

def print_process(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model {current_design}...")
        completed_models.append(current_design)

        time.sleep(2)

def print_completed(completed_models):
    print("Printed all models.")
    for completed_model in completed_models:
        print(completed_model)