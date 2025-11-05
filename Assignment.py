import sys

my_file_path = r"C:\Users\phatt\Documents\Nw\Security\Security Engineer ARIT\Input.txt"

def read_file(path_to_file):
    try:
        with open(path_to_file, mode='r', encoding='utf-8') as f:
            content = f.read()
            
        return content
    
    except Exception as e:
        
        print("Cant' Open file")
    
    return None

data = read_file(my_file_path)

if data is not None:
    print(data)