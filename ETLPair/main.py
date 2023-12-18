#%%
import pandas as pd
import numpy as np
from src import pair_11 as pair
#%%
df_clientes = pd.read_csv('src/clientes.csv')
df_productos = pd.read_csv('src/productos.csv')
df_ventas = pd.read_csv('src/ventas.csv')
#%%
clientes_mayus = pair.mayusculas(df_clientes)
productos_mayus = pair.mayusculas(df_productos)
ventas_mayus = pair.mayusculas(df_ventas)
#%%
productos = df_productos.pair.renombrar
# %%
df_productos.sample(5)
# %%
