import re


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


def next_match(filter, current, maxvalue):

    tmp_bump_order = False
    tmp_res = RES()
    
    if filter == "*" or filter == False:
        # Здесь и в аналогичных местах - предполагаем валидность фильтра.
        tmp_res = increment(current , maxvalue)
        if tmp_res.bump_order:
            tmp_bump_order = True

    elif filter == "/3":
        # Здесь и в аналогичных местах - предполагаем валидность фильтра.
        tmp_res = increment(current , maxvalue)
        x = tmp_res.value
        while tmp_res.value % 3 != 0:
            tmp_res = increment(x , maxvalue)
            if tmp_res.bump_order:
                tmp_bump_order = True
            x = tmp_res.value
    
    elif filter == "1,10,15":
        # Здесь и в аналогичных местах - предполагаем валидность фильтра.
        tmp_res = increment(current , maxvalue)
        x = tmp_res.value
        while not(tmp_res.value in [1,10,15]):
            tmp_res = increment(x , maxvalue)
            if tmp_res.bump_order:
                tmp_bump_order = True
            x = tmp_res.value
    
    elif filter == "9-18":
        # Здесь и в аналогичных местах - предполагаем валидность фильтра.
        tmp_res = increment(current , maxvalue)
        x = tmp_res.value
        while not((tmp_res.value >= 9) and (tmp_res.value <= 18)):
            tmp_res = increment(x , maxvalue)
            if tmp_res.bump_order:
                tmp_bump_order = True
            x = tmp_res.value

    tmp_res.bump_order = tmp_bump_order
    return tmp_res




class MYCRON:

    def __init__(self):
        self.second = 15
        self.minute = 10
        self.hour = 21
        self.day = 27
        self.month = 11
        self.year = 2024

    def get_next_second(self):
        tmp_res = next_match(second_filter, self.second, 60)
        self.second = tmp_res.value
        if tmp_res.bump_order:
            self.get_next_minute()

        
    def get_next_minute(self):
        tmp_res = next_match(minute_filter, self.minute, 60)
        self.minute = tmp_res.value
        if tmp_res.bump_order:
            self.get_next_hour()
        

    def get_next_hour(self):
        tmp_res = next_match(hour_filter, self.hour, 24)
        self.hour = tmp_res.value
        if tmp_res.bump_order:
            self.get_next_day()

    def get_next_day(self):
        tmp_res = next_match(hour_filter, self.hour, 30)
        self.hour = tmp_res.value
        if tmp_res.bump_order:
            self.get_next_month()
    
    def get_next_month(self):
        tmp_res = next_match(hour_filter, self.hour, 12)
        self.hour = tmp_res.value
        if tmp_res.bump_order:
            self.get_next_year()
    
    def get_next_year(self):
        tmp_res = next_match(hour_filter, self.hour, 10000)
        self.hour = tmp_res.value
        





print("Start")

now_second = 15
now_minute = 10
now_hour = 21
now_day = 27
now_month = 11
now_year = 2024

second_filter = "9-18"
minute_filter = "1,10,15"
hour_filter = "1,10,15"
day_filter = "9-18"
month_filter = "9-18"
year_filter = "9-18"


mc = MYCRON()
while True:
    mc.get_next_second()
    print(str(mc.hour) + ":" + str(mc.minute) + ":" + str(mc.second))









# ######################################################################################
# Что надо:
# ######################################################################################

# 1. Все упаковать в один класс
# 2. Продумать как обращаться к этому классу, ну наверное ожидается, что можно орбратиться к статичному методу, без инстанцирования
# 3. Раз нет инстанса, как обращаться к локальным переменным, нужна ведь оболасть видимости. Можно инстанцировать объект дочернего класса.
# 4. Объединить бы все методы get_next_**** в один, можно? да почему нет, отличаются только максимальным значением
# 5. Добавить регулярные выражения, чтобы парсить фильтры
# 6. Класс RES кудато бы спрятать чтоли, корявенько лежит
# 7. чтото надо порешать с исключениями, типа 28/29/30/31 день, и с високосными годами. Где это ловить?
# 8. Удостовериться, что комбинация фильтров верная, валидная и реальная дата существует. Пока непонятно как удостовериться.



# Это все лучше сделать одной функцией next_match()
# --------------------------------------------------------
# def next_match_second(filter, now_second): 60
# def next_match_minute(filter, now_minute): 60
# def next_match_hour(filter, now_hour): 24 
# def next_match_day(filter, now_day): 28, 29, 30, 31 ???
# def next_match_month(filter, now_month): 12
# def next_match_year(filter, now_year): 10 000



# ######################################################################################
# Через вложенные while не получилось, потому - видимо надо делать рекурсию.
# ######################################################################################

# while not bump_hours:
#     bump_minutes = False
#     tmp_res2 = next_match_minute(minute_filter, now_minute)
#     while not bump_minutes:
#         bump_minutes = False
#         tmp_res = next_match_second(second_filter, now_second)
#         if tmp_res.bump_order:
#             _tmp_res_ = increment(now_minute , 60)
#             now_minute = _tmp_res_.value
#             bump_minutes = True
#         print(str(now_minute) + " ------ " + str(now_second))


# while not bump_hours:
#     bump_minutes = False

#     while not bump_minutes:
#         print("second bumped")
#         tmp_res = next_match_second(second_filter, now_second)
#         if tmp_res.bump_order:
#             # _tmp_res_ = increment(now_minute , 60)
#             # now_minute = _tmp_res_.value
#             bump_minutes = True
#         else:
#             now_second = tmp_res.value
#             print(str(now_minute) + " ------ " + str(now_second))
    
#     print("minute bumped")
#     tmp_res2 = next_match_minute(minute_filter, now_minute)
#     now_minute = tmp_res2.value
#     if tmp_res2.bump_order:
#         print("hour bumped")
#         _tmp_res_ = increment(now_hour , 24)
#         now_hour = _tmp_res_.value
#         bump_hours = True



# ######################################################################################
# Какая должна быть последовательность?
# ######################################################################################

# 1. Получить следующей доступное значеное минут next_match_minute(), согласно фильтру, начиная от now_minutes
#     Если происходит bump_order, то now_hours увеличиваем на 1
# 3. Получить следующей доступное значеное часа
# 4. Получить следующей доступное значеное дня
# 5. Получить следующей доступное значеное месяца
# 6. Получить следующей доступное значеное года
# 7. Сформировать дату из получившихся значений
# 8. Если дата является валидной, то break и вот он окончательный ответ, 
#     если дата не является валидной, то собственно тоже непонятно чт0 делать в этом случае, 
#     нужен новый запуск, но не с теми-же входными данными, а собственно что должно измениться?



# ######################################################################################
# # отладочный вывод на экран
# ######################################################################################
# y=0
# x=47
# while True:
#     tmp_res = next_match_second("9-18", x)
#     x = tmp_res.value
#     if tmp_res.bump_order:
#         y=y+1
#     print(str(y) + " ------ " + str(x))




