<?php
       $nome = $_POST['nome'];
       $sobreNome = $_POST['sobreNome'];
       $cpf = $_POST['cpf'];
       $rg = $_POST['rg'];
       $estadoCivil = $_POST['estadoCivil'];
       $dataNascimento = $_POST['dataNascimento'];
       $numResidencia = $_POST['numResidencia'];
       $bairro = $_POST['bairro'];
       $cidade = $_POST['cidade'];
       $complemento = $_POST['complemento'];
       $logradouro = $_POST['logradouro'];
       $cep = $_POST['cep'];
       $estado = $_POST['estado'];
       $admissao = $_POST['admissao'];
       $rfid = $_POST['rfid'];

       require 'postgresqlphpconnect/vendor/autoload.php';
       use PostgreSQL\Connection as Connection;
       use PostgreSQL\Insert as Insertion;
       $pdo =  Connection::get()->connect();
       $insert = New Insertion($pdo);
      try{
        $id =  $insert-> criaFuncionario($nome, $sobreNome, $cpf, $rg, $dataNascimento, $estadoCivil,$logradouro, $numResidencia, $complemento, $bairro, $cidade, $cep,  $estado, $admissao,$rfid);
        echo  $id ;
    }
    catch (\PDOException $e) {
    echo $e->getMessage();
}
//$id =  $insert -> criaFuncionario('pablo','nunes','13123114279','1434512341','06041996','solteiro','laguna','155','r12','erqrq','dui','38400296','mG','1612942');


?>
