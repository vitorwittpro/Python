from printing_functions import print_process, print_completed 

unprinted = ['tomato', 'scream movie', 'scooby-doo']
completed = []

# copy unprinted_design
print_process(unprinted[:], completed_models=completed)
print_completed(completed_models=completed)

print(unprinted)