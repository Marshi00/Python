try:
    file = open("a_file.txt", "a")
    file.write("1233")
    a_dict = {"key": "value"}
    print(a_dict["2323"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("tte")
except KeyError as error_msg:
    print(f"The key {error_msg} does not exist.")
# Run only when try successfully run
else:
    content = file.read()
    print(content)
# Run no matter what
finally:
    file.close()
    print("file was closed")
    height = float(input("Height"))
    if height > 3:
        raise ValueError("human height should not be over 3 meters.")
