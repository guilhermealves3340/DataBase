<?php
namespace PostgreSQL;

class Select {
private $pdo;

public function __construct($pdo) {
        $this->pdo = $pdo;
    }

public function verificalogin($username, $password) {
     // prepare statement for insert
    $stmt = $this->pdo->prepare('SELECT tipo_acesso
                                FROM proj.tb_login
                                WHERE login = :username and password = :password');     // pass values to the statement
     $stmt->bindValue(':username', $username);
     $stmt->bindValue(':password', $password);

     // execute the insert statement
     $stmt->execute();
     return $stmt->fetchObject();
 }
}
