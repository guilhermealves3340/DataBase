<?php
    $erroUsuario = isset($_GET['erro_usuario']) ? $_GET['erro_usuario'] : 0;
?>

<!DOCTYPE html>
<html lang="pt-br" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Tesla</title>
        <link rel="icon" type="image/png" href="img/logo.png">
        <link rel="stylesheet" href="font-awesome-4.7.0/css/font-awesome.min.css">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <link rel="stylesheet" href="css/style.css">
    </head>
    <body>
        <div class="container">
            <div class="row justify-content-center">
                <div class="card py-4" style="width: 25rem;">
                    <div class="row justify-content-center">
                        <div class="col-md-4">
                            <img src="img/logo.png" class="img-fluid" width="100%" alt="Responsive image">
                        </div>
                    </div>
                    <div class="card-body">

                        <form method="POST" action="login.php" class="">
                            <div class="form-group">
                                <div class="row justify-content-center">
                                    <div class="col-md-12">
                                        <div class="form-group left-inner-addon">
                                            <i class="fa fa-envelope" aria-hidden="true"></i>
                                            <input type="email" class="form-control" name="email"  <?php if($erroUsuario == 1) echo "style='border-color: red;'"; ?> required placeholder="E-mail">
                                        </div>
                                    </div>

                                    <div class="col-md-12">
                                        <div class="form-group left-inner-addon">
                                            <i class="fa fa-unlock-alt" aria-hidden="true"></i>
                                            <input type="password" class="form-control" name="senha"   <?php if($erroUsuario == 1) echo "style='border-color: red;'"; ?> required placeholder="Senha">
                                        </div>
                                    </div>
                                </div>

                                <div class="col-md-12 text-center">
                                    <?php
                                    if($erroUsuario == 1){
                                        echo '<font color="#FF0000">E-mail e ou senha inválido(s)</font>';
                                        echo "<script>$('#myModal2').modal('show');</script>";
                                    }
                                    ?>
                                </div>

                            </div>

                            <div class="col-md-12 text-center">
                                <button type="submit" class="btn btn-success"><i class="fa fa-sign-in" aria-hidden="true"></i> Entrar</button>
                            </div>
                        </form>


                    </div>
                </div>
            </div>
        </div>
    </body>
</html>
