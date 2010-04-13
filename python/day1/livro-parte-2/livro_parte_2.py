# encoding: utf-8
import sys
import os

def file_stat(filename):
    # initialization
    line_count, char_count, word_count = 0, 0, 0
    
    # read file content
    with open(filename, 'r') as f:
        for line in f:
            line_count += 1
            char_count += len(line)
            word_count += len(line.split())

    return char_count, line_count, word_count

def read_csv(filename):
    import csv
    
    rows = []
    try:
        reader = csv.reader(open(filename, 'r'))
        for row in reader:
             rows.append(tuple(row))
    except Exception as e:
        print e
        sys.exit()

    return rows

class MyException(Exception):
    pass

def diff_dirs(dirA, dirB):
    def content_is_different(fileA, fileB):
        from hashlib import md5
        return md5(open(fileA, 'r').read()).hexdigest() != \
               md5(open(fileB, 'r').read()).hexdigest()
    
    # list files
    filesA = set(os.listdir(dirA))
    filesB = set(os.listdir(dirB))
    
    unique_files = (filesA - filesB).union(filesB - filesA)
    common_files = filesA.intersection(filesB)

    files = list(unique_files)

    for f in common_files:
        fileA = os.path.join(dirA, f)
        fileB = os.path.join(dirB, f)
        if content_is_different(fileA, fileB):
            files.append(f)
    
    return sorted(files)

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print 'diff directories'
  dir1 = os.path.join(os.path.dirname(__file__), 'exec5', 'dir1')
  dir2 = os.path.join(os.path.dirname(__file__), 'exec5', 'dir2')
  test(diff_dirs(dir1, dir2),
    ['file2.txt', 'file3.txt', 'other_content.txt'])

  print 'file stats'
  test(file_stat('exec1.txt'), (26, 4, 4))
  
  print 'read csv'
  test(read_csv('exec3.txt'),
    [
        ('henrique', 'dos', 'santos', 'bastos'),
        ('cristiane', 'da', 'cruz', 'monteiro')
    ]
  )

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()