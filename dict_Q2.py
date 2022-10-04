sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys_to_remove = ["name", "salary"]
for item in keys_to_remove:
    if item in sample_dict:
        del sample_dict[item]

print(sample_dict)
