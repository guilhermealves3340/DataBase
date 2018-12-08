<!DOCTYPE html>
<html lang="pt_BR">
    <head>
        <link rel="icon" type="image/png" href="../img/logo.png">
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
                                    Lista de Funcionários
                                </div>
                            </div><br>

                            <div class="tile-body">
                                <table class="table table-hover table-bordered" id="sampleTable">
                                    <thead>
                                        <tr>
                                            <th>Nome</th>
                                            <th>Sobrenome</th>
                                            <th>CPF</th>
                                            <th>Ação</th>
                                        </tr>
                                    </thead>
                                    <tbody>


                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>


            <script src="../js/jquery-3.2.1.min.js"></script>
        </main>

        <?php include 'rodape.php'; ?>
    </body>
</html>
