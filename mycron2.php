<?php

class RES {   // ********************************* От этого класса надо избавиться - все в ассоциативный массив
    public $value = 0;
    public $bump_order = false;
}

class MYCRON {

    private function increment($x, $max) {
        $result = new RES();
        $result->value = $x + 1;
        if ($result->value == $max) {
            $result->value = 0;
            $result->bump_order = true;
        }
        return $result;
    }

    private function is_match($filter, $current) {
        $result = false;

        if ($filter == "*" || $filter == false) {
            $result = true;
        } elseif (preg_match("/\/\d+/", $filter)) {
            $divider = intval(preg_replace("/\/(\d+)/", "$1", $filter));
            if ($current % $divider == 0) {
                $result = true;
            }

        } elseif (preg_match("/\d+(?:,\d+)+/", $filter)) {
            
            $str_arr = preg_replace("/\d+(,\d+)+/", "$0", $filter);
            $arr = explode(",", $str_arr);
            $arr = array_map('intval', $arr);
            if (in_array($current, $arr)) {
                $result = true;
            }
        } elseif (preg_match("/(\d+)-(\d+)/", $filter)) {
            $fromint = intval(preg_replace("/(\d+)-(\d+)/", "$1", $filter));
            $toint = intval(preg_replace("/(\d+)-(\d+)/", "$2", $filter));
            if ($current >= $fromint && $current <= $toint) {
                $result = true;
            }
        }

        return $result;
    }

    private function next_match($filter, $current, $maxvalue) {
        $tmp_bump_order = false;
        $tmp_res = new RES();

        if ($filter == "*") {
            $tmp_res = $this->increment($current, $maxvalue);
            if ($tmp_res->bump_order) {
                $tmp_bump_order = true;
            } 
        } elseif (preg_match("/\/\d+/", $filter)) {
            $divider = intval(preg_replace("/\/(\d+)/", "$1", $filter));
            $tmp_res = $this->increment($current, $maxvalue);
            $x = $tmp_res->value;
            while ($tmp_res->value % $divider != 0) {
                $tmp_res = $this->increment($x, $maxvalue);
                if ($tmp_res->bump_order) {
                    $tmp_bump_order = true;
                }
                $x = $tmp_res->value;
            }
        } elseif (preg_match("/\d+(?:,\d+)+/", $filter)) {
            $str_arr = preg_replace("/\d+(,\d+)+/", "$0", $filter);
            $arr = explode(",", $str_arr);
            $arr = array_map('intval', $arr);

            $tmp_res = $this->increment($current, $maxvalue);
            $x = $tmp_res->value;
            while (!in_array($tmp_res->value, $arr)) {
                $tmp_res = $this->increment($x, $maxvalue);
                if ($tmp_res->bump_order) {
                    $tmp_bump_order = true;
                }
                $x = $tmp_res->value;
            }
        } elseif (preg_match("/(\d+)-(\d+)/", $filter)) {
            $fromint = intval(preg_replace("/(\d+)-(\d+)/", "$1", $filter));
            $toint = intval(preg_replace("/(\d+)-(\d+)/", "$2", $filter));

            $tmp_res = $this->increment($current, $maxvalue);
            $x = $tmp_res->value;
            while (!($tmp_res->value >= $fromint && $tmp_res->value <= $toint)) {
                $tmp_res = $this->increment($x, $maxvalue);
                if ($tmp_res->bump_order) {
                    $tmp_bump_order = true;
                }
                $x = $tmp_res->value;
            }
        } elseif (preg_match("/\d+/", $filter)) { // ********************************** ТУТ надо проверить реализацию фильтра - одно значение
            $intvalue = intval(preg_replace("/(\d+)/", "$1", $filter));
            $tmp_res = $this->increment($current, $maxvalue);
            $x = $tmp_res->value;
            while ($tmp_res->value != $intvalue) {
                $tmp_res = $this->increment($x, $maxvalue);
                if ($tmp_res->bump_order) {
                    $tmp_bump_order = true;
                }
                $x = $tmp_res->value;
            }
        } 

        $tmp_res->bump_order = $tmp_bump_order;
        return $tmp_res;
    }

    public function start_calc() {
        
        // if (!$this::is_match($this->filter['sec'], $this->second)) {
        //     $this->get_next_second();
        // }
        if (!$this->is_match($this->filter['min'], $this->minute)) {
            $this->get_next_minute();
        }
        if (!$this->is_match($this->filter['hour'], $this->hour)) {
            $this->get_next_hour();
        }
        if (!$this->is_match($this->filter['day'], $this->day)) {
            $this->get_next_day();
        }
        if (!$this->is_match($this->filter['mon'], $this->month)) {
            $this->get_next_month();
        }
        if (!$this->is_match($this->filter['year'], $this->year)) {
            $this->get_next_year();
        }
    }

    public function get_next_second() {
        $tmp_res = $this->next_match($this->filter['sec'], $this->second, 60);
        $this->second = $tmp_res->value;
        if ($tmp_res->bump_order) {
            $this->get_next_minute();            
        }
    }

    public function get_next_minute() {
        $tmp_res = $this->next_match($this->filter['min'], $this->minute, 60);
        $this->minute = $tmp_res->value;
        if ($tmp_res->bump_order) {
            $this->get_next_hour();
        }
    }

    public function get_next_hour() {
        $tmp_res = $this->next_match($this->filter['hour'], $this->hour, 24);
        $this->hour = $tmp_res->value;
        if ($tmp_res->bump_order) {
            $this->get_next_day();
        }
    }

    public function get_next_day() {
        $tmp_res = $this->next_match($this->filter['day'], $this->day, 32);
        $this->day = $tmp_res->value;
        // Нулевых дней в месяце не бывает, в отличае от секунд, минут и часов
        if ($tmp_res->value == 0) {
            print ("Попытка сделать день НУЛЕМ");
            $tmp_res = $this->next_match($this->filter['day'], $this->day, 32);
            $tmp_res->bump_order = true;
        }
        if ($tmp_res->bump_order) {
            $this->get_next_month();
        }
    }

    public function get_next_month() {
        $tmp_res = $this->next_match($this->filter['mon'], $this->month, 12);
        $this->month = $tmp_res->value;
        if ($tmp_res->bump_order) {
            $this->get_next_year();
        }
    }

    public function get_next_year() {
        $tmp_res = $this->next_match($this->filter['year'], $this->year, 10000);
        $this->year = $tmp_res->value;
    }



    public function nextTime($filter, $currenttime) {


        // ************ Здесь эти переменные парсим из строковой перменной $currenttime **********************
        $this->second = 15;
        $this->minute = 30;
        $this->hour = 17;
        $this->day = 27;
        $this->month = 11;
        $this->year = 2024;

        // Это чтоб все не-указанные фильтры по умолчанию были '*'
        $this->filter = array_merge(
            [
            'sec'=>'*', 
            'min'=>'*', 
            'hour'=>'*', 
            'day'=>'*', 
            'mon'=>'*', 
            'year'=>'*' 
            ], 
            $filter
        );

        // Делаем сдвиг всех первых значений кроме секунды (чувствуется что криво, видимо сама эта логика содержит ошибку)
        $this->start_calc();

        // Основной запуск, он каскадом спустится от секунд до года.
        $this->get_next_second();
        $resultstr = $this->hour . ":" . $this->minute . ":" . $this->second . "   " . $this->day . "-" . $this->month . "-" . $this->year . "\n";
        
        // Дернем для проверки еще несколько раз, просто чтоб вывести на экран. Потом надо убрать **********************************
        echo $resultstr;
        for ($i=0;$i<20 ; $i++) {
            $this->get_next_second();
            echo $this->hour . ":" . $this->minute . ":" . $this->second . "   " . $this->day . "-" . $this->month . "-" . $this->year . "\n";
        }

        return $resultstr;
    }



}







// Декоратор
class CronTimer {
    public static function nextTime($filter, $currenttime) {
        return (new MYCRON())->nextTime($filter, $currenttime);
    }
}


$start_date = "01.01.2024 10:00:00";

$filter = [
    "sec" => "55",		// Любое число секунд
    "min" => "55",	// Число минут кратное 10
    "hour" => "/10",	// Час от 9 до 18 включительно
    "day" => "*",		// День любой
    "mon" => "*",		// Месяц любой
    "year" => "*"		// Год любой
];

// Здесь выводим искомое значение
echo CronTimer::nextTime($filter, $start_date);

?>
