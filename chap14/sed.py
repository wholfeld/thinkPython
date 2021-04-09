import sys
from os.path import dirname, join

def sed():
    if len(sys.argv) < 5:
        print("not enough args")
        return

    search_word = sys.argv[1]
    replacement_word = sys.argv[2]
    read_file = sys.argv[3]
    write_file = sys.argv[4]
    current_dir = dirname(__file__)
    read_file = join(current_dir, "./" + read_file)
    write_file = join(current_dir, "./" + write_file)

    with open(read_file, "r") as rf:
        with open(write_file, "w+") as wf:
            while True:
                line = rf.readline()
                if not line:
                    break
                wf.write(line.replace(search_word, replacement_word))

sed()