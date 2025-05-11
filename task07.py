try:
    with open('sample.txt', 'r') as file:
        print("File content:")
        for line in file:
            print(line.strip())  
except FileNotFoundError:
    print("Error: 'sample.txt' not found. Please check the file name or path.")
