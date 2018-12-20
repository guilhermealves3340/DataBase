<?php
    class DataBase {
        private $host = 'localhost';
        private $port = '5050';
        private $usuario = 'root';
        private $senha = '1997';
        private $database = 'db_banco';

        public function conecta_mysql(){

            $con = pg_connect($this->host, $this->usuario, $this->senha, $this->database,$this->port);
            pg_set_charset($con, 'utf8');

            if(mysqli_connect_errno()){
                echo 'Erro ao tentar se conectar com o BD MYSQL: '.mysqli_connect_errno();
            }

            return $con;
        }
    }
?>
