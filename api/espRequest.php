<?php
    $params = json_decode(file_get_contents('php://input'), true);
    $param1 = $params['exp'];
    $param2 = $params['sensor'];
    if($param1 == 'fis1' && $param2 == 'temperature' ){
        $espUrl='http://192.168.30.21';
        $sensor=$param2;
        $url = $espUrl.'/'.$sensor;
        $curl = curl_init();
        curl_setopt_array($curl, [
            CURLOPT_RETURNTRANSFER => 1,
            CURLOPT_URL => $url
        ]);
        $response = curl_exec($curl);
        curl_close($curl);
        echo $response;
    }
    
?>