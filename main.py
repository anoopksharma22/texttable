import argparse
ap = argparse.ArgumentParser()

ap.add_argument("-f", "--file", required=True, help="csv file")
args = vars(ap.parse_args())

class TextTable:
    def __init__(self,rows):
        self.rows = rows
        self.total_no_colums = len(self.rows[0].split(","))
        self.space_between = 2
        self.width_border_length = self.get_longest_row_lenght() + self.space_between * self.total_no_colums + self.total_no_colums + 1

    def __repr__(self):
        return(f"{self.rows}")
    
    def generate_table(self):
        print('-' * self.width_border_length)
        for row in self.rows:
            for col in row.split(","):
                print('|','' * self.space_between,col.strip(), '' * self.space_between,end="")
            print('' * self.space_between,'|',end='')
            print()
            print('-' * self.width_border_length)
    def get_longest_row_lenght(self):
        longest_row = max(self.rows,key=len)
        return len(longest_row)


def run():
    headers = None
    rows = []
    with open( args['file'], 'r') as f:        
        while True:
            row = f.readline().strip()
            if not row:
                break
            rows.append(row)
    text_table = TextTable(rows)
    print(text_table.total_no_colums)
    print(text_table.width_border_length)
    text_table.generate_table()

if __name__ == "__main__":
    run()