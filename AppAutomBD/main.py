import pandas as pd
from dateutil.utils import today
from numpy.core.defchararray import capitalize

# Carregando as tabelas
tab_produtos = pd.read_excel("Base de Dados.xlsx", sheet_name="FactProdutos")
tab_categoria = pd.read_excel("Base de Dados.xlsx", sheet_name="DimCategoria")
tab_fabrica = pd.read_excel("Base de Dados.xlsx", sheet_name="DimFabricas")

# Definindo o cdProduto sendo o último cdProduto + 1
cd_produto = tab_produtos['cdProduto'].iloc[-1] + 1

# Capturando os valores do usuário
categoria = capitalize(input("Digite a categoria do produto: "))
metal = capitalize(input("Digite o metal do produto: "))
nome = input("Digite o nome do produto: ")
modal = input("Digite a modalidade do produto: ")
custo = float(input("Digite o custo do produto: "))
vista = custo * 2.2
prazo = vista * 1.1
fabrica = capitalize(input("Digite a fábrica do produto: "))
cod_fabrica = input("Digite o código que a fábrica dá ao produto: ")
data_compra = today()


# Transformando a categoria no ID da categoria selecionada
linha_categoria = tab_categoria.loc[tab_categoria['Categoria'] == categoria]
categoria = linha_categoria['ID'].iloc[0]
pref_cd = linha_categoria['Prefixo'].iloc[0]

# Definindo o código
codigo = str(pref_cd) + str(cd_produto)

# Transformando a fábrica no ID da fábrica selecionada
linha_fabrica = tab_fabrica.loc[tab_fabrica["Fábrica"] == fabrica]
fabrica = linha_fabrica['ID'].iloc[0]

d = {'Codigo': [codigo], 'cdProduto': [cd_produto], 'cdCategoria': [categoria], 'Metal': [metal],
     'Nome': [nome], 'Modalidade': [modal], 'Custo': [custo], ' Vista': [vista], 'Prazo': [prazo],
     'cdFabrica': [fabrica], 'Cod Fabrica': [cod_fabrica], 'Data Compra': [data_compra]}

linha = pd.DataFrame(data=d)

resultado = pd.concat([tab_produtos, linha], axis=0)
print(resultado)
