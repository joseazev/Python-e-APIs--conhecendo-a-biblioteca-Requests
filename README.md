# Python e APIs: Conhecendo a Biblioteca Requests

Esta classe `ManipulacaoDeRepositorio` fornece métodos para interagir com a API do GitHub, permitindo a criação de repositórios e o upload de arquivos. A classe é inicializada com um nome de usuário do GitHub e utiliza um token de acesso para autenticação.

## Funcionalidades

### 1. Criação de Repositórios

O método `criando_repositorio` permite criar um novo repositório no GitHub. 

#### Parâmetros:
- `name_repo` (str): O nome do repositório a ser criado.

#### Exemplo de Uso:
```python
repo = ManipulacaoDeRepositorio('seu_username')
repo.criando_repositorio('nome_do_repositorio')
```

### 2. Upload de Arquivos

O método `upload_arquivo` permite fazer o upload de um arquivo para um repositório especificado no GitHub.

#### Parâmetros:
- `path_file` (str): O caminho do arquivo a ser enviado.
- `name_repo` (str): O nome do repositório onde o arquivo será enviado.
- `name_file` (str): O nome do arquivo a ser enviado.

#### Exemplo de Uso:
```python
repo = ManipulacaoDeRepositorio('seu_username')
repo.upload_arquivo('caminho/do/arquivo.txt', 'nome_do_repositorio', 'arquivo.txt')
```

### 3. Configuração de Arquivo (Método Interno)

O método estático `__configurar_arquivo` lê e codifica um arquivo em base64. Esse método é utilizado internamente para preparar arquivos para upload.

#### Parâmetros:
- `path_sender` (str): O caminho do arquivo a ser lido e codificado.

---

### Exemplo Completo de Uso

```python
from manipulacao_repositorio import ManipulacaoDeRepositorio

# Inicializa a classe com o nome de usuário do GitHub
repo = ManipulacaoDeRepositorio('seu_username')

# Cria um novo repositório
repo.criando_repositorio('nome_do_repositorio')

# Resumo da Classe `DadosRepositorios`

A classe `DadosRepositorios` foi desenvolvida para interagir com a API do GitHub e coletar informações sobre os repositórios de um usuário específico. Esta classe facilita a listagem de repositórios e a extração de informações relevantes, como os nomes dos repositórios e as linguagens de programação usadas.

## Funcionalidades

### 1. Inicialização da Classe

A classe é inicializada com o nome do proprietário dos repositórios (`owner`). Durante a inicialização, a classe também configura a URL base da API do GitHub e os cabeçalhos necessários para autenticação usando um token de acesso.

### 2. Listar Repositórios

O método privado `__lista_repositorio` coleta uma lista de repositórios do usuário especificado. Ele realiza múltiplas requisições à API do GitHub para obter até 20 páginas de resultados, lidando com possíveis exceções durante o processo.

### 3. Extrair Nomes dos Repositórios

O método privado `__nome_repos` recebe a lista de repositórios em formato JSON e extrai os nomes dos repositórios, retornando uma lista com esses nomes.

### 4. Extrair Linguagens dos Repositórios

O método privado `__nome_linguagens` também recebe a lista de repositórios em formato JSON e extrai as linguagens de programação usadas em cada repositório, retornando uma lista com essas linguagens.

### 5. Criar DataFrame com Informações dos Repositórios

O método `cria_df_linguagens` utiliza os métodos anteriores para obter a lista de repositórios, extrair os nomes e as linguagens de programação, e então cria um DataFrame do Pandas contendo essas informações. O DataFrame resultante possui duas colunas: `repository_name` e `language`.

## Exemplo de Uso

```python
# Criar instância da classe para o usuário 'amzn'
amazon_rep = DadosRepositorios('amzn')
# Criar DataFrame com os repositórios e linguagens do usuário 'amzn'
ling_mais_usada_amzn = amazon_rep.cria_df_linguagens()

# Criar instância da classe para o usuário 'netflix'
netflix_rep = DadosRepositorios('netflix')
# Criar DataFrame com os repositórios e linguagens do usuário 'netflix'
ling_mais_usada_netflix = netflix_rep.cria_df_linguagens()

# Salvando os dados em arquivos CSV
ling_mais_usada_amzn.to_csv('dados/amazon_rep.csv', index=False)
ling_mais_usada_netflix.to_csv('dados/netflix_rep.csv', index=False)
```

Esta classe proporciona uma maneira simples e eficiente de coletar e organizar dados sobre repositórios do GitHub, permitindo uma análise rápida e a geração de relatórios sobre as linguagens de programação utilizadas.
# Faz upload de um arquivo para o repositório
repo.upload_arquivo('caminho/do/arquivo.txt', 'nome_do_repositorio', 'arquivo.txt')
```

Esta classe facilita a interação programática com o GitHub, automatizando tarefas comuns como a criação de repositórios e o upload de arquivos.
