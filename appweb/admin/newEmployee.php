<?php
    require_once('../DataBase.php');
    $objDb = new DataBase();
    $link = $objDb->conecta_mysql();

    $sqlArea = "SELECT * FROM tb_area_conhecimento;";
    $resultSQLArea = mysqli_query($link, $sqlArea);
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
                                    Cadastrar Novo Curso
                                </div>
                            </div><br>

                            <form action="#">
                                <div class="form-group">
                                    <label>Nome do Curso:</label>
                                    <input type="text" class="form-control" name="nomeCurso">
                                </div>

                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label>Carga Horária:</label>
                                            <input type="text" class="form-control" name="cargaHoraria">
                                        </div>

                                        <div class="col-md-6">
                                            <label>Valor do Curso:</label>
                                            <input type="text" class="form-control" name="valor">
                                        </div>
                                    </div>
                                </div>

                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label>Vídeo de Apresentação:</label>
                                            <input type="file" name="videoApresentacao">
                                        </div>
                                        <div class="col-md-6">
                                            <label>Àrea do Conhecimento:</label>
                                            <select class="form-control" id="exampleFormControlSelect1">
                                                <?php
                                                    while($rows = mysqli_fetch_assoc($resultSQLArea)){
                                                ?>
                                                    <option value="<?php echo $rows['id_area']; ?>"><?php echo $rows['nome']; ?></option>
                                                <?php
                                                    }
                                                ?>
                                            </select>
                                        </div>
                                    </div>
                                </div>


                                <div class="form-group">
                                    <div class="row">
                                        <div class="container text-center">
                                			<a class="btn btn-primary" href="javascript:void(0)" id="addInput">
                                				<span class="glyphicon glyphicon-plus" aria-hidden="true"></span>
                                				<i class="fa fa-plus" aria-hidden="true"></i> Adicionar Aula
                                			</a>
                                        </div>
                                    </div>
                                </div>


                    			<div id="dynamicDiv">

                    		    </div>

                                <span class="row justify-content-center">
                                    <button type="submit" class="btn btn-success">Cadastrar</button>
                                </span>
                            </form>

                        </div>
                    </div>
                </div>
            </div>
        </main>


        <script>
            $(function () {
                var scntDiv = $('#dynamicDiv');
                var cont = 1;
                $(document).on('click', '#addInput', function () {
                    $(

                        '<p>' +
                            '<div class="form-group" id="remInput">' +
                                '<div class="row">' +
                                    '<div class="container">' +
                                        '<div class="card">' +
                                            '<div class="card-header list-group-item active">' +
                                                'Aula ' + cont++ +

                                                '<span class="clo-md-6" style="float: right;">' +
                                                    '<a class="btn btn-danger"  href="javascript:void(0)">' +
                                                        '<i class="fa fa-times" aria-hidden="true"></i>' +
                                                    '</a>' +
                                                '</span>' +
                                            '</div>' +

                                            '<div class="card-body" style="background: #DCDCDC;">' +
                                                '<div class="form-group">' +
                                                    '<label>Título da Aula:</label>' +
                                                    '<input type="tituloSecao" class="form-control">' +
                                                '</div>' +
                                                '<div class="form-group">' +
                                                    '<label>Vídeo:</label>' +
                                                    '<input type="file" name="videoSecao">' +
                                                '</div>' +
                                            '</div>' +
                                        '</div>' +
                                    '</div>' +
                                '</div>' +
                            '</div>' +
                        '</p>'


                    ).appendTo(scntDiv);
                    return false;
                });
                $(document).on('click', '#remInput', function () {
                    $(this).appendTo(scntDiv).remove();
                    return false;
                });
            });
        </script>

        <?php include 'rodape.php'; ?>
    </body>
</html>
