import fnmatch
import glob
import os
import pandas as pd
import sys


EXPORT_DIR = "clean"


def process_csv(file):
    print("PROCESSING:", file)

    try:
        df = pd.read_csv(file)

        df.to_csv(
            os.path.join(EXPORT_DIR, os.path.basename(file)),
            encoding='utf-8',
            index=False,
            header=True
        )
    except Exception as err:
        print("ERROR:", file, "not processed --", err)


def ingest_path(path):
    if os.path.isfile(path):
        if not fnmatch.fnmatch(path, "*.csv"):
            print(path, "is not a CSV file, you silly goose!")
        else:
            process_csv(path)
        return

    if os.path.isdir(path):
        for file in glob.glob(os.path.join(path, "*.csv")):
            process_csv(file)
        return

    print(path, "is not an existing path.")


def parse_args():
    # Exits when no argument is passed
    if len(sys.argv) < 2:
        sys.exit("ERROR: No file was passed. Please pass a file to continue.")

    # in case of any file processing, confirm the state of the export directory
    if not os.path.isdir(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)

    # Handles when 1 argument is passed
    if len(sys.argv) == 2:
        path = sys.argv[1]
        ingest_path(path)

    # Handles when more than 1 argument is passed
    if len(sys.argv) > 2:
        for path in sys.argv[1:]:
            ingest_path(path)


def main():
    parse_args()

    print("Processed all files!")


if __name__ == "__main__":
    main()
