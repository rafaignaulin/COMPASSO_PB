#EXERCICIO SEMANA 01 PROGRAMA DE BOLSAS COMPASSO
#RAFAEL IGNAULIN

USE programa_bolsas

#3 A
# Retorna todos os livros publicados após 2014, em ordem crescente
SELECT * FROM LIVRO WHERE (Publicacao >= '2014-01-01') ORDER BY (Publicacao);

#3 B
# Retorna os 10 livros mais caros
SELECT * FROM LIVRO ORDER BY(Valor) DESC LIMIT 10;

#3 C
# Retorna as 5 editoras com maior quantidade de livros
SELECT E.Nome, L.Editora ,COUNT(L.Editora) as Contador_Livros
	FROM EDITORA E INNER JOIN LIVRO L
	ON E.CodEditora = L.Editora
	GROUP BY E.CodEditora 
	ORDER BY COUNT(L.Editora) DESC LIMIT 5;

#3 D
# Retorna por ordem do codigo do Autor todas os Autores e suas respectivas publicaçoes
SELECT A.Nome, A.CodAutor, COUNT(L.Autor) AS Contador_Publicacoes
	FROM AUTOR A LEFT JOIN LIVRO L
	ON A.CodAutor = L.Autor
	GROUP BY A.CodAutor;

#3 E
# Retorna por ordem do codigo da Editora todas as Editoras e suas respectivas publicaçoes
SELECT E.Nome, E.CodEditora, COUNT(L.Autor) AS Contador_Publicacoes
	FROM EDITORA E LEFT JOIN LIVRO L
	ON E.CodEditora = L.Editora 
	GROUP BY E.CodEditora;

#3 F
# Retorna o Autor com mais livros
SELECT A.Nome, A.CodAutor, COUNT(L.Autor) AS Contador_de_Livros
	FROM AUTOR A LEFT JOIN LIVRO L
	ON A.CodAutor = L.Autor
	GROUP BY A.CodAutor
	ORDER BY COUNT(L.Autor) DESC LIMIT 1;

#3 G
# Retorna por ordem alfabética o Autor com menos livros
SELECT A.Nome, A.CodAutor, COUNT(L.Autor) AS Contador_de_Livros
	FROM AUTOR A LEFT JOIN LIVRO L
	ON A.CodAutor = L.Autor
	GROUP BY A.CodAutor
	ORDER BY COUNT(L.Autor), A.Nome ASC LIMIT 1;



