from help_function import read_the_file

def get_list_of_languages(languages, data):
    list_of_languages = []
    for language in languages:
        is_language_in_object = False
        payment_of_vacancie = 0
        number_of_vacancie = 0    
        for objects in data:
            if objects['candidat'] and language in objects['candidat']:
                is_language_in_object = True
                payment_of_vacancie += (objects['payment_to'] + objects['payment_from']) / 2
                number_of_vacancie += 1
        if is_language_in_object:
            new_dict = {
                'language' : language,
                'payment_from' : payment_of_vacancie,
                'vacancies' : number_of_vacancie
            }
            list_of_languages.append(new_dict)
    return list_of_languages

def print_statistics(languages):
    for objects in languages:
        average_payment = str(int(objects['payment_from'] / objects['vacancies']))
        print('Язык:',objects['language'].ljust(12),end = '',sep = '')
        print('Cредняя заработная плата:',average_payment.ljust(8),end = '')
        print('Количество вакансий:',objects['vacancies'])

if __name__ == '__main__':
    languages = read_the_file('Languages.json')
    data = read_the_file('NewData.json')
    languages = get_list_of_languages(languages, data)
    print_statistics(languages)




