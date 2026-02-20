import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

#criando dados ficticios 
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100),
    'Stock A': [100 + i for i in range(100)],
    'Stock B': [120 - i for i in range(100)],
    'Stock C': [90 + (i *0.5) for i in range(100)]
}

df = pd.DataFrame(data)

#criando o grafico de linhas interarivo com o plotly 
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Stock A'],
        mode='lines',
        name='Stock A'
    )
)
fig.add_trace(
    go.Scatter(
    x=df['Date'],
    y=df['Stock B'],
    mode='lines',
    name='Stock B'
)
)
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Stock C'],
        mode='lines',
        name='Stock C'
    )
)

#configurando o layout do grafico
fig.update_layout(
    title='Preço das Ações ao Longo do Tempo', 
    xaxis_title='Data',
    yaxis_title='Preço',
    hovermode='x'
)

fig.show()