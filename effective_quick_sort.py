# 89375451

"""
Тимофей решил организовать соревнование по спортивному программированию, чтобы найти талантливых стажёров.
Задачи подобраны, участники зарегистрированы, тесты написаны.
Осталось придумать, как в конце соревнования будет определяться победитель.

Каждый участник имеет уникальный логин. Когда соревнование закончится,
к нему будут привязаны два показателя: количество решённых задач Pi и размер штрафа Fi.
Штраф начисляется за неудачные попытки и время, затраченное на задачу.

Тимофей решил сортировать таблицу результатов следующим образом: при сравнении двух участников выше будет идти тот,
у которого решено больше задач. При равенстве числа решённых задач первым идёт участник с меньшим штрафом.
Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в алфавитном (лексикографическом) порядке.

Тимофей заказал толстовки для победителей и накануне поехал за ними в магазин.
В своё отсутствие он поручил вам реализовать алгоритм быстрой сортировки (англ. quick sort) для таблицы результатов.
Так как Тимофей любит спортивное программирование и не любит зря расходовать оперативную память,
то ваша реализация сортировки не может потреблять O(n) дополнительной памяти для промежуточных данных
(такая модификация быстрой сортировки называется "in-place").

Формат ввода
В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
В каждой из следующих n строк задана информация про одного из участников.
i-й участник описывается тремя параметрами:

- уникальным логином (строкой из маленьких латинских букв длиной не более 20)
- числом решённых задач Pi
- штрафом Fi
Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.
Формат вывода
Для отсортированного списка участников выведите по порядку их логины по одному в строке.
"""


def get_input():
    participants_number = int(input())
    participants_results = []

    for participant in range(participants_number):
        name, task, penalty = input().split()
        participants_results.append((name, int(task), int(penalty)))

    return participants_results


def swap(array, first_item, second_item):
    array[first_item], array[second_item] = array[second_item], array[first_item]


def is_higher(object_1, object_2):
    if object_1[1] == object_2[1] and object_1[2] == object_2[2]:
        return object_1[0].lower() < object_2[0].lower()
    elif object_1[1] == object_2[1]:
        return object_1[2] < object_2[2]
    return object_1[1] > object_2[1]


def quick_sort_interation(array, start, end):
    pivot = array[end]
    left = start
    right = end - 1
    while left < right:
        while (left < end) and (not is_higher(array[left], pivot)):
            left += 1
        while (right > start) and (is_higher(array[right], pivot)):
            right -= 1
        if left < right:
            swap(array, left, right)

    if is_higher(array[left], pivot):
        swap(array, left, end)

    return left


def effective_quick_sort(array, start, end):
    if start >= end:
        return
    partition = quick_sort_interation(array, start, end)
    effective_quick_sort(array, start, partition - 1)
    effective_quick_sort(array, partition + 1, end)


if __name__ == '__main__':
    inputs = get_input()
    effective_quick_sort(inputs, 0, len(inputs) - 1)
    inputs.reverse()

    print(*[participant[0] for participant in inputs], sep='\n')
