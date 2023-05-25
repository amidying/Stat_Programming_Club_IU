


with open("table.txt","a") as f:
    for i in range(2,21):
        f.write(f"The following table is for {i}")
        f.write("\n")
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}")
            f.write("\n")
        