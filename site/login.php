<?php
       $username = $_POST['username'];
       $password = $_POST['password'];

       require 'postgresqlphpconnect/vendor/autoload.php';
       use PostgreSQL\Connection as Connection;
       use PostgreSQL\Select as Selection;

      try{
        $pdo =  Connection::get()->connect();
        $select = New Selection($pdo);
        $tipo = $select -> verificalogin($username,$password);
        echo  $tipo -> tipo_acesso;
    }
    catch (\PDOException $e) {
    echo $e->getMessage();
}
//$id =  $insert -> criaFuncionario('pablo','nunes','13123114279','1434512341','06041996','solteiro','laguna','155','r12','erqrq','dui','38400296','mG','1612942');


?>
