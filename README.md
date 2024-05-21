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

# Faz upload de um arquivo para o repositório
repo.upload_arquivo('caminho/do/arquivo.txt', 'nome_do_repositorio', 'arquivo.txt')
```

Esta classe facilita a interação programática com o GitHub, automatizando tarefas comuns como a criação de repositórios e o upload de arquivos.
