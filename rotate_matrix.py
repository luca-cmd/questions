Matrix = list[list[int]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


class Main:
    def __init__(self, matrix: Matrix) -> None:
        self.matrix = matrix
        self.rotation = 0
        self.position = [
            [[2, 0], [1, 0], [0, 0]],
            [[2, 1], [1, 1], [0, 1]],
            [[2, 2], [1, 2], [0, 2]],
        ]

    def rotate_board(self):
        new_matrix: Matrix = []
        for _ in range(self.rotation):
            for i in range(len(self.matrix)):
                line: list[int] = []
                for v in range(3):
                    line.append(
                        self.matrix[self.position[i][v][0]][self.position[i][v][1]]
                    )
                new_matrix.append(line)
            self.matrix = new_matrix
            new_matrix = []

    def print_board(self):
        for i in self.matrix:
            print("\n-------------\n|", end="")
            for x in i:
                print(f" {x} ", end="|")
        print("\n-------------")

    def start(self):
        while True:
            self.print_board()
            self.rotation = int(
                int(input("how much you want to rotate the matrix -> ")) / 90
            )
            self.rotate_board()


if __name__ == "__main__":
    main = Main(matrix=matrix)
    main.start()
