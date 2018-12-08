<?php
namespace PostgreSQL;

class insert {
private $pdo;

public function __construct($pdo) {
        $this->pdo = $pdo;
    }

public function criaFuncionario($nome, $sobreNome, $cpf, $rg, $dataNascimento, $estadoCivil,$logradouro, $numResidencia, $complemento, $bairro, $cidade, $cep,  $estado, $admissao, $rfid) {
     // prepare statement for insert
    $stmt = $this->pdo->prepare('INSERT INTO proj.tb_funcionario (nome, sobreNome, cpf, rg, dataNascimento, estadocivil, logradouro, numResidencia, complemento, bairro, cidade, cep, estado, admissao, idTag) VALUES( :nome, :sobreNome, :cpf, :rg, :dataNascimento, :estadocivil, :logradouro, :numResidencia, :complemento, :bairro, :cidade, :cep, :estado, :admissao,:idTag)');
     // pass values to the statement
     $stmt->bindValue(':nome', $nome);
     $stmt->bindValue(':sobreNome', $sobreNome);
     $stmt->bindValue(':cpf', $cpf);
     $stmt->bindValue(':rg', $rg);
     $stmt->bindValue(':dataNascimento', $dataNascimento);
     $stmt->bindValue(':estadocivil', $estadoCivil);
     $stmt->bindValue(':logradouro', $logradouro);
     $stmt->bindValue(':numResidencia', $numResidencia);
     $stmt->bindValue(':complemento', $complemento);
     $stmt->bindValue(':bairro', $bairro);
     $stmt->bindValue(':cidade', $cidade);
     $stmt->bindValue(':cep', $cep);
     $stmt->bindValue(':estado', $estado);
     $stmt->bindValue(':admissao', $admissao);
     $stmt->bindValue(':idTag', $rfid);

     // execute the insert statement
     $stmt->execute();

     // return generated id
     echo "Usuário gerado com sucesso!";
 }
}
