<?php
    echo '<!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8">
        <title>Example</title>
      </head>
      <body>
        <h1>Example</h1>
        <button onclick="loadHelloWorld()">Load Hello World</button>
        <script>
          function loadHelloWorld() {
            fetch("apiEsp/espRequest.php")
              .then(response => response.text())
              .then(data => {
                teste=data;
                console.log(teste);
              })
              .catch(error => console.error(error));
          }
        </script>
      </body>
    </html>'
?>