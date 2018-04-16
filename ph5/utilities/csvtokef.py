import csv
import argparse
from datetime import datetime

PROG_VERSION = "2017.257"

def get_args():
    parser = argparse.ArgumentParser(
            description='Converts a csv generated by keftocsv to a kef file.',
            usage=('Version: {0} keftocsv '
                   '--file="kef_file" '.format(PROG_VERSION))
            )
    parser.add_argument("-f", "--file", action="store",
                        required=True, type=str, metavar="file")
    parser.add_argument("-o", "--outfile", action="store",
                    required=True, type=str, metavar="outfile")
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    with open(args.file, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        kef_dict_list = [row for row in reader]
    with open(args.outfile, 'w') as keffile:
        # write kef header
        keffile.write(
           "#\n"
           "#    {0}\n"
           "#\n".format(datetime.now())
        )
        row_index = 1
        for kef_dict in kef_dict_list:
            keffile.write("#   Table row {0}\n".format(row_index))
            keffile.write("{0}\n".format(kef_dict['table']))
            for key in reader.fieldnames:
                if key != 'table':
                    keffile.write("    {0}={1}\n".format(key, kef_dict[key]))
            row_index += 1

if __name__ == "__main__" :
    main()
