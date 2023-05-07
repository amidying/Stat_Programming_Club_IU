student = {
    "Neaz" : 19,
    "Rabbi" : 14

}
student2 = {
    "Neaz" : ["Boroikuri","Mohanpur","Rajsahi","Unmarried"],
    "Rabbi": {
        "Village" : "xyz",
        "Roll" : 14,
        "Sex" : "Male",
        "Age" : 20.5,
        "Married" : False
    }
}
print(student["Neaz"])
print(student["Rabbi"])
print(student2["Neaz"])
print(student2["Rabbi"])

print(student.keys())
print(student.values())
print(student.items())
student["Neaz"] = False;
student.update({"Neaz": True})
print(student)