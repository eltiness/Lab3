# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first,participants_second,split_=","):
   list_words_one=participants_first.split(split_)
   list_words_two = participants_second.split(split_)
   list_words=list_words_one+list_words_two
   list_words = list(set(list_words))
   list_words.sort()
   return list_words
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
All = find_common_participants (participants_first_group,participants_second_group,)
print(All)

# TODO Провеьте работу функции с разделителем отличным от запятой

All = find_common_participants (participants_first_group,participants_second_group,"|")
print(All)