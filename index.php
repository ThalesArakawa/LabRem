<?php
    //header("Access-Control-Allow-Origin: *");
    //header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
    //header("Access-Control-Allow-Headers: Content-Type");
    $pages=['landpage'=>'pages/landpage.php','home'=>'pages/home.php','lab'=>'pages/lab.php','module1'=>'pages/module1.php','experiment'=>'pages/experiment.php','teste'=>'js/teste.php'];
    $css=['landpage'=>'landpage.css','home'=>'home.css','lab'=>'lab.css','module1'=>'module1.css','experiment'=>'experiment.css'];
    $js=['landpage'=>'','home'=>'','lab'=>'','module1'=>'','experiment'=>'experimentf1.js'];
    if(isset($_GET['page'])){
        if(isset($pages[$_GET['page']])){
            $page=$_GET['page'];
        }
        else{
            $page='landpage';
        }
    }
    else{
        $page='landpage';
    }
    echo '<!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="description" content="Laboratório para todos">
            <link rel="stylesheet" type="text/css" href="./css/'.$css[$page].'">
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.1/p5.js"></script>
            <title>LaBReM</title>
        </head>
        <body>';

        if($page != 'landpage'){
            echo '<header class="header">
            <section class="logoHeader">
                <img class="logoHeaderIcon" src="img/lab.png" alt="logoLaBReM">
                <div class="logoText">
                    <h1 class="logo-title">lABREM</h1>
                    <h2 class="logo-subTitle">LABORATÓRIO REMOTO</h2>
                </div>
            </section>
            <nav class="mainMenu">
                <a class="mainMenuOption" href="?page=home">Página Inicial</a>
                <a class="mainMenuOption" href="?page=lab">Laboratório</a>
                <a class="mainMenuOption" href="?page=about">Sobre</a>
            </nav>
        </header>';
        }

        

        require($pages[$page]);
        require('pages/footer.php');


echo    '<script src="./js/'.$js[$page].'"></script></body></html>'
        
        
?>
