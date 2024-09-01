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




def next_match_minute(filter, now_minute):

    tmp_bump_order = False
    tmp_res = RES()
    
    if filter == "*" or filter == False:
        # Здесь и в аналогичных местах - предполагаем валидность фильтра.
        tmp_res = increment(now_minute , 60)
        if tmp_res.bump_order:
            tmp_bump_order = True

    elif filter == "/3":
        # Здесь и в аналогичных местах - предполагаем валидность фильтра.
        tmp_res = increment(now_minute , 60)
        x = tmp_res.value
        while tmp_res.value % 3 != 0:
            tmp_res = increment(x , 60)
            if tmp_res.bump_order:
                tmp_bump_order = True
            x = tmp_res.value
    
    elif filter == "1,10,15":
        # Здесь и в аналогичных местах - предполагаем валидность фильтра.
        tmp_res = increment(now_minute , 60)
        x = tmp_res.value
        while not(tmp_res.value in [1,10,15]):
            tmp_res = increment(x , 60)
            if tmp_res.bump_order:
                tmp_bump_order = True
            x = tmp_res.value
    
    elif filter == "9-18":
        # Здесь и в аналогичных местах - предполагаем валидность фильтра.
        tmp_res = increment(now_minute , 60)
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



# 0. Удостовериться, что комбинация фильтров верная, валидная и реальная дата существует
#     На самом деле пока непонятно как удостовериться.


now_second = 15
now_minute = 10
now_hour = 21
now_day = 27
now_month = 11
now_year = 2024

second_filter = "9-18"
minute_filter = "*"
hour_filter = "9-18"
day_filter = "9-18"
month_filter = "9-18"
year_filter = "9-18"




bump_minutes = False
bump_hours = False





def get_next_second(now_arr):
    tmp_res = next_match_second(second_filter, now_arr["now_second"])
    if tmp_res.bump_order:
        get_next_minute()

    
def get_next_minute():
    pass

def get_next_hour():
    pass




while not bump_hours:
    while not bump_minutes:
        tmp_res = next_match_second(second_filter, now_second)
        if tmp_res.bump_order:
            bump_minutes = True
        print(str(now_minute) + " ------ " + str(now_second))
    
    tmp_res2 = next_match_minute(minute_filter, now_minute)
    if tmp_res2.bump_order:
        bump_hours = True








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





    # 2. Получить следующей доступное значеное минут next_match_minute(), согласно фильтру, начиная от now_minutes
    #     Если происходит bump_order, то now_hours увеличиваем на 1
    


    # 3. Получить следующей доступное значеное часа
    # 4. Получить следующей доступное значеное дня
    # 5. Получить следующей доступное значеное месяца
    # 6. Получить следующей доступное значеное года
    # 7. Сформировать дату из получившихся значений
    # 8. Если дата является валидной, то break и вот он окончательный ответ, 
    #     если дата не является валидной, то собственно тоже непонятно чт0 делать в этом случае, 
    #     нужен новый запуск, но не с теми-же входными данными, а собственно что должно измениться?

    







# # Вывод на экран
# y=0
# x=47
# while True:
#     tmp_res = next_match_second("9-18", x)
#     x = tmp_res.value
#     if tmp_res.bump_order:
#         y=y+1
#     print(str(y) + " ------ " + str(x))




