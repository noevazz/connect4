class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def clamp(num, min_value, max_value):
    num = max(min(num, max_value), min_value)
    return num

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
                    print("□  ", end="")
            print()
    
    def add_item(self, item: int, pos_at_x: int) -> str:
        column_sum = sum([ abs(row[pos_at_x]) for row in self.matrix])
        if column_sum == self.height:
            return "notpossible" # not possible
        post_at_y = self.height-1-column_sum        
        self.matrix[post_at_y][pos_at_x] = item
        if self.check_diagonal_backslash(pos_at_x, post_at_y, item) == "win":
            return "win"
        #if self.check_diagonal_forwardslash(pos_at_x, post_at_y, item) == "win":
        #    return "win"
        if self.check_horizontal(post_at_y, item) == "win":
            return "win"
        if self.check_vertical(pos_at_x, item) == "win":
            return "win"
        return "ok" # no issues

    def check_vertical(self, pos_at_x, check_value) -> str:
        next_to_y_origin = Vector2(pos_at_x, 0)
        counter = 0
        for i in range(self.height):
            value_at_this_pos = self.matrix[next_to_y_origin.y+i][next_to_y_origin.x]
            if value_at_this_pos == check_value:
                counter += 1
                if counter == 4:
                    return "win"
            else:
                counter = 0
    
    def check_horizontal(self, pos_at_y, check_value) -> str:
        next_to_y_origin = Vector2(0, pos_at_y)
        counter = 0
        for i in range(self.width):
            value_at_this_pos = self.matrix[next_to_y_origin.y][next_to_y_origin.x+i]
            if value_at_this_pos == check_value:
                counter += 1
                if counter == 4:
                    return "win"
            else:
                counter = 0
    
    def check_diagonal_backslash(self, pos_at_x, post_at_y, check_value) -> str:
        next_to_y_origin = Vector2(0, post_at_y-pos_at_x)
        print("x", next_to_y_origin.x, ", y", next_to_y_origin.y)
        counter = 0
        for i in range(self.height-next_to_y_origin.y):
            print("i", i)
            print(self.matrix)
            if next_to_y_origin.x+i == self.width:
                break
            value_at_this_pos = self.matrix[next_to_y_origin.y+i][next_to_y_origin.x+i]
            if value_at_this_pos == check_value:
                counter += 1
                if counter == 4:
                    return "win"
            else:
                counter = 0
            print(">>>>", self.matrix[next_to_y_origin.y+i][next_to_y_origin.x+i], end="")
            print()
        return None
    
    def check_diagonal_forwardslash(self, pos_at_x, pos_at_y, check_value) -> str: # WIP
        clamp_x = clamp(pos_at_x+pos_at_y, pos_at_x, self.width-1)
        next_to_x_origin = Vector2(clamp_x, 0)
        print("pos_at_x", pos_at_x, "pos_at_y", pos_at_y)
        print("x", next_to_x_origin.x, ", y", next_to_x_origin.y)
        counter = 0
        for i in range(self.height):
            print("i", i)
            print(self.matrix)
            if next_to_x_origin.x-i == -1:
                break
            value_at_this_pos = self.matrix[next_to_x_origin.y+i][next_to_x_origin.x-i]
            if value_at_this_pos == check_value:
                counter += 1
                if counter == 4:
                    return "win"
            else:
                counter = 0
            print(">>>>", self.matrix[next_to_x_origin.y+i][next_to_x_origin.x-i], end="")
            print()
        return None



if __name__ == "__main__":
    B = Board(6,8)
    B.draw_dashboard()
    player = 1 # player1=1, player2=-1
    while(True):
        print("Player", "•" if player==1 else "∘", end=" ")
        item_pos = int(input("position: "))
        new_item = B.add_item(player, item_pos)
        if new_item == "notpossible":
            print("!!!Not possible!!!\n")
        elif new_item == "win":
            B.draw_dashboard()
            print("Wohoo! we have a winner,", "Player", "•" if player==1 else "∘")
            break
        else:
            player *= -1
            B.draw_dashboard()

