#ATIVIDADE SEMANA 2
#PROGRAMA DE BOLSAS COMPASSO CHAPECÓ
#RAFAEL IGNAULIN

# 10 LIVROS MAIS CAROS
SELECT L.Cod AS 'Código Livro', L.Titulo, 
	L.Autor AS 'Codigo Autor', A.Nome AS 'Nome do Autor',
    L.Valor, L.Editora AS 'Codigo Editora', E.Nome AS 'Nome da Editora' FROM 
	LIVRO L LEFT JOIN AUTOR A 
	ON L.Autor = A.CodAutor
	LEFT JOIN EDITORA E
	ON L.Editora = E.CodEditora
	ORDER BY L.Valor DESC LIMIT 10;

# Quantidades de livros estão ordenados pela ordem alfabetica da Editora 
SELECT L.Editora AS 'Codigo Editora', E.Nome AS 'Nome da Editora' , COUNT(L.Editora) as 'Quantidade de Livros' FROM 
	LIVRO L INNER JOIN EDITORA E
	ON L.Editora = E.CodEditora
	GROUP BY E.CodEditora
	ORDER BY COUNT(L.Editora) DESC, L.Editora  LIMIT 5;
    
 
