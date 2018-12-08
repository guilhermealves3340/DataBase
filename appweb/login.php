<?php
    include_once 'DataBase.php';
    $objDb = new DataBase();
    $link = $objDb->conecta_mysql();

    $email = htmlspecialchars(addslashes($_POST['email']));
    $senha = htmlspecialchars(addslashes($_POST['senha']));

    $sql = "SELECT * FROM tb_usuarios WHERE email = '$email' AND senha = '$senha' ";
    $resultado_sql = mysqli_query($link, $sql);

    if(mysqli_affected_rows($link)){
        $dados_usuario = mysqli_fetch_array($resultado_sql);
    
        if(isset($dados_usuario['id'])){
            $_SESSION['id_usuario'] = $dados_usuario['id_usuario'];
            header('Location: admin/index.php');
        }
    }

    else {
        header('Location: index.php?erro_usuario=1');
    }

    mysqli_close($link);
?>
