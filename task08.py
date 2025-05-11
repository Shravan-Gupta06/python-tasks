text1 = input("Enter text to write to the file: ")
try:
    with open("output.txt", "w") as file:
        file.write(text1 + "\n")
    print("Data successfully written to output.txt.")
except Exception as e:
    print("An error occurred while writing to the file:", e)


text2 = input("\nEnter additional text to append: ")
try:
    with open("output.txt", "a") as file:
        file.write(text2 + "\n")
    print("Data successfully appended.")
except Exception as e:
    print("An error occurred while appending to the file:", e)

print("\nFinal content of output.txt:")
try:
    with open("output.txt", "r") as file:
        for line in file:
            print(line.strip())
except Exception as e:
    print("An error occurred while reading the file:", e)
