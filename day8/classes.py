class Matrix:
    data = []

    def __init__(self, lines):
        for line in lines:
            chars = list(line)
            self.data.append(chars)

    def get_value(self, row, col):
        if row > len(self.data) or row < 0:
            return None

        line = self.data[row]
        if col > len(line) or col < 0:
            return None

        char = line[col]
        return int(char)

    def get_row(self, row):
        if row > len(self.data) or row < 0:
            return None
        return self.data[row]

    def get_num_rows(self):
        return len(self.data)

    # assumes all rows same size
    def get_num_cols(self):
        row = self.data[0]
        return len(row)