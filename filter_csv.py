import argparse
import csv


def main():
    parser = argparse.ArgumentParser(
        description="Print the rows of a CSV where a column has a given value.")
    parser.add_argument("filename", help="the CSV file to read")
    parser.add_argument("column", help="the name of the column to match on")
    parser.add_argument("value", help="the value to match")

    args = parser.parse_args()
    
    
        # TODO: open args.filename and read it with csv.reader. The first row is the
    #   header. Find the position of args.column within the header, then print every
    #   data row (its values joined by commas) whose value in that column equals
    #   args.value.
    
    with open(args.filename) as file:
        reader = csv.reader(file)
        rows = list(reader)
        
    header = rows[0]
    column_index = header.index(args.column)
    
    for row in rows[1:]:
        if row[column_index] == args.value:
            print(",".join(row))
        




if __name__ == "__main__":
    main()
