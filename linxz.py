# -*- coding: utf-8 -*-
import sys
import re
import os
import shutil

def get_special_paths(dirname):
    files_list=[]  
      
    for root, sub_dirs, files in os.walk(dirname):  
        for special_file in files:  
            if special_file.find('__w__')<>-1:  
                files_list.append(os.path.join(root,special_file))    
                            
    return files_list

  
def copy_to(paths, to_dir):
    for file in paths:
        fileName = os.path.basename(file)  
        destPath = to_dir + os.path.sep + fileName
        if os.path.exists(to_dir):
            pass
        else:
            os.mkdir(to_dir)
        if os.path.exists(file) and not os.path.exists(destPath):
            shutil.copyfile(file, destPath)

def main():
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir] dir [dir ...]";
        sys.exit(1)
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]
    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)   # Gather all the special files
    paths = []
    for dirname in args:
        print dirname
        paths.extend(get_special_paths(dirname))
        print paths
        if todir:
            copy_to(paths, todir)
        else:
            print '\n'.join(paths)
if __name__ == "__main__":
    main()
