def filehandling_funcs():


    with open('file.txt', 'r') as file:
        read_content = file.read()
        print(read_content)

    with open('file.txt','a') as file:

        write_content = input("enter the content you want to enter in the file")
        file.write(write_content)

    with open("file.txt","r") as file:
        partial_content = file.read(len(file.__sizeof__(file))/2)
        print(partial_content)

    with open("file.txt", "r") as file:
        content = [""]
        for line in file:
            content[line] = file.readline(line).strip
            
        for index in content:
            print(content[index])


def main():
    filehandling_funcs()

if __name__ == "__main__":
    main()
