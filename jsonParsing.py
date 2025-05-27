import json

courses = '{"name":"SurajKhopkar","language":["Java","Python"]}'

# loads is used to parse a json string to dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])

# to get first language taught by trainer i.e. java

list_languages = dict_courses['language']
print(list_languages[0])

