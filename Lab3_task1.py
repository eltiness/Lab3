# TODO Напишите функцию для поиска индекса товара
def searching(list):
    index = 0
    item = items_list[0]
    for item in items_list:
         if find_item==item:
           index=list.index (item)
           return index
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = searching(items_list)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
