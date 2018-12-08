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
                                    Cadastrar Novo Funcionário
                                </div>
                            </div><br>

                            <form action="#">
                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label>Nome:</label>
                                            <input type="text" class="form-control" name="nome">
                                        </div>

                                        <div class="col-md-6">
                                            <label>Sobrenome:</label>
                                            <input type="text" class="form-control" name="sobrenome">
                                        </div>
                                    </div>
                                </div>

                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label>CPF:</label>
                                            <input type="text" class="form-control" name="cpf">
                                        </div>

                                        <div class="col-md-6">
                                            <label>RG:</label>
                                            <input type="text" class="form-control" name="rg">
                                        </div>
                                    </div>
                                </div>

                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label>Data de Nascimento:</label>
                                            <input type="text" class="form-control" name="dataNascimento">
                                        </div>

                                        <div class="col-md-6">
                                            <label>Estado Civil:</label>
                                            <input type="text" class="form-control" name="estadoCivil">
                                        </div>
                                    </div>
                                </div>

                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label>CEP:</label>
                                            <input type="text" class="form-control" name="cep">
                                        </div>

                                        <div class="col-md-6">
                                            <label>Rua:</label>
                                            <input type="text" class="form-control" name="rua">
                                        </div>
                                    </div>
                                </div>

                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label>Número:</label>
                                            <input type="text" class="form-control" name="numero">
                                        </div>

                                        <div class="col-md-6">
                                            <label>Complemento:</label>
                                            <input type="text" class="form-control" name="complemento">
                                        </div>
                                    </div>
                                </div>

                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label>Bairro:</label>
                                            <input type="text" class="form-control" name="bairro">
                                        </div>

                                        <div class="col-md-6">
                                            <label>Cidade:</label>
                                            <input type="text" class="form-control" name="cidade">
                                        </div>
                                    </div>
                                </div>

                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label>Estado:</label>
                                            <input type="text" class="form-control" name="estado">
                                        </div>

                                        <div class="col-md-6">
                                            <label>ID Tag:</label>
                                            <input type="text" class="form-control" name="idTag">
                                        </div>
                                    </div>
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
