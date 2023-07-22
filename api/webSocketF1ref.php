<?php
//declare(strict_types=1);
header('Content-Type: text/event-stream');
header('Cache-Control: no-cache');

while (true) {
    $espUrl='http://192.168.30.21';
    $url = $espUrl.'/temperature';
    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_RETURNTRANSFER => 1,
        CURLOPT_URL => $url
    ]);
    $response = curl_exec($curl);
    $number = rand(1, 100);
    //echo "event: number\n";
    echo "data: ".((int) curl_exec($curl))."\n\n";
    flush();
    sleep(1);
}

?>

