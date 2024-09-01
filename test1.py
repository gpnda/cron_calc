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
        # filter = "*"
        tmp_res = increment(current , maxvalue)
        if tmp_res.bump_order:
            tmp_bump_order = True

    elif re.match("\/\d+", filter) is not None:
        # filter = "/3"
        divider = int(re.search("\/(\d+)", filter).group(1))
        tmp_res = increment(current , maxvalue)
        x = tmp_res.value
        while tmp_res.value % divider != 0:
            tmp_res = increment(x , maxvalue)
            if tmp_res.bump_order:
                tmp_bump_order = True
            x = tmp_res.value
    
    elif re.match("\d+(?:,\d+)+", filter) is not None:
        # filter == "5,10,15"
        str_arr = re.search("\d+(,\d+)+", filter).group(0)
        arr = str_arr.split(",")
        for i in range(0, len(arr)):
            arr[i] = int(arr[i])
        
        tmp_res = increment(current , maxvalue)
        x = tmp_res.value
        while not(tmp_res.value in arr):
            tmp_res = increment(x , maxvalue)
            if tmp_res.bump_order:
                tmp_bump_order = True
            x = tmp_res.value
    
    elif re.match("(\d+)-(\d+)", filter) is not None:
        # filter == "9-18":
        fromint = int(re.search("(\d+)-(\d+)", filter).group(1))
        toint = int(re.search("(\d+)-(\d+)", filter).group(2))
        print("=================")
        print(fromint)
        print(toint)

        tmp_res = increment(current , maxvalue)
        x = tmp_res.value
        while not((tmp_res.value >= fromint) and (tmp_res.value <= toint)):
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
        self.day = tmp_res.value
        if tmp_res.bump_order:
            self.get_next_month()
    
    def get_next_month(self):
        tmp_res = next_match(hour_filter, self.hour, 12)
        self.month = tmp_res.value
        if tmp_res.bump_order:
            self.get_next_year()
    
    def get_next_year(self):
        tmp_res = next_match(hour_filter, self.hour, 10000)
        self.year = tmp_res.value
        



print("Start")

now_second = 15
now_minute = 10
now_hour = 21
now_day = 27
now_month = 11
now_year = 2024

second_filter = "1-5"
minute_filter = "/7"
hour_filter = "/5"
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
# 9. текущая реализация доверяет тому, что текущий час - валидный, проходит фильтр, иначе он бы перешагнул его. 
#    По всей видимости надо будет ввести подгонку годов, месяцев, дней, часов, и т.д. под филтры, 
#    и именно в таком порядке - сначала года и далее вниз.



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



# ######################################################################################
# # Постановка задачи
# ######################################################################################

# Задача состоит в том, что бы сделать функцию, которая по заданным критериям определяет ближайшую 
# точку в будущем, соответствующую этим критериям.
# Критерии представляют из себя массив временных параметров, таких как секунды, минуты, часы, 
# дни, месяцы и годы.
# Любой из этих параметров может быть задан так:
# - символ * означает, что значение может быть любым
# - если параметр не задан, считается, что он задан *
# - диапазон двух чисел 5-10, значит подходят числа от и до включая оба значения
# - перечисление через запятую 1,3,5
# - остаток от деления 0/2 - подходят все числа, которые при делении на 2 дают 0 в остатке. Т.е. это
#  все четные числа. Если первое число 0, то его можно опустить и будет просто /5 - это значит 0,5,10...

# Параметры задаются в виде такого массива
# [
# 	"sec" => "*",		// Любое число секунд
# 	"min" => "/10",		// Число минут кратное 10
# 	"hour" => "9-18",	// Час от 9 до 18 включительно
# 	"day" => "*",		// День любой
# 	"mon" => "*",		// Месяц любой
# 	"year" => "*"		// Год любой
# ]
# Альтернативный способ - числовой массив, в котором параметры расположены в таком порядке 
# [секунды,минуты,часы,дни,месяцы,годы]
# Если параметров меньше 6 то считается, что пропущены последние. Например, [0,10,"*",1] означает, 
# что секунды заданы как 0, минуты как 10, часы как *, дни как 1, месяцы и годы не заданы, т.е. *

# Реализацию нужно поместить в класс CronTimer, основная функция должна быть статической и называться 
# nextTime. Принимает два параметра. Первый обязательный - это массив с параметрами, второй 
# необязательный - это строка с датой-временем, которая считается текущей, в формате "дд.мм.гггг чч:мм:сс". 
# Если второй параметр не передан, то считаем от реального текущего времени.
# В классе могут быть любые другие вспомогательные функции.
# Функция должна возвращать подходящую дату-время в виде строки в формате "дд.мм.гггг чч:мм:сс" или 
# false, если подходящее время недостижимо.

# Примеры вызова функции и возвращаемого результата.
# CronTimer::nextTime([], "01.01.2024 10:00:00") == "01.01.2024 10:00:01"
# CronTimer::nextTime(["sec"=>15], "01.01.2024 10:00:00") == "01.01.2024 10:00:15"
# CronTimer::nextTime(["min"=>"5/10"], "01.01.2024 10:00:00") == "01.01.2024 10:05:00"
# CronTimer::nextTime(["year"=>2023], "01.01.2024 10:00:00") === false

# Задача считается выполненной, если
# - при любых корректных входящих параметрах выдает правильный результат
# - вычисления в пределах 1 года не должны занимать более 1 секунды
# - это должен быть ваш код, а не готовая библиотека

# После того, как задача сдана на проверку, если в ней будут обнаружены ошибки, вам будет предложено их 
# исправить. До трех раз (т.е. на третий раз задача должна работать без ошибок). Если после этого в задаче 
# все еще обнаруживаются ошибки (т.е. она не соответствует хотя бы одному из критериев), считается, что вы 
# не способны довести свой код до рабочего состояния.

# Порядок работы
# 1) Вы изучаете задачу и решаете можете ли вы ее выполнить и готовы ли взяться за выполнение
# 2) Оцениваете стоимость ее выполнения в рублях и приблизительные сроки
# 3) Если оценки нас устраивают, вы приступаете к выполнению
# 4) После выполнения вы сдаете задачу. Если в ней обнаруживаются ошибки - она возвращается вам для их 
# исправления
# 5) Если ошибок нет, задача считается выполненной и оплачивается

# Комментарий к тестовому: вычисления в пределах 1 года не должны занимать более 1 секунды 
# вот тут, что имеется ввиду дистанция 1 год. 365 календарных дней от исходной точки.



# ######################################################################################

# Сначала буду делать суть, потом подгонять к условиям задачи.
# 