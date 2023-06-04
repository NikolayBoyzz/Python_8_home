# def search(book: str, info: str) -> str:
#    """Находит в списке записи по определенному критерию поиска"""
#    book = book.split('\n')
#    flag = False
#    res = []
#    for contact in book:
#        if info in contact:
#            res.append(contact)
#            res_str = '\n'.join(map(str,res))
#            flag = True

#    if flag == True:
#        print(res_str)
#        search2 = input("Введите уточнение для поиска")

#    else:
#        return 'Совпадений не найдено'

#def search(book: str, info: str) -> str:
#    """Находит в списке записи по определенному критерию поиска"""
#    book = book.split('\n')
#    for contact in book:
#        if info in contact:
#            return contact
#    return 'Совпадений не найдено'

#with open('book.txt', 'r', encoding='utf-8') as file:   
#        data = file.read()
#print (data)
#data_to_find = input ('Введите данные для поиска: ')
#print (data_to_find)