
file_list = ['file1.txt', 'file2.txt', 'file3.txt']  


output_file = 'merged_file.txt'


with open(output_file, 'w') as outfile:
    for filename in file_list:
        with open(filename, 'r') as infile:
            for line in infile:
                outfile.write(line)  

print(f"Files merged successfully into '{output_file}'")
