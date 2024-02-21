import json



#dict

person_string = '{"name":"Ali","Languages":["python","c#"]}'
person_dict = {"name":"Ali","languages":["Python","C#"]}
# result = person["name"]
# result = person["Languages"]
# result = person["Languages"][0]

#JSON string to Dict
# result= json.loads(person_string)
# result = result["name"]
# result = result["Languages"]

# with open("person.json") as f:
#     data=json.load(f)
#     print(data)
#     print(data["name"])
#     print(data["Languages"])


# #Dict to JSON string
# result = json.dumps(person_dict)
# print(type(result))
# with open("person.json","w")as f:
#     json.dump(person_dict,f)

person_dict=json.loads(person_string)
result = json.dumps(person_dict,indent=4,sort_keys=True)

print(person_dict)
print(result)


