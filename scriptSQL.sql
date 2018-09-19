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
    CONSTRAINT pk_userID PRIMARY KEY(userID),
    CONSTRAINT fk_codDep FOREIGN KEY(codDep)
        REFERENCES proj.departamentos(codDep),
    CONSTRAINT fk_codCargo FOREIGN KEY(codCargo)
        REFERENCES proj.cargos(codCargo),
    admissao        TIMESTAMP NOT NULL,
    demissao        TIMESTAMP
)

CREATE TABLE proj.infoPessoais(
	userId			    INTEGER NOT NULL,
	nome			    VARCHAR(20),
	sobreNome		    VARCHAR(35),
	cpf				    VARCHAR(13),
	rg				    VARCHAR(10)
	dataNascimento	    TIMESTAMP,
    largadouro          VARCHAR(40) NOT NULL,
    numResidencia       INTEGER NOT NULL,
    complemento         VARCHAR(15),
    bairro              VARCHAR(15),
    cidade              VARCHAR(15) NOT NULL,
    cep                 VARCHAR(9) NOT NULL,
    estado          VARCHAR(2) NOT NULL
    CONSTRAINT fk_userID FOREIGN KEY(userID)
        REFERENCES proj.funcionarios(userID),

    CONSTRAINT pk_cpf PRIMARY KEY(cpf),
    CONSTRAINT pk_rg PRIMARY KEY(rg)
)

CREATE TABLE proj.contato(
    userID          INTEGER NOT NULL,
    CONSTRAINT fk_userID FOREIGN KEY(userID)
        REFERENCES proj.funcionarios(userID),
    tel             VARCHAR(15),
    cel             VARCHAR(15),
    email           VARCHAR(32),
    CONSTRAINT fk_userID FOREIGN KEY(userID)
        REFERENCES proj.funcionarios(userID)
)

CREATE TABLE proj.login(
    password        VARCHAR(15) NOT NULL,
    userID          INTEGER NOT NULL,
    CONSTRAINT fk_userID FOREIGN KEY(userId),
        REFERENCES proj.funcionarios(userID),
    CONSTRAINT pk_userID PRIMARY KEY(userID)

)

CREATE TABLE proj.departamentos(
    codDep          INTEGER,
    departamento    VARCHAR(10),
    CONSTRAINT pk_codDep PRIMARY KEY(codDep)
)

CREATE TABLE proj.cargos(
    codCargo        INTEGER,
    cargo           VARCHAR(10),
    CONSTRAINT pk_codCargo PRIMARY KEY(codCargo)
)







