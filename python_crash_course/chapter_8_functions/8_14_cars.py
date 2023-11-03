def make_car(manufaturer, model, **car_info):
    car_info['manufactor'] = manufaturer
    car_info['model'] = model
    return car_info

car = make_car('Subaru', 'wrx', color='blue', tow_package=True)

print(car)