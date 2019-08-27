animals_in_kennel = [
    {
        "id": 1,
        "breed": "German Shepherd",
        "age": 3,
        "name": "Jack"
    },
    {
        "id": 2,
        "breed": "Siamese",
        "age": 9,
        "name": "Shy"
    },
    {
        "id": 3,
        "breed": "Labradoodle",
        "age": 5,
        "name": "Avett"
    },
    {
        "id": 4,
        "breed": "Shnauzer",
        "age": 1,
        "name": "Gypsy"
    },
]

print("Regular for loop version:")

# loop over list of dicts
for animal in animals_in_kennel:
    # inside of each dog dict, loop over the KVP to print to console
    for key, value in animal.items():
        print(f'Key "{key}": {value}')

# now doing with a comprehension
print("------------------------")
print("Comprehension Version:")


dog_data = [print(f'Key "{key}": {value}')
            for animal in animals_in_kennel for key, value in animal.items()]
