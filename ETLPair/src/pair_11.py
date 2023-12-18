#%%
import pandas as pd
import numpy as np
import os 
import sys 
#%%
pd.set_option('display.max_columns', None)
#%%
def mayusculas (dataframe):
    dataframe.columns = map(str.lower, dataframe.columns)
    return dataframe
#%%
def renombrar (df_productos):
    df_productos = df_productos.reset_index(drop=True)
    return df_productos
#%%
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
    
# %%
