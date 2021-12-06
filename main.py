import os

'''
    For the given path, get the List of all files in the directory tree 
'''


def getlist_of_files(dir_name, output_dir):

    contents = os.listdir(dir_name)
    print(contents)
    list_of_dirs = ''
    list_of_files = ''

    for entry in contents:
        # Create full path
        full_path = os.path.join(dir_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            list_of_dirs += entry
            list_of_dirs += 'brahma \n putra \n'
            os.mkdir(os.path.join(output_dir, entry))
            getlist_of_files(full_path, os.path.join(output_dir, entry))
        else:
            list_of_files += entry
            list_of_files += 'files\n filesfjfj \n'

    html_name = os.path.join(output_dir, os.path.basename(dir_name)+'.html')
    file1 = open(html_name, 'w', encoding="utf-8")
    to_file = ''
    to_file = to_file + list_of_dirs + list_of_files
    file1.write(to_file)
    file1.close()

def main():
    dir_name = r"C:\Users\Marik\Dropbox\Site"
    output_dir = r"D:\Documents\Programming\output"
    getlist_of_files(dir_name, output_dir)
    print('ogi\nogi')

if __name__ == '__main__':
    main()
