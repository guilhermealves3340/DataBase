<?php
    require_once('../DataBase.php');
    $objDb = new DataBase();
    $link = $objDb->conecta_mysql();
?>
<!DOCTYPE html>
<html lang="pt_BR">
    <head>
        <link rel="icon" type="image/png" href="../img/logo.png">
        <script src="../js/jquery-3.2.1.min.js"></script>
    </head>

    <body class="app sidebar-mini rtl">
        <?php include "menu.php"; ?>
        <main class="app-content">
            <div class="row d-flex justify-content-center">
                <div class="row col-md-12">
                    <div class="col-md-12">
                        <div class="tile">
                            <div class="row text-center">
                                <div class="col-md-12 h3">
                                    Relatório
                                </div>
                            </div><br>

                            <form action="#">

                              <div id="piechart"></div>

                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </main>

        <?php include 'rodape.php'; ?>
    </body>
</html>
<?php

$m = new MongoClient('mongodb://localhost', [
    'username' => 'abc',
    'password' => 'abc@123',
    'db'       => 'abc'
]);

$id = $_GET['_id']

$cursor = tela.horas.find({_id : $id})

$studentData = array();

foreach($cursor as $row){

   foreach($row->marks as $item){
    $result = array();

    $result ['nome'] = $item->nome;

    $result ['sobrenome']  = $item->sobrenome;

    $result ['cargaHoraria']     = $item->cargaHoraria;

    $result ['horas_compridas']     = $item->horas_compridas;

    $result ['salario']     = $item->salario;

    $funcData[] = $result;
  }

  }

  echo json_encode($funcData);

?>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

<script type="text/javascript">
// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {

  var data = google.visualization.arrayToDataTable([
  ['Task', 'Hours per Day'],
  ['Work', 8],
  ['Eat', 2],
  ['TV', 4],
  ['Gym', 2],
  ['Sleep', 8]
]);

  // Optional; add a title and set the width and height of the chart
  var options = {'title':'My Average Day', 'width':550, 'height':400};

  // Display the chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, options);
}


</script>
