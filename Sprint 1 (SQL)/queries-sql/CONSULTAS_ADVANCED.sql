use sucos_vendas;


SELECT Nome FROM tabela_de_clientes WHERE Nome LIKE '%Mattos%';

SELECT * FROM tabela_de_produtos WHERE SABOR LIKE '%Maça%' AND EMBALAGEM = 'PET';

SELECT * FROM tabela_de_clientes;

SELECT DISTINCT BAIRRO FROM tabela_de_clientes WHERE CIDADE = 'Rio de Janeiro' LIMIT 1, 4;

SELECT DISTINCT * FROM notas_fiscais WHERE DATA_VENDA = '2017-01-01' ORDER BY DATA_VENDA LIMIT 10;

SELECT * FROM tabela_de_produtos WHERE NOME_DO_PRODUTO = 'Linha Refrescante - 1 Litro - Morango/Limão' ORDER BY PRECO_DE_LISTA DESC;  

SELECT codigo_do_produto,  sum(quantidade) as SomaQuantidades FROM itens_notas_fiscais where codigo_do_produto = 1101035 group by codigo_do_produto;


SELECT CPF, COUNT(NUMERO) AS COMPRAS FROM notas_fiscais
	WHERE YEAR(DATA_VENDA) = 2016 
    GROUP BY CPF 
    HAVING COMPRAS > 2000
    ORDER BY COMPRAS DESC;
    
SELECT YEAR(DATA_DE_NASCIMENTO), CASE
		WHEN YEAR(DATA_DE_NASCIMENTO) < 1990 THEN 'Velhos'
        WHEN YEAR(DATA_DE_NASCIMENTO) BETWEEN 1990 AND 1995 THEN 'Jovens'
        WHEN YEAR(DATA_DE_NASCIMENTO) > 1995 THEN 'Crianças'
		END AS Status_Clientes 
        FROM tabela_de_clientes 
        GROUP BY YEAR(DATA_DE_NASCIMENTO), CASE
		WHEN YEAR(DATA_DE_NASCIMENTO) < 1990 THEN 'Velhos'
        WHEN YEAR(DATA_DE_NASCIMENTO) BETWEEN 1990 AND 1995 THEN 'Jovens'
        WHEN YEAR(DATA_DE_NASCIMENTO) > 1995 THEN 'Crianças'
		END
        ORDER BY YEAR(DATA_DE_NASCIMENTO);
        
        