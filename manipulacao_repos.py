import requests
import base64

class ManipulacaoDeRepositorio:
    """
    Classe para manipulação de repositórios no GitHub.
    
    Esta classe permite criar repositórios e fazer upload de arquivos para repositórios 
    do GitHub usando a API do GitHub.

    Atributos:
    ----------
    username : str
        O nome de usuário do GitHub.
    
    Métodos:
    --------
    criando_repositorio(name_repo):
        Cria um novo repositório no GitHub.
        
    upload_arquivo(path_file, name_repo, name_file):
        Faz upload de um arquivo para o repositório especificado no GitHub.
    """

    def __init__(self, username) -> None:
        """
        Inicializa a classe ManipulacaoDeRepositorio com o nome de usuário do GitHub.

        Parâmetros:
        -----------
        username : str
            O nome de usuário do GitHub.
        """
        self.username = username
        self.__api_base_url = 'https://api.github.com'
        self.__access_token = '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'
        self.__headers = {
            'Authorization': 'Bearer ' + self.__access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def criando_repositorio(self, name_repo):
        """
        Cria um novo repositório no GitHub.

        Parâmetros:
        -----------
        name_repo : str
            O nome do repositório a ser criado.
        
        Retorna:
        --------
        None
        """
        url = f'{self.__api_base_url}/user/repos'
        data = {
            'name': name_repo,
            'description': 'Repositório com as linguagens de programação da Amazon',
            'private': False
        }

        response = requests.post(url, json=data, headers=self.__headers)
        print(f'Status da criação do repositório: {response.status_code}')

    @staticmethod
    def __configurar_arquivo(path_sender):
        """
        Lê e codifica um arquivo em base64.

        Parâmetros:
        -----------
        path_sender : str
            O caminho do arquivo a ser lido e codificado.
        
        Retorna:
        --------
        encoded_content : bytes
            O conteúdo do arquivo codificado em base64.
        """
        with open(path_sender, 'rb') as file:
            file_content = file.read()

        encoded_content = base64.b64encode(file_content)
        print('Configuração de arquivo OK')
        return encoded_content

    def upload_arquivo(self, path_file, name_repo, name_file):
        """
        Faz upload de um arquivo para o repositório especificado no GitHub.

        Parâmetros:
        -----------
        path_file : str
            O caminho do arquivo a ser enviado.
        name_repo : str
            O nome do repositório onde o arquivo será enviado.
        name_file : str
            O nome do arquivo a ser enviado.
        
        Retorna:
        --------
        None
        """
        with open(path_file, 'rb') as file:
            file_content = file.read()

        encoded_content = base64.b64encode(file_content)

        url = f'{self.__api_base_url}/repos/{self.username}/{name_repo}/contents/{name_file}'

        data = {
            'message': 'Adicionando um novo arquivo',
            'content': encoded_content.decode('utf-8')
        }

        response = requests.put(url, json=data, headers=self.__headers)
        print(f'Status do upload do arquivo: {response.status_code}')

    def deletar_repositorio(self,repo):
        owner = self.username
        repo = repo
        url = f'https://api.github.com/repos/{owner}/{repo}'
        
        response = requests.delete(url, headers=self.__headers)
        print(f"status do delete: {response.status_code}")

#intanciando
novo_repo = ManipulacaoDeRepositorio('joseazev')

name_repo = 'linguagens-repositorios-empresas'
name_file = 'netflix_rep.csv'
path_file = f'dados/{name_file}'

novo_repo.deletar_repositorio(name_repo)
novo_repo.criando_repositorio(name_repo)
novo_repo.upload_arquivo(path_file,name_repo,name_file)
