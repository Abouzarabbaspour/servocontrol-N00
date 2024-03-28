import json

angle_values = {
    'open': 0,
    'close': -180
}
# read values from json file
with open('values.json') as f:
    data = json.load(f)
    angle_values['open'] = data['open']
    angle_values['close'] = data['close']
    print(angle_values)