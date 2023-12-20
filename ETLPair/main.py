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
productos = pair.renombrar(df_productos)
productos
# %%
clientes_limpieza = pair.limpieza_tabla(df_clientes)
productos_limpieza = pair.limpieza_tabla(productos)
ventas_limpieza = pair.limpieza_tabla(df_ventas)
# %%
clientes_limpieza.sample(5)
# %%
productos.sample(5)
#%%
ventas_limpieza.sample(5)

df_juntos = pair.union(df_ventas, df_clientes, productos)
df_juntos

# %%
