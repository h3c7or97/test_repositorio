import pandas as pd

frame_data = {
    'Nombre': ['Hector', 'Daniela', 'Erick'], 
    'Edad': [24, 24, 28], 
    'Cargo': ['Assistant', 'Manager', 'Clerk']
    }

df = pd.DataFrame(frame_data)
print(df)