<?php
require "mycron2.php";

$start_date = "15.01.2024 01:02:03";

$filter = [
    "sec" => "3",		// Любое число секунд
    "min" => "/5",	// Число минут кратное 10
    "hour" => "/10",	// Час от 9 до 18 включительно
    "day" => "*",		// День любой
    "mon" => "*",		// Месяц любой
    "year" => "*"		// Год любой
];

// Здесь выводим искомое значение
$t= $start_date;
for ($i=0;$i<20;$i++) {
    $t=CronTimer::nextTime($filter, $t);
    print ($t . "\n");
}


