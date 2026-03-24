from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

df = extract_data()
df = transform_data(df)
load_data(df)

print("ETL pipeline executed successfully!")
