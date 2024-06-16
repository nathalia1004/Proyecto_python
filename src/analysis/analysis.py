import pandas as pd
import os
from ..decorators.decorators import timeit, logit

@logit
@timeit

def load_data(data_path):
    
    if data_path.endswith(".csv"):
        df=pd.read_csv(data_path)
    elif data_path.endswith("xlsx"):
        df = pd.read_excel(data_path)
    else:
        raise ValueError("Unsopported fiel format")
    print("Data loaded successfully")
    
    return df 

#print(load_data("data/raw/products.csv"))
@logit
@timeit
def clean_data(df):
    df["price"]= df["price"].replace(r"[\$,]", "", regex= True).astype(float)
    
    print("data cleaned Successfully")
    return df

@logit
@timeit
def analyze_data(df):
    print("Basic Data Analysis: ")
    print(df.describe())
    print("\nProducts with highest prices: ")
    highestPrices= df.nlargest(5,"price")
    print(highestPrices)
    
    return highestPrices

@logit
@timeit
def save_clean_data(df,outputh_path):
    if outputh_path.endswith(".csv"):
        df.to_csv(outputh_path, index=False)
    elif outputh_path.endswith(".xlsx"):
        df.to_excel(outputh_path, index=False)
    else:
        raise ValueError("Usopported file formart")
    
    print(f"Clean data saved to {outputh_path}")
    
if __name__ == "__main__":
    data_path ="data/raw/products.csv"
    outhputh_path = "data/processed/cleaned_products.csv"
    
    df =load_data(data_path)
    df =clean_data(df)
    
    df = analyze_data(df)
    os.makedirs("data/processed", exist_ok=True)
    
    save_clean_data(df, outhputh_path) #Guardamos los datos limpios en el archivo específico