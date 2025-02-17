# Simulador de Impacto Tributário em E-commerce

Um script Python que simula e analisa o impacto de mudanças tributárias em produtos de e-commerce, com foco especial no setor de livros.

## 🎯 Funcionalidades

- Análise de impacto em diferentes produtos de e-commerce
- Cálculo automático da diferença tributária
- Simulação de cenários com aumento de 10% nos preços
- Formatação de valores monetários para melhor visualização

## 📊 Dados Simulados

O script trabalha com dois conjuntos principais de dados:
- Lista de produtos diversos (eletrônicos, livros, etc.)
- Métricas de vendas (quantidade e preço por produto)

## 💻 Exemplo de Uso

```python
# Dados de exemplo
produtos = ['computador', 'livro', 'tablet', ...]
produtos_ecommerce = [
    [10000, 2500],  # [quantidade, preço]
    [50000, 40],
    # ...
]

# O script automaticamente:
# 1. Identifica produtos específicos (ex: livros)
# 2. Calcula o impacto do aumento tributário
# 3. Mostra a diferença no valor total
```

## 🔍 Resultado

O script fornece:
- Valor total de vendas atual
- Novo valor após mudança tributária
- Diferença a ser paga em impostos

## 🚀 Como usar

1. Defina sua lista de produtos
2. Adicione os dados de vendas [quantidade, preço]
3. Execute o script
4. Analise o impacto tributário nos resultados

## 📝 Notas

- Os valores são formatados com separadores de milhar para melhor leitura
- O aumento simulado é de 10% sobre o preço atual
- Facilmente adaptável para diferentes porcentagens de aumento
