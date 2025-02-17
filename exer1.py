"""MUDANÇA DE CARGA TRIBUTARIO"""

produtos = ['computador', 'livro', 'tablete', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']
#cada item da lista dos produtos coressponde a quantidade de venda no mes e preço nessa ordem
produtos_ecommerce = [
    [10000,2500],
    [50000, 40],
    [7000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

qtde = 50000
preco = 40
total = qtde * preco
print('{:,}'.format(total))

if 'livro' in produtos:
    i_livro = produtos.index('livro')
    total_antiga = produtos_ecommerce[i_livro][0] * produtos_ecommerce[i_livro][1]
    produtos_ecommerce[i_livro][1] = produtos_ecommerce[i_livro][1] * 1.1
    novo_total = produtos_ecommerce[i_livro][0] * produtos_ecommerce[i_livro][1]
    print("Vamos pagar de imposto a mais R${:,}".format(novo_total - total_antiga))