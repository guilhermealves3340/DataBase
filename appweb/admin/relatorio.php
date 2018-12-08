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


                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </main>

        <?php include 'rodape.php'; ?>
    </body>
</html>
