import os, sys

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
                print(".",end='')
    return total_size

def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
    while size > power:
        size /= power
        n += 1
    return size, power_labels[n]+'bytes'


def usage():
    print("> python size-of-tree-of-folders.py [folder]")
    print("Sample of folder: '/home/john/test'")
    sys.exit()

    
def main():
    if len(sys.argv) == 1:
        usage()
        # Example usage
    directory_path = sys.argv[1]
    total_size = get_directory_size(directory_path)
    size, power = format_bytes(total_size)
    print(f"\nTotal size of directory '{directory_path}':\n=> {round(size, 1)} {power}")

   
if __name__ == "__main__":
    main()
        
