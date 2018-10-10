CREATE SCHEMA proj;

CREATE TABLE proj.tb_funcionario(
	userID		    	INTEGER,
	codCargo		    INTEGER NOT NULL,
	estadoCivil		  INTEGER NOT NULL,              
	cargaHoraria	  NUMERIC NOT NULL,
	salario			    NUMERIC(7,2) NOT NULL,
	ativo			      BOOLEAN NOT NULL,
	idTag			      INTEGER NOT NULL,
	CONSTRAINT pk_func_userID PRIMARY KEY(userID),
  admissao        TIMESTAMP NOT NULL,
  demissao        TIMESTAMP
);

CREATE TABLE proj.tb_infoPessoais(
	userID			INTEGER,
	nome			      VARCHAR(20) NOT NULL,
	sobreNome		    VARCHAR(35) NOT NULL,
	cpf				      VARCHAR(13) NOT NULL,
	rg				      VARCHAR(10) NOT NULL,
	dataNascimento  TIMESTAMP,
  	logradouro      VARCHAR(40) NOT NULL,
  	numResidencia   INTEGER NOT NULL,
  	complemento     VARCHAR(15),
  	bairro          VARCHAR(15),
  	cidade          VARCHAR(15) NOT NULL,
  	cep             VARCHAR(9) NOT NULL,
  	estado          VARCHAR(2) NOT NULL,
    CONSTRAINT fk_id_userID FOREIGN KEY(userID) REFERENCES proj.tb_funcionario(userID)
);

CREATE TABLE proj.tb_contato(
    userID          INTEGER NOT NULL,
    tel             VARCHAR(15),
    cel             VARCHAR(15),
    email           VARCHAR(32),
    CONSTRAINT fk_cont_userID  FOREIGN KEY(userID) REFERENCES proj.tb_funcionario(userID)
);

CREATE TABLE proj.tb_login(
    password        VARCHAR(15) NOT NULL,
    userID          INTEGER NOT NULL,
    CONSTRAINT fk_login_userID FOREIGN KEY(userID) REFERENCES proj.tb_funcionario(userID),
    CONSTRAINT pk_userID PRIMARY KEY(userID)
);

CREATE TABLE proj.tb_departamentos(
    codDep          INTEGER,
    departamento    VARCHAR(10),
    CONSTRAINT pk_codDep PRIMARY KEY(codDep)
);

CREATE TABLE proj.tb_cargos(
		codDep          INTEGER,
		codCargo        INTEGER,
    cargo           VARCHAR(10),
    CONSTRAINT pk_carg_codCargo PRIMARY KEY (codCargo),
		CONSTRAINT fk_carg_codDep FOREIGN KEY (codDep) REFERENCES proj.tb_departamentos(codDep)
);

CREATE TABLE proj.tb_entrada(
  userID            INTEGER,
  dia               DATE NOT NULL,
  horas             TIME NOT NULL,
  CONSTRAINT fk_IN_userID FOREIGN KEY (userID) REFERENCES proj.tb_funcionario(userID)
);

CREATE TABLE proj.tb_almoco(
  userID            INTEGER,
  dia               DATE NOT NULL,
  horas             TIME NOT NULL,
  CONSTRAINT fk_ALM_userID FOREIGN KEY (userID) REFERENCES proj.tb_funcionario(userID)
);

CREATE TABLE proj.tb_retorno(
  userID            INTEGER,
  dia               DATE NOT NULL,
  horas             TIME NOT NULL,
  CONSTRAINT fk_RTN_userID FOREIGN KEY (userID) REFERENCES proj.tb_funcionario(userID)
);

CREATE TABLE proj.tb_saida(
  userID            INTEGER,
  dia               DATE NOT NULL,
  horario           TIME NOT NULL,
  CONSTRAINT fk_OUT_userID FOREIGN KEY (userID) REFERENCES proj.tb_funcionario(userID)
);

DROP SCHEMA proj;
DROP TABLE proj.tb_funcionario;
DROP TABLE proj.tb_infopessoais;
