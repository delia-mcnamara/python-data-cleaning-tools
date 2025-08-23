import fnmatch
import glob
import os
import pandas as pd
import sys


EXPORT_DIR = "clean"


def prep_csv_for_merge(file, df_temp):
    print("PREPPING FOR MERGE:", file)

    try:
        df = pd.read_csv(file)
        df_temp.append(df)
    except Exception as err:
        print("ERROR:", file, "not appended --", err)


def ingest_path(path, df_temp):
    if os.path.isfile(path):
        if not fnmatch.fnmatch(path, "*.csv"):
            print(path, "is not a CSV file, you silly goose!")
        else:
            prep_csv_for_merge(path, df_temp)
        return

    if os.path.isdir(path):
        for file in glob.glob(os.path.join(path, "*.csv")):
            prep_csv_for_merge(file, df_temp)
        return

    print(path, "is not an existing path.")


def merge_csv(path, df_temp):
    df_merged = pd.concat(df_temp, ignore_index=True)

    # FIX: what happens if `newname` includes `/`?
    newname = os.path.basename(path)

    df_merged.to_csv(
        os.path.join(EXPORT_DIR, newname),
        encoding='utf-8',
        index=False,
        header=True
    )


def parse_args():
    # Exits when no argument is passed
    if len(sys.argv) < 2:
        sys.exit("ERROR: No file was passed. Please pass a file to continue.")

    # in case of any file processing, confirm the state of the export directory
    if not os.path.isdir(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)

    df_temp = []

    # Handles when 1 argument is passed
    if len(sys.argv) == 2:
        path = sys.argv[1]
        ingest_path(path, df_temp)
        merge_csv(path, df_temp)

    # Handles when more than 1 argument is passed
    if len(sys.argv) > 2:
        for path in sys.argv[1:]:
            ingest_path(path, df_temp)
            merge_csv(path, df_temp)


def main():
    parse_args()

    print("Processed all files!")


if __name__ == "__main__":
    main()
