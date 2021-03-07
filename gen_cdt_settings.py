"""
    Tool for generating Eclipse CDT includes settings XML file.

    usage: gen_cdt_settings.py [-h] [-v] [-r path] [--ignore-c] [--ignore-cpp] out_file

    positional arguments:
      out_file       specify the output file filename

    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  turn on verbose mode
      -r, --relative turn on relative mode with the given path as the root
      --ignore-c     ignore C header files
      --ignore-cpp   ignore C++ header files
"""

if __name__ == "__main__":
    import argparse
    import cig
    import os
    import pathlib

    parser = argparse.ArgumentParser(description='Generate includes settings for Eclipse CDT project.')
    parser.add_argument('out_file', help='specify the output file filename')
    parser.add_argument('-v', '--verbose', help='turn on verbose mode', action="store_true")
    parser.add_argument('-r', '--relative', type=pathlib.Path,
                        help='turn on relative mode with the given path as the root')
    parser.add_argument('--ignore-c', help='ignore C header files', action="store_true")
    parser.add_argument('--ignore-cpp', help='ignore C++ header files', action="store_true")
    args = parser.parse_args()   

    if args.ignore_c :
        print("Skipping C header files.")
        hFolders = set()
    else:
        print("Searching for C header files.")
        hFolders = cig.folders(os.getcwd(), ['.h']) 
    if args.ignore_cpp :
        print("Skipping C++ header files.")
        hppFolders = set()
    else:
        print("Searching for C++ header files.")
        hppFolders = cig.folders(os.getcwd(), ['.hpp']) 

    if args.verbose:
        print(f'C includes paths({len(hFolders)}):')
        for folder in hFolders:
            print(f'\t{folder}')
        print(f'C++ includes paths({len(hppFolders)}):')
        for folder in hppFolders:
            print(f'\t{folder}')

    print(f'Writing settings file to {args.out_file}.')
    cig.generateXML(args.out_file, hFolders, hppFolders, args.relative)
    print('Done.')


