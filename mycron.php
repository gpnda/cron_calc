<?php

class RES {
    public $value = 0;
    public $bump_order = false;
}

function increment($x, $max) {
    $result = new RES();
    $result->value = $x + 1;
    if ($result->value == $max) {
        $result->value = 0;
        $result->bump_order = true;
    }
    return $result;
}

function is_match($filter, $current) {
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

function next_match($filter, $current, $maxvalue) {
    $tmp_bump_order = false;
    $tmp_res = new RES();

    if ($filter == "*" || $filter == false) {
        $tmp_res = increment($current, $maxvalue);
        if ($tmp_res->bump_order) {
            $tmp_bump_order = true;
        }
    } elseif (preg_match("/\/\d+/", $filter)) {
        $divider = intval(preg_replace("/\/(\d+)/", "$1", $filter));
        $tmp_res = increment($current, $maxvalue);
        $x = $tmp_res->value;
        while ($tmp_res->value % $divider != 0) {
            $tmp_res = increment($x, $maxvalue);
            if ($tmp_res->bump_order) {
                $tmp_bump_order = true;
            }
            $x = $tmp_res->value;
        }
    } elseif (preg_match("/\d+(?:,\d+)+/", $filter)) {
        $str_arr = preg_replace("/\d+(,\d+)+/", "$0", $filter);
        $arr = explode(",", $str_arr);
        $arr = array_map('intval', $arr);

        $tmp_res = increment($current, $maxvalue);
        $x = $tmp_res->value;
        while (!in_array($tmp_res->value, $arr)) {
            $tmp_res = increment($x, $maxvalue);
            if ($tmp_res->bump_order) {
                $tmp_bump_order = true;
            }
            $x = $tmp_res->value;
        }
    } elseif (preg_match("/(\d+)-(\d+)/", $filter)) {
        $fromint = intval(preg_replace("/(\d+)-(\d+)/", "$1", $filter));
        $toint = intval(preg_replace("/(\d+)-(\d+)/", "$2", $filter));

        $tmp_res = increment($current, $maxvalue);
        $x = $tmp_res->value;
        while (!($tmp_res->value >= $fromint && $tmp_res->value <= $toint)) {
            $tmp_res = increment($x, $maxvalue);
            if ($tmp_res->bump_order) {
                $tmp_bump_order = true;
            }
            $x = $tmp_res->value;
        }
    }

    $tmp_res->bump_order = $tmp_bump_order;
    return $tmp_res;
}

class MYCRON {

    public $second = 15;
    public $minute = 30;
    public $hour = 17;
    public $day = 27;
    public $month = 11;
    public $year = 2024;

    public function start_calc() {
        global $second_filter, $minute_filter, $hour_filter, $day_filter, $month_filter, $year_filter;

        // if (!is_match($second_filter, $this->second)) {
        //     $this->get_next_second();
        // }
        if (!is_match($minute_filter, $this->minute)) {
            $this->get_next_minute();
        }
        if (!is_match($hour_filter, $this->hour)) {
            $this->get_next_hour();
        }
        if (!is_match($day_filter, $this->day)) {
            $this->get_next_day();
        }
        if (!is_match($month_filter, $this->month)) {
            $this->get_next_month();
        }
        if (!is_match($year_filter, $this->year)) {
            $this->get_next_year();
        }
    }

    public function get_next_second() {
        global $second_filter;
        $tmp_res = next_match($second_filter, $this->second, 60);
        $this->second = $tmp_res->value;
        if ($tmp_res->bump_order) {
            $this->get_next_minute();
        }
    }

    public function get_next_minute() {
        global $minute_filter;
        $tmp_res = next_match($minute_filter, $this->minute, 60);
        $this->minute = $tmp_res->value;
        if ($tmp_res->bump_order) {
            $this->get_next_hour();
        }
    }

    public function get_next_hour() {
        global $hour_filter;
        $tmp_res = next_match($hour_filter, $this->hour, 24);
        $this->hour = $tmp_res->value;
        if ($tmp_res->bump_order) {
            $this->get_next_day();
        }
    }

    public function get_next_day() {
        global $day_filter;
        $tmp_res = next_match($day_filter, $this->day, 30);
        $this->day = $tmp_res->value;
        if ($tmp_res->bump_order) {
            $this->get_next_month();
        }
    }

    public function get_next_month() {
        global $month_filter;
        $tmp_res = next_match($month_filter, $this->month, 12);
        $this->month = $tmp_res->value;
        if ($tmp_res->bump_order) {
            $this->get_next_year();
        }
    }

    public function get_next_year() {
        global $year_filter;
        $tmp_res = next_match($year_filter, $this->year, 10000);
        $this->year = $tmp_res->value;
    }
}








echo "Start1\n";

$now_second = 15;
$now_minute = 30;
$now_hour = 17;
$now_day = 27;
$now_month = 11;
$now_year = 2024;

$second_filter = "1-5";
$minute_filter = "/7";
$hour_filter = "/5";
$day_filter = "9-18";
$month_filter = "9-18";
$year_filter = "9-18";

$mc = new MYCRON();
$mc->start_calc();
while (true) {
    $mc->get_next_second();
    echo $mc->hour . ":" . $mc->minute . ":" . $mc->second . "\n";
}

?>
