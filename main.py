import argparse

ap = argparse.ArgumentParser(description="Prints the csv file in tabular form")
ap.add_argument("-f", "--file", required=True, help="csv file")
args = vars(ap.parse_args())


def read_file():
    rows = []
    col_width = {}
    with open(args['file'],'r') as f:
        while True:
            row = f.readline().strip()
            rows.append(row)
            if not row:
                break
            
            cols = row.split(',')
            for i,col in enumerate(cols):            
                if i in col_width:
                    if col_width[i] < len(col):
                        col_width[i] = len(col)
                else:
                    col_width[i] = len(col)
    return rows,col_width

def total_col_width(col_width):
        width = 0
        for k,v in col_width.items():
            width += v
        
        return width + len(col_width) * 3 + 1 #Not sure about adding this 1

def run():
    rows, col_width = read_file()    
    x = '-' * total_col_width(col_width)
    for i,row in enumerate(rows):
        if not row:
            break
        cols = row.split(',')
        print(f'{x:<{total_col_width(col_width)}}')
        for i,col in enumerate(cols):
            print(f'| {col:<{col_width[i]}} ',end='')
        print("|",end='')
        print()

    print(f'{x:<{total_col_width(col_width)}}')


if __name__ == "__main__":
    run()
    
