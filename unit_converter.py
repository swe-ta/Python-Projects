with open("units_length.txt", "r") as f:
    lines = f.readlines()

print("Unit Converters:")
print("------------------------")
print("1. Length Conversion")
print("2. Weight Conversion")
print("3. Volume Conversion")

choice = int(input("Choose a conversion (1-3): "))

if choice == 1:
    lengthDict = {}
    for line in lines:
        parsed = line.strip().split("\t")
        lengthDict[parsed[0]] = parsed[1]

print(lengthDict)
unit = int(input("Enter unit:"))
print("Enter the unit you want to convert to: ",lengthDict.keys())
[print(item) for item in (lengthDict.keys())]
length = input("Please enter one of these!")
print(f"{unit} is equal to {unit *(lengthDict[length])} {length}")







