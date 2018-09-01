from help_function import read_the_file, record_to_file

def rewrite_data(data):
    new_data = []
    for objects in data:
        new_dict = {
        'profession' : objects['profession'],
        'payment_from' : objects['payment_from'],
        'payment_to' : objects['payment_to'],        
        'candidat' : objects['candidat']
        }
        new_data.append(new_dict)
    return new_data

if __name__ == '__main__':
    data = read_the_file('Data.json')
    data = rewrite_data(data)
    record_to_file(data, 'NewData.json')
