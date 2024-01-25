import os

#welcome statement
print("Hello, this is your file renamer program.")

#choosing an amount of files
choice = input("Do you want to rename one file or many? ")

try:
  while True:
    if choice.lower() == "one":

        #taking paths to an old and a new file
        file = os.path.join(input("Type a file path: "))
        new_file = os.path.join(input("Type a new file path: "))
        #actual renaming
        os.rename(file, new_file)

    elif choice.lower() == "many":

        #warning
        print("Please make sure all of your files are in the same catalog.")
      
        #taking a path to a directory
        path_to_dir = os.path.join(input("Type a directory path: "))
      
        #choosing a name for all new files, only number at the end will be different
        name = input("Type a new name for your files: ")

        #a directory tree
        files = os.listdir(path_to_dir)
      
        #a loop counter
        i = 1

        #a loop to actually rename all files in directory
        for file in files:
            old_file_path = os.path.join(path_to_dir, file)
            new_file_path = os.path.join(path_to_dir, f'{name} {i}')
            os.rename(old_file_path, new_file_path)
            i += 1
          
    #handling invalid input
    else: 
      print("Invalid input.")
      break

#adding error handling
except FileNotFoundError as e:
    print(f"Error: {e}. Please check your file paths.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

  