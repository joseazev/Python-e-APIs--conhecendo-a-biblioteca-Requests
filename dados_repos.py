import requests
import pandas as pd

class DadosRepositorios:
    """
    Classe para obter e manipular dados de repositórios no GitHub.

    Esta classe permite listar repositórios de um usuário específico e criar um DataFrame
    com os nomes dos repositórios e suas respectivas linguagens de programação.

    Atributos:
    ----------
    owner : str
        O nome do proprietário dos repositórios no GitHub.
    
    Métodos:
    --------
    cria_df_linguagens():
        Cria um DataFrame com os nomes dos repositórios e suas linguagens de programação.
    """

    def __init__(self, owner):
        """
        Inicializa a classe DadosRepositorios com o nome do proprietário dos repositórios.

        Parâmetros:
        -----------
        owner : str
            O nome do proprietário dos repositórios no GitHub.
        """
        self.owner = owner
        self.__api_base_url = 'https://api.github.com'
        self.__access_token = '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'
        self.__headers = {
            'Authorization': 'Bearer ' + self.__access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }
        
    def __lista_repositorio(self):
        """
        Lista os repositórios do proprietário.

        Retorna:
        --------
        repos_list : list
            Uma lista de repositórios em formato JSON.
        """
        repos_list = []
        for page_num in range(1, 20):
            try:
                url_page = f'{self.__api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url_page, headers=self.__headers)
                repos_list.append(response.json())
            except Exception as e:
                print(f"Erro ao listar repositórios: {e}")
                repos_list.append(None)
            
        return repos_list
    
    def __nome_repos(self, repos_list):
        """
        Extrai os nomes dos repositórios de uma lista de repositórios.

        Parâmetros:
        -----------
        repos_list : list
            Lista de repositórios em formato JSON.

        Retorna:
        --------
        repo_names : list
            Lista de nomes de repositórios.
        """
        repo_names = []
        for page in repos_list:
            if page is not None:
                for repo in page:
                    try:
                        repo_names.append(repo['name'])
                    except KeyError:
                        pass
            
        return repo_names
    
    def __nome_linguagens(self, repos_list):
        """
        Extrai as linguagens dos repositórios de uma lista de repositórios.

        Parâmetros:
        -----------
        repos_list : list
            Lista de repositórios em formato JSON.

        Retorna:
        --------
        repos_languages : list
            Lista de linguagens dos repositórios.
        """
        repos_languages = []
        for page in repos_list:
            if page is not None:
                try:
                    for repo in page:
                        repos_languages.append(repo['language'])
                except KeyError:
                    pass

        return repos_languages
    
    def cria_df_linguagens(self):
        """
        Cria um DataFrame com os nomes dos repositórios e suas linguagens de programação.

        Retorna:
        --------
        dados_amzn : pd.DataFrame
            DataFrame contendo os nomes dos repositórios e suas linguagens de programação.
        """
        repositorios = self.__lista_repositorio()
        nome = self.__nome_repos(repositorios)
        linguagens = self.__nome_linguagens(repositorios)

        dados_amzn = pd.DataFrame()
        dados_amzn['repository_name'] = nome
        dados_amzn['language'] = linguagens

        return dados_amzn

# Exemplo de uso
amazon_rep = DadosRepositorios('amzn')
ling_mais_usada_amzn = amazon_rep.cria_df_linguagens()
#print(ling_mais_usada_amzn)

netflix_rep = DadosRepositorios('netflix')
ling_mais_usada_netflix = netflix_rep.cria_df_linguagens()

# Salvando os dados
ling_mais_usada_amzn.to_csv('dados/amazon_rep.csv', index=False)
ling_mais_usada_netflix.to_csv('dados/netflix_rep.csv', index=False)
