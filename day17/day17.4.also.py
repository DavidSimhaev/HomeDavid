from superclassapi import GetFromApi


# https://datausa.io/api/data?drilldowns=Nation&measures=Population 

url = "https://datausa.io/api"
method = "data"
parameters = {'drilldowns': 'State', 'measures': 'Population', 'year': '2018'}

l = GetFromApi(url).addMethod(method=method, parameters=parameters).GetDataFromApi().GetValueFromKey("data")
print(l)