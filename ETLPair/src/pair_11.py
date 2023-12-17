#%%
import pandas as pd
import numpy as np
#%%
pd.set_option('display.max_columns', None)
# %%
df_clientes = pd.read_csv("clientes.csv", index_col = 0)
df_clientes.sample(5)
# %%
df_productos = pd.read_csv("productos.csv", index_col = 0)
df_productos.sample(5)
# %%
df_ventas = pd.read_csv("ventas.csv", index_col = 0)
df_ventas.sample(5)
# %%
df_clientes.shape[0] #filas
# %%
df_clientes.shape[1] #columnas
# %%
df_productos.shape[0]
# %%
df_ventas.shape[0]
#%%
def mayusculas (dataframe):
    dataframe.columns = map(str.lower, dataframe.columns)
    return dataframe
#%%
df_clientes = mayusculas(df_clientes)
df_productos = mayusculas(df_productos)
df_ventas = mayusculas(df_ventas)
# %%
def limpieza_tabla (dataframe):
    print(f"Duplicados: {dataframe.duplicated().sum()}")
    print("\n ..................... \n")

    print("Nulos:")
    df_nulos = pd.DataFrame(dataframe.isnull().sum() / dataframe.shape[0] * 100, columns = ["%_nulos"])
    display(df_nulos[df_nulos["%_nulos"] > 0])

    print("\n ..................... \n")
    print(f"Las columnas son:")
    display(pd.DataFrame(dataframe.dtypes, columns = ["tipo_dato"]))
    