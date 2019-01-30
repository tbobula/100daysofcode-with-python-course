cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    jeeps = [car for car in cars['Jeep']]
    return ", ".join(jeeps)


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [model[0] for model in cars.values()]


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    mached_models = []
    for models in cars.values():
        for model in models:
            if grep.lower() in model.lower():
                mached_models.append(model)
    return mached_models


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    return { manufacture: sorted(models) for manufacture, models in cars.items() }

print(get_all_jeeps(cars))
print(get_first_model_each_manufacturer(cars))
print(get_all_matching_models(cars))
print(sort_car_models(cars))
