class TextTable:
    def __init__(self,csv) -> None:    
        self.rows = []
        self.col_width = {}
        for row in csv.split('\n'):            
            self.rows.append(row.strip())
            cols = row.split(',')
            for i,col in enumerate(cols):            
                if i in self.col_width:
                    if self.col_width[i] < len(col):
                        self.col_width[i] = len(col)
                else:
                    self.col_width[i] = len(col)

        width = 0
        for k,v in self.col_width.items():
            width += v        
        self.max_col_width =  width + len(self.col_width) * 3 + 1 #Not sure about adding this 1, but it works

    def generate_table(self):
        table_output = ""        
        x = '-' * self.max_col_width
        for i,row in enumerate(self.rows):
            if not row:
                break
            cols = row.split(',')
            # print(f'{x:<{total_col_width(col_width)}}')
            table_output += f'{x:<{self.max_col_width}}' + "\n"
            for i,col in enumerate(cols):
                # print(f'| {col:<{col_width[i]}} ',end='')
                table_output += f'| {col:<{self.col_width[i]}} '
            # print("|",end='')
            table_output += "|"
            # print()
            table_output += "\n"

            # print(f'{x:<{total_col_width(col_width)}}')
        table_output += f'{x:<{self.max_col_width}}' + "\n"
        return table_output

