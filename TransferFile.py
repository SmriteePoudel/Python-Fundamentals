def copy_file_content(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            dest.write(src.read())
        print(f"Content copied from {source_file} to {destination_file}")
    except FileNotFoundError:
        print("One of the files was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


source = "source.txt"
destination = "destination.txt"
copy_file_content(source, destination)
