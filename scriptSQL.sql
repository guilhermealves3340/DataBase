CREATE SCHEMA proj

CREATE TABLE proj.funcionarios(
	userID			INTEGER,
	codDep			INTEGER,
	codCargo		INTEGER,
	estadoCivil		INTEGER NOT NULL,
	cargaHoraria	DOUBLE NOT NULL,
	salario			NUMERIC(7,2) NOT NULL,
	ativo			BOOLEAN NOT NULL,
	idTag			INTEGER NOT NULL,
	CONSTRAINT pk_func_UID PRIMARY KEY(userID),
  CONSTRAINT fk_func_userID FOREIGN KEY(userID) REFERENCES proj.infoPessoais(cpf),
  CONSTRAINT fk_func_codDep FOREIGN KEY(codDep) REFERENCES proj.departamentos(codDep),
  CONSTRAINT fk_func_codCargo FOREIGN KEY(codCargo) REFERENCES proj.cargos(codCargo),
  admissao        TIMESTAMP NOT NULL,
  demissao        TIMESTAMP
)

CREATE TABLE proj.infoPessoais(
	nome			    VARCHAR(20) NOT NULL,
	sobreNome		    VARCHAR(35) NOT NULL,
	cpf				    VARCHAR(13) NOT NULL,
	rg				    VARCHAR(10) NOT NULL,
	dataNascimento	    TIMESTAMP,
  logradouro          VARCHAR(40) NOT NULL,
  numResidencia       INTEGER NOT NULL,
  complemento         VARCHAR(15),
  bairro              VARCHAR(15),
  cidade              VARCHAR(15) NOT NULL,
  cep                 VARCHAR(9) NOT NULL,
  estado          VARCHAR(2) NOT NULL,
  CONSTRAINT pk_cpf PRIMARY KEY(cpf)
)

CREATE TABLE proj.contato(
    userID          INTEGER NOT NULL,
    tel             VARCHAR(15),
    cel             VARCHAR(15),
    email           VARCHAR(32),
    CONSTRAINT fk_cont_userID  FOREIGN KEY(userID) REFERENCES proj.infoPessoais(cpf),
    CONSTRAINT pk_cpf PRIMARY KEY(userID)
)

CREATE TABLE proj.login(
    password        VARCHAR(15) NOT NULL,
    userID          INTEGER NOT NULL,
    CONSTRAINT fk_login_userID FOREIGN KEY(userID) REFERENCES proj.infoPessoais(cpf),
    CONSTRAINT pk_userID PRIMARY KEY(userID)
)

CREATE TABLE proj.departamentos(
    codDep          INTEGER,
    departamento    VARCHAR(10),
    CONSTRAINT pk_codDep PRIMARY KEY(codDep)
)

CREATE TABLE proj.cargos(
		codDep          INTEGER,
		codCargo        INTEGER,
    cargo           VARCHAR(10),
    CONSTRAINT pk_carg_codCargo PRIMARY KEY (codCargo),
		CONSTRAINT fk_carg_codDep FOREIGN KEY (codDep) REFERENCES proj.departamentos(codDep)
)
