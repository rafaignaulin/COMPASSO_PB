
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Logo_CompassoUOL_Positivo.png/440px-Logo_CompassoUOL_Positivo.png"/>


# PROGRAMA DE BOLSAS COMPASSO
# RAFAEL IGNAULIN
# RESUMO SEMANA 06


# Parte 01
- Curso AWS Training  Data Analytics
 
 Introducao ao Data Analytics e ao Big Data
 
 Empresas gastam milhoes de dolares para armazenar  dados, porem nao fazem nada com eles.

 Componentes de uma analise de data: 
 - Coletar os dados, armazenar os dados;
 - Processar e analisar os dados;
 - Consumir os dados para gerar insights importantes.


  5 Vs : Volume, Velocidade, Variedade, Veracidade e Valor
> Volume: É a quantidade de dados trafegados. 
>> - Dados Estruturados
>> - Dados Semi-Estruturados
>> - Dados Não Estruturados
>
> É fato  que os dados estao cada vez maiores e mais diversos a cada dia, por isso devemos aprimorar e analisar cada vez mais nossos dados.
>
> Podemos armazenar os dados em forma de Buckets no Amazon S3, separados em object keys.
>
> - Data  Lakes:
>> Armazenando grandes quantidades de dados brutos (em maioria não estruturado), em um repositorio centralizado e com menor custo.
>> 
>> Amazon EMR é um servico de Data Lakes da amazon com suporte para frameworks conhecidos, como o Apache Hadoop e o Apache Spark.
>>
>> Cientista de dados normalmente gastam 60% do tempo limpando e organizando dados e 19% coletando em Datasets.
>
> - Data Warehouse
>> Armazenando quantidades medias de dados já analisados, transformados e preparados para analises de mercado.
>> - Data marts é uma pequena parte de um Data Warehouse
>>
>> Amazon Redshift é o serviço que cria um sistema de Data Warehouse no ecossistema AWS.
>
> - Apache Hadoop é um framework de processamento distribuido para big data. Os clusters utilizam o HDFS (Hadoop Distributed File System) para guardar os dados locais para processamento.
>> Beneficios de usar o Apache Hadoop
>> - Administra grande quantidade de variedade de dados.
>> - Possui uma grande quantidade de soluções construidas para o ecosistema Apache.
>> - Construido para garantir velocidade com alto volume de dados do Big Data.


> Velocidade: é a rapidez com que os dados sao processados.
>> "Quando negócios precisam de insights e decisões rápidas dos dados que eles estão coletando, eles precisam focar na velocidade da ánalise de dados."
>
> Tipos de processamento de dados:
> - Batch Processing (Processamento em lotes): São processados grandes quantidades de dados em lotes. São divididos em processamentos agendados e periódicos. (Terabytes, petabytes - horas, dias)
> - Stream Processing (Processamnto de dados rapidos): São processados pequenas quantidades de dados, e em quase tempo real - ou em tempo real. (Gigabytes - milisegundos, minutos)
>
> Arquitetura  de processamento batch e stream na AWS: Amazon Kinesis (data firehose, data analytics), Amazon  S3, Amazon Glue, Amazon Athena, Amazon Quicksight, 

> Variedade: é a quantidade de tipos diferentes de dados que podemos receber no ecossistema de Big Data.
>> "Quando o negocio fica lotado de dados vindos de diferentes lugares, que quando analisados nao se extraem informacoes uteis, temos um problema da analise de variedade desses dados."

>> Tipos de dados: Estruturados, semi estruturados, nao estruturados.
>> 
>> Dados estruturados são aqueles bem fixos, de facil analise. Como exemplo temos Planilhas e tabelas dos bancos de dados.
>>
>> Dados semiestruturados são aqueles que ainda possuem alguma estrutura, mesmo que não muito definida.
>>
>> Dados não estruturados correspondem a 80 % dos dados gerados no mundo. São aqueles dados mais valiosos, porem os  mais dificeis de analisar e os que tem os menores padrões.
>>
>> - Data stores: Bancos de dados Relacionais, e bancos de dados NOSQL (tipos documento, chave valor, e graficos)
>>> - OLTP: Bancos de dados relacionais transacionais
>>> - OLAP: Bancos e dados relacionais analiticos

>Veracidade é os dados que são verificados e se são confiaveis para tomar decisões baseados neles.
>> Integridade de dados  em sistemas de Big Data
>> - Data cleansing: é a analise e limpeza dos dados que estão corrompidos e que não são confiaveis.
>>
>> Schemas(database, information) - organizacao de conteudos para  referencias , indices e relacoes no banco de dados.
>>
>> - ACID:
>>> - Atomicidade: A atomicidade garante que as transaçoes ou falharam completamente ou finalizaram completamente.
>>> - Consistencia: consistencia das transacoes em relacao as regras e constantes.
>>> - Isolamento: Uma transacao nao pode interferir em outra transação em andamento.
>>> - Durabilidade: é sobre manter todas essas mudancas duraveis.
>>
>> - BASE:
>>> - Basic Available: Estar pronto a resposta para a requisicao imediatamente;
>>> - Soft State: Um estado que pode ser mudado, de forma que se  torna totalmente consistente;
>>> - Eventual Consistency: Reforça os dois topicos acima,  que prioriza que os dados vão ser eventualmente consistentes.
>>
>> ELT: Extração, Transformação e "Load" (Inserção)
>>>  Extracao de um dado recebido via batch ou via stream, de um determinado data source (data lake)
>>> Transformação e normalização deste dado;
>>> Inserção deste dado em  um data mart- data warehouse para futura analise.

> Valor: O ultimo V, e o mais importante, é o valor e o poder dos dados  para gerar insights decisões e ações importantissimas  para o rumo do negócio.
>
> "Não adianta absolutamente nada passar por todos os processos de coleta, armazenamento e transformação desses dados se a analise final for completamente deficiente."
>> - Information analytics : Processar a informação  para encontrar  o valor contido nele.                        
>> - Operational analytics: É uma forma de analise de dados para receber e reportar dado em operações de TI.
>>
>>> - Descritivo:  O que aconteceu?
>>> - Diagnostico: Como isso aconteceu?
>>> - Preditivo: O que irá acontecer?
>>> - Prescriptivo: O que eu devo fazer?
>>> - Cognitivo: Quais são as açoes recomendadas baseada no "learning" do sistema?
>>
>> Reports:
>> - Estáticos: Utilizando planilhas, PDFs e  slides para analisar os resultados;
>> - Interativos: Estão se tornando mais comum, possui a vantagem que alem de serem estaticos, eles podem aplicar filtros e graficos, mudar  escalas, e agrupar e sortear valores.
>> - Dashboard: é uma interface completamente digital que possui o objetivo de  mostrar todos os pontos a serem analisados.
