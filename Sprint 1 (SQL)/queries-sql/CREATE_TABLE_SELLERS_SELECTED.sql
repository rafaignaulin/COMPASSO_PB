INSERT INTO TABELA_DE_VENDEDORES (matricula, NOME, PERCENTUAL_COMISSAO, DATA_ADMISSAO, FERIAS)
	VALUES ('00101', 'Carol', 10.2, '2015-06-07', 0),
			('01101', 'Rafael', 45.2, '2011-06-07', 0),
            ('02101', 'Roberta', 10.2, '2016-06-07', 0),
            ('03101', 'Gislaine', 11.2, '2015-06-07', 1),
            ('04101', 'Mateus', 0.2, '2015-08-07', 1),
            ('05101', 'Marcos', 19.2, '2015-06-07', 1),
            ('06101', 'Guilherme', 35.2, '2015-06-07', 0);
            

SELECT * FROM TABELA_DE_VENDEDORES;

SELECT * FROM TABELA_DE_VENDEDORES WHERE (PERCENTUAL_COMISSAO > 10);

SELECT * FROM TABELA_DE_VENDEDORES WHERE (DATA_ADMISSAO < '2015-06-07');
SELECT * FROM TABELA_DE_VENDEDORES WHERE (YEAR(DATA_ADMISSAO) > 2014);
SELECT * FROM TABELA_DE_VENDEDORES WHERE FERIAS AND YEAR(DATA_ADMISSAO) < 2016;