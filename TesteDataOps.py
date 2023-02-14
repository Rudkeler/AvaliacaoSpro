#importando libs Pandas e Client MongoDB
import pandas as pd
from pymongo import MongoClient

carros = {
    'Carro': ['Onix', 'Polo', 'Sandero', 'Fiesta', 'City'],
    'Cor': ['Prata', 'Branco', 'Prata', 'Vermelho', 'Preto'],
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda']
}
#criando DataFrame para carros
dfCarros = pd.DataFrame(carros)

montadoras = {
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda'],
    'País': ['EUA', 'Alemanha', 'França', 'EUA', 'Japão'],
}

#criando DataFrame para montadoras
dfMontadoras = pd.DataFrame(montadoras)

#conectando ao MongoDB
client = MongoClient('localhost', 27017)
db = client['TestDataOps']

#criando collections
collection1 = db['Carros']
collection2 = db['Montadoras']

#gravando dataframes no mongo
carros = dfCarros.to_dict(orient='records')
montadoras = dfMontadoras.to_dict(orient='records')

#gravando dados no mongo
collection1.insert_many(carros)
collection2.insert_many(montadoras)


