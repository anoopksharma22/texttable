import argparse
ap = argparse.ArgumentParser()

ap.add_argument("-f", "--file", required=True, help="csv file")
args = vars(ap.parse_args())


class ColWidth:
    def __init__(self,col_width) -> None:
        self.col_width = col_width
    
    
    def total_col_width(self):
        width = 0
        for k,v in self.col_width.items():
            width += v
        
        return width + len(self.col_width) * 3 + 1

with open(args['file'],'r') as f:
    col_width = {}
    rows = []
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

    colw = ColWidth(col_width)
    x = '-' * colw.total_col_width()
    for i,row in enumerate(rows):
        if not row:
            break
        cols = row.split(',')
        print(f'{x:<{colw.total_col_width()}}')
        for i,col in enumerate(cols):
            print(f'| {col:<{col_width[i]}} ',end='')
        print("|",end='')
        print()
    
    print(f'{x:<{colw.total_col_width()}}')
