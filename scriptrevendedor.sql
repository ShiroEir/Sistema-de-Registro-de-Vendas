CREATE DATABASE revendedor;

CREATE TABLE produto(
	codigo int NOT NULL PRIMARY KEY,
	nome varchar(50) NOT NULL,
	quantidade int NOT NULL,
	preço_unitario real
);