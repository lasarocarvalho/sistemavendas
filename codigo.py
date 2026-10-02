# titulo - Sistema de Vendas
# Seção Cadastrar Vendas
    # Campo Data
    # Campo Vendedor - Ana, Bruno, Carla
    # Campo Produto - Notebook, Celular, Fone
    # Campo Quantidade  
    # Campo Valor
    # Botão Cadastrar Venda
        # Quando o botão for clicado, a venda deve ser salva na base de dados (arquivo CSV) e uma mensagem de sucesso deve ser exibida
# Seção Vendas Cadastradas
    # Tabela com as vendas cadastradas
# Seção Dashboard
    # Card/Métrica com o faturamento total
    # Gráfico de Barras/Coluna -> Venda por vendedor
    # Gráfico de pizza -> Venda por produto

# pip install streamlit pandas plotly
# python -m streamlit run codigo.py

import streamlit as st
import pandas as pd
import plotly.express as px

# carregar a base de dados
tabela = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

# Seção Cadastrar Vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao = st.sidebar.button("Cadastrar Venda")

# logica de cadastro
if botao:
    if valor<=0:
        st.error("O valor da venda deve ser maior que zero!")
    else:        
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela)
        tabela.loc[ultima_linha] = nova_venda
        tabela.to_csv("vendas.csv", index=False)
        print(nova_venda)
        st.success("Venda cadastrada com sucesso!") 

# Seção Vendas Cadastradas
st.write("## Vendas Cadastradas")
st.dataframe(tabela)

# Seção Dashboard
st.write("## Dashboard")

# Card/Métrica com o faturamento total
faturamento = tabela["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")

# Gráfico de Barras/Coluna -> Venda por vendedor
grafico1 = px.bar(tabela, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)


# Gráfico de pizza -> Venda por produto
grafico2 = px.pie(tabela, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)