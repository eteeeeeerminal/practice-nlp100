import json

with open("jawiki-country.json") as f:
    data = f.read()

article_data_list = data.split("\n")
article_dict_list = [json.loads(data) for data in article_data_list if data]

britain_data = list(filter(lambda x: x["title"] == "イギリス", article_dict_list))
print(britain_data[0]["text"])