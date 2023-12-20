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
def renombrar (dataframe):
    new_column_names = dataframe.reset_index(drop=True).columns
    dataframe.columns = new_column_names
    return dataframe
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

    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas categóricas son: ")
    dataframe_categoricas = dataframe.select_dtypes(include = "O")
    for col in dataframe_categoricas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valore únicos:")
        display(pd.DataFrame(dataframe[col].value_counts()).head())
    
    return dataframe

#%%
def union (df_cliente, df_ventas, producto):
    df_union = df_cliente.merge(df_ventas, left_on="id", right_on="id_cliente")
    df_union.drop(columns=["id_cliente"], inplace=True)
    producto.rename(columns={'id': 'id_producto'}, inplace=True)
    df_final = df_union.merge(producto, on = "id_producto", how="left")
    df_final.to_csv("etl1.csv")

    return df_final
# %%
def modificar_col_products(dataframe, columna): 
    dataframe[columna].fillna('', inplace=True)
    return dataframe

#%%
def eliminar_nulos(dataframe, columna): 
    dataframe[columna] = dataframe[columna].fillna(dataframe[columna].mode()[0])
    return dataframe
#%%
def nulls_unknown(dataframe, lista_columnas):
    for columna in lista_columnas: 
        dataframe[columna]= dataframe[columna].fillna("unknown")
    return dataframe

# %%
def eliminar_columns_prod(dataframe, columna1, columna2, columna3):
    dataframe.drop(columns=[columna1, columna2], axis=1, inplace=True)
    dataframe.rename(columns={columna3: columna1}, inplace=True)
    return dataframe 



