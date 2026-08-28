# 📘 Atividade: Pipeline Automatizado de Dados

## 🎯 Objetivo

Construa um pipeline de dados usando apenas Python e sua biblioteca padrão. Você irá ler um arquivo CSV, validar e transformar os registros, armazená-los em um banco SQLite e gerar um relatório resumido.

## 📝 Tarefas

### 🛠️ Ler e normalizar os dados

#### Descrição
Implemente a leitura do arquivo `data.csv` e normalize os registros para que todos tenham o mesmo formato. Os valores numéricos devem ser convertidos para os tipos corretos, e espaços extras devem ser removidos dos textos.

#### Requisitos
O programa concluído deve:

- Usar o módulo `csv` para ler o arquivo, sem depender de pandas.
- Criar uma função `load_records(filename)` que retorne uma lista de dicionários.
- Converter `quantity` para inteiro e `unit_price` para número decimal.
- Remover espaços no início e no fim dos campos de texto.
- Informar quantos registros foram carregados.

### 🛠️ Validar e transformar os registros

#### Descrição
Adicione uma etapa de qualidade de dados ao pipeline. Registros inválidos devem ser separados e não podem ser enviados ao banco de dados.

#### Requisitos
O programa concluído deve:

- Criar uma função `validate_record(record)` que retorne uma lista de mensagens de erro.
- Considerar inválido um registro sem `date`, `category` ou `product`.
- Considerar inválidos valores de `quantity` menores ou iguais a zero e valores de `unit_price` negativos.
- Criar uma função `transform_records(records)` que acrescente o campo `total` (`quantity * unit_price`) aos registros válidos.
- Exibir a quantidade de registros válidos e inválidos e os erros encontrados.

### 🛠️ Armazenar os dados em SQLite

#### Descrição
Persista os registros válidos em um banco SQLite chamado `sales.db`. A execução do pipeline deve poder ser repetida sem duplicar os dados do arquivo de entrada.

#### Requisitos
O programa concluído deve:

- Usar o módulo `sqlite3` para criar uma tabela `sales`.
- Armazenar data, categoria, produto, quantidade, preço unitário e total.
- Criar uma chave única que impeça a mesma venda de ser inserida duas vezes.
- Usar consultas parametrizadas ao inserir os dados.
- Fechar a conexão ao terminar, inclusive quando ocorrer um erro.

### 🛠️ Gerar um relatório automatizado

#### Descrição
Consulte o banco de dados e gere um relatório de texto chamado `report.txt` com indicadores úteis sobre as vendas processadas.

#### Requisitos
O programa concluído deve:

- Criar uma função `generate_report(connection, filename)`.
- Informar o total de vendas, a quantidade total de itens e a receita total.
- Listar a receita agrupada por categoria em ordem decrescente.
- Incluir a data e hora de geração do relatório.
- Executar todas as etapas por meio de uma função `main()`.
