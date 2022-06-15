class Board:
    def __init__(self, width, height):
        self.width  :int = width
        self.height :int = height
        self.matrix :list(list()) = [[0 for x in range(self.width)] for y in range(self.height)]
    
    def draw_dashboard(self):
        print([x for x in range(self.width)], end="\n\n")
        for row in self.matrix:
            print(" ", end="")
            for item in row:
                if item == 1:
                    print("•  ", end="")
                elif item == -1:
                    print("∘  ", end="")
                else:
                    print("⎕  ", end="")
            print()
                    

    
    def add_item(self, item: int, pos_at_x: int):
        column_sum = sum([ abs(row[pos_at_x]) for row in self.matrix])
        if column_sum == self.height:
            print("Not possible")
        self.matrix[self.height-1-column_sum][pos_at_x] = item


if __name__ == "__main__":
    B = Board(6,8)
    B.draw_dashboard()
    player = 1 # player1=1, player2=-1
    while(True):
        print("Player", "1" if player==1 else "2", end=" ")
        item_pos = int(input("position: "))
        B.add_item(player, item_pos)
        player *= -1
        B.draw_dashboard()

