<?php
if (isset($_POST['connect'])) {
  require 'postgresqlphpconnect/vendor/autoload.php';
  use PostgreSQL\Connection as Connection;
  try {
      Connection::get()->connect();
      echo 'A connection to the PostgreSQL database sever has been established successfully.';
  } catch (\PDOException $e) {
      echo $e->getMessage();
    }
  }


?>
