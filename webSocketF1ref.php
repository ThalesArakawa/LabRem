<?php
declare(strict_types=1);
header('Content-Type: text/event-stream');

while (true) {
    $number = rand(1, 100);
    echo "event: number\n";
    echo "data: ".$number;
    echo "\n\n";
    //flush();
    sleep(1);
}

