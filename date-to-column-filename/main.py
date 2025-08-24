from datetime import datetime as dt
import fnmatch
import glob
import os
import pandas as pd
import sys


EXPORT_DIR = "clean"


def prep_csv_for_dating(file, df_temp, date):
    print("PREPPING FOR DATING:", file)

    df = pd.read_csv(file)

    date = df.loc[0, "date"]
    date = pd.to_datetime(
        date,
        format="%m/%d/%Y"
    )

    print("The date this template was filled is", date)

    df.columns = df.iloc[1]

    df = df[2:].reset_index(drop=True)

    df["date"] = date
    col = df.pop("date")
    df.insert(0, "date", col)

    df_temp.append(df)


def ingest_path(path, df_temp, date):
    if os.path.isfile(path):
        if not fnmatch.fnmatch(path, "*.csv"):
            print(path, "is not a CSV file, you silly goose!")
        else:
            prep_csv_for_dating(path, df_temp, date)
        return

    if os.path.isdir(path):
        for file in glob.glob(os.path.join(path, "*.csv")):
            prep_csv_for_dating(file, df_temp, date)
        return

    print(path, "is not an existing path.")


def merge_csv(path, df_temp, date):
    df_merged = pd.concat(df_temp, ignore_index=True)

    date_string = date.strftime("%Y-%m-%d")

    file = f'cleaned_date_template_{date_string}.csv'

    df_merged.to_csv(
        os.path.join(EXPORT_DIR, file),
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
    date = dt.now()

    # Handles when 1 argument is passed
    if len(sys.argv) == 2:
        path = sys.argv[1]
        ingest_path(path, df_temp, date)
        merge_csv(path, df_temp, date)

    # Handles when more than 1 argument is passed
    if len(sys.argv) > 2:
        for path in sys.argv[1:]:
            ingest_path(path, df_temp, date)
            merge_csv(path, df_temp, date)


def main():
    parse_args()

    print("Processed all files!")


if __name__ == "__main__":
    main()
