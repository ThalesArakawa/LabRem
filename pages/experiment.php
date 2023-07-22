<?php
    echo '<main class="content">
    <script src="./js/sketch.js"></script>
    <script src="./js/cenario.js"></script>
    <script src="./js/papaparse.min.js"></script>
    <section class="experimentTitle">
        <div>
            <h1 id="experimentTitle" class="experimentTitle">Experimento | Plano Inclinado</h1>
        </div>
    </section>
    <section id="experimentDiv" class="experimentDiv">
        <div id="simulation" class="simulation"></div>
        <div id="chart-distance" class="highcharts-figure"></div>
    </section>
    <section class="interactions">
        <button class="expButton" id="start">Iniciar</button>
        <button class="expButton" id="export">Exportar Dados</button>
        <button class="expButton" id="backToLab" onclick='.'window.location.href="?page=module1";'.'>Voltar</button>
    </section>
</main>';
?>