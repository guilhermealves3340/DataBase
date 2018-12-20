<?php
    include_once 'DataBase.php';
    $link = conecta_banco();

    $email = htmlspecialchars(addslashes($_POST['email']));
    $senha = htmlspecialchars(addslashes($_POST['senha']));

    $sql = "SELECT * FROM proj.tb_login WHERE login = '$email' AND password = '$senha'; ";
    $resultSQL = pg_query($link, $sql);

    if(pg_affected_rows($resultSQL)){
        $dadosUsuario = pg_fetch_array($resultSQL);
        if(isset($dadosUsuario['userid'])){
            $_SESSION['userid'] = $dadosUsuario['userid'];
            header('Location: admin/');
        }
    }
    else {
        header('Location: index.php?erro=1');
    }
?>
