<head>
    <title>Instituto Aprenda Mais</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" type="image/png" href="../img/logo.png">
    <link rel="stylesheet" type="text/css" href="../css/main.css">
    <link rel="stylesheet" href="../css/bootstrap.min.css">
    <link rel="stylesheet" href="../font-awesome-4.7.0/css/font-awesome.min.css">
</head>

<?php $aqui = basename($_SERVER['PHP_SELF'],'.php'); ?>

<header class="app-header">
    <a class="app-header__logo" href="index.php">
        <div class="container">
            <img src="../img/logo.png" width="40px">
        </div>
    </a>
    <a class="app-sidebar__toggle" href="#" data-toggle="sidebar" aria-label="Hide Sidebar"></a>

    <ul class="app-nav">

        <li class="dropdown">
            <a class="app-nav__item" href="#" data-toggle="dropdown" aria-label="Open Profile Menu">
                <i class="fa fa-user fa-lg"></i>
            </a>

            <ul class="dropdown-menu settings-menu dropdown-menu-right">
                <li>
                    <a class="dropdown-item" href="sair.php"><i class="fa fa-sign-out fa-lg"></i> Sair</a>
                </li>
            </ul>
        </li>
    </ul>
</header>

<div class="app-sidebar__overlay" data-toggle="sidebar"></div>

<aside class="app-sidebar">
    <div class="app-sidebar__user">
    </div>

    <ul class="app-menu">

        <li class="treeview"><a class="app-menu__item  <?php if(($aqui == 'index') || ($aqui == 'newEmployee')) echo 'active'; ?>" href="#" data-toggle="treeview"><i class="app-menu__icon fa fa-users"></i><span class="app-menu__label">Funcionários</span><i class="treeview-indicator fa fa-angle-right"></i></a>
            <ul class="treeview-menu">
                <li>
                    <a class="treeview-item <?php if($aqui == 'index') echo 'active'; ?>" href="index.php"> Listar</a>
                </li>
                <li>
                    <a class="treeview-item <?php if($aqui == 'newEmployee') echo 'active'; ?>" href="newEmployee.php"> Cadastrar</a>
                </li>
            </ul>
        </li>

        <li>
            <a class="app-menu__item <?php if($aqui == 'relatorio') echo 'active'; ?>" href="relatorio.php">
                <i class="app-menu__icon fa fa-file-text"></i>
                <span class="app-menu__label">Relatórios</span>
            </a>
        </li>

    </ul>
</aside>
