import pandas as pd
import json


#file = open('data/Stacje.json')
#json_object = json.load(file)
#print(json_object)

with open('data/Stacje.json') as file:
    data = json.load(file)


    processed_dict = data['data']
    df = pd.DataFrame(processed_dict)
    print(df)
