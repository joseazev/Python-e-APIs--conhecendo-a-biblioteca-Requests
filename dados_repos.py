import requests
import pandas as pd


class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.__api_base_url = 'https://api.github.com'
        self.__access_token = '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'
        self.__headers = {'Authorization': 'Bearer ' + self.__access_token,
                    'X-gitHub-Api-Version': '2022-11-28'}
        
    def __lista_repositorio(self):
        repos_list = []
        for page_num in range(1, 20):
            try:
                url_page = f'{self.__api_base_url}/users/{self.owner}/repos?page={page_num}'
                
                response = requests.get(url_page, headers=self.__headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
            
        return repos_list
    
    def __nome_repos(self, repos_list):
        repo_names = []
        for page in repos_list:
            for repo in page:
                try:
                    repo_names.append(repo['name'])
                except:
                    pass
            
        return repo_names
    
    def __nome_linguagens(self, repos_list):
        repos_langueges = []
        for page in repos_list:
            try:
                for repo in page:
                    repos_langueges.append(repo['language'])
            except:
                pass

        return repos_langueges
    
    def cria_df_linguagns(self):
        repoositorios = self.__lista_repositorio()
        nome = self.__nome_repos(repoositorios)
        linguagens = self.__nome_linguagens(repoositorios)

        dados_amzn = pd.DataFrame()
        dados_amzn['repository_name'] = nome
        dados_amzn['language'] = linguagens

        return dados_amzn




amazon_rep = DadosRepositorios('amzn')
ling_mais_usada_amzn = amazon_rep.cria_df_linguagns()
#print(ling_mais_usada_amzn)

netflix_rep = DadosRepositorios('netflix')
ling_mais_usada_netflix = netflix_rep.cria_df_linguagns()

#salvando os dados 

ling_mais_usada_amzn.to_csv('dados/amazon_rep.csv', index=False)

ling_mais_usada_netflix.to_csv('dados/netflix_rep.csv', index=False)