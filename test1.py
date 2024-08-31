import re
print("Start")

class RES:
    def __init__(self):
        self.value = 0
        self.bump_order = False

def increment(x , max):
    result = RES()
    result.value = x + 1
    if result.value == max:
        result.value=0
        result.bump_order = True
    return result

def next_match_second(filter, now_second):

    tmp_bump_order = False
    tmp_res = RES()
    
    if filter == "*" or filter == False:
        # Здесь и в аналогичных местах - предполагаем валидность фильтра.
        tmp_res = increment(now_second , 60)
        if tmp_res.bump_order:
            tmp_bump_order = True

    elif filter == "/3":
        # Здесь и в аналогичных местах - предполагаем валидность фильтра.
        tmp_res = increment(now_second , 60)
        x = tmp_res.value
        while tmp_res.value % 3 != 0:
            tmp_res = increment(x , 60)
            if tmp_res.bump_order:
                tmp_bump_order = True
            x = tmp_res.value
    
    elif filter == "1,10,15":
        # Здесь и в аналогичных местах - предполагаем валидность фильтра.
        tmp_res = increment(now_second , 60)
        x = tmp_res.value
        while not(tmp_res.value in [1,10,15]):
            tmp_res = increment(x , 60)
            if tmp_res.bump_order:
                tmp_bump_order = True
            x = tmp_res.value
    
    elif filter == "9-18":
        # Здесь и в аналогичных местах - предполагаем валидность фильтра.
        tmp_res = increment(now_second , 60)
        x = tmp_res.value
        while not((tmp_res.value >= 9) and (tmp_res.value <= 18)):
            tmp_res = increment(x , 60)
            if tmp_res.bump_order:
                tmp_bump_order = True
            x = tmp_res.value

    tmp_res.bump_order = tmp_bump_order
    return tmp_res


# def next_match_minute(filter, now_minutes):
# def next_match_hour(filter, now_hours):
# def next_match_day(filter, now_day):
# def next_match_month(filter, now_month):
# def next_match_year(filter, now_year):



0. Удостовериться, что комбинация фильтров верная, валидная и реальная дата существует
    На самом деле пока непонятно как удостовериться.

while True:
    1. Получить следующей доступное значеное секунд next_match_second(), согласно фильтру, начиная от now_seconds
        Если происходит bump_order, то now_minutes увеличиваем на 1
        Е

    2. Получить следующей доступное значеное минут next_match_minute(), согласно фильтру, начиная от now_minutes
        Если происходит bump_order, то now_hours увеличиваем на 1

    3. Получить следующей доступное значеное часа
    4. Получить следующей доступное значеное дня
    5. Получить следующей доступное значеное месяца
    6. Получить следующей доступное значеное года
    7. Сформировать дату из получившихся значений
    8. Если дата является валидной, то break и вот он окончательный ответ, 
        если дата не является валидной, то собственно тоже непонятно чт0 делать в этом случае, 
        нужен новый запуск, но не с теми-же входными данными, а собственно что должно измениться?







# Вывод на экран
y=0
x=47
while True:
    tmp_res = next_match_second("9-18", x)
    x = tmp_res.value
    if tmp_res.bump_order:
        y=y+1
    print(str(y) + " ------ " + str(x))




