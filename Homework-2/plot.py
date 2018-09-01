import matplotlib.pyplot as plt
import pandas as pd
from help_function import read_the_file
from statistics import get_list_of_languages


if __name__ == '__main__':
    languages = read_the_file('Languages.json')
    data = read_the_file('NewData.json')
    languages = get_list_of_languages(languages, data)
    average_payment=[]
    new_languages=[]
    for objects in languages:
        average_payment.append(int(objects['payment_from'] / objects['vacancies']))
        new_languages.append(objects['language'])
    
    table = pd.DataFrame({'language':pd.Series(average_payment),
                           'salary':pd.Series(new_languages),
                         })
    
    table.plot(x='salary', y='language', kind='bar')
    plt.xlabel('Языки программирования')
    plt.ylabel('Средняя зарплата')
    plt.title('Статистика cредней зарплаты по различным языкам программирования в Москве')
    plt.show()
