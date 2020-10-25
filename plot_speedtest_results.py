import plotly.express as px
import pandas as pd


df = pd.read_csv('speedtest_results.csv')
fig = px.line(df, x="date", y=['download', 'upload'], title='Speedtest results')
fig.show()
