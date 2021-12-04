

file_name = 'input.txt'
numbers = []
boards = []

def main():
    with open(file_name, 'r') as input:
        numbers_input = input.readline()
        numbers = [int(number.strip('\n')) for number in numbers_input.split(',')]
        while True:
            line = input.readline()
            if not line:
                break
            elif line == "\n":
                continue
            else:
                board = []
                board_line = [[int(num.strip(' ')),False] for num in line.split(' ') if     num != '']
                board.append(board_line)
                for i in range(len(board_line)-1):
                    line = input.readline()
                    board_line = [[int(num.strip(' ')),False] for num in line.split(' ')    if num != '']
                    board.append(board_line)
            boards.append([board,False])

    for bingo_num in numbers:
        one_left = False
        last_num = -1
        if [board[1] for board in boards].count(False) == 1:
            one_left = True
            for i,board in enumerate(boards):
                if board[1] == False:
                    last_num = i
        for board in boards:
            for board_line in board[0]:
                for board_item in board_line:
                    if board_item[0] == bingo_num:
                        board_item[1] = True
        for i,board in enumerate(boards):
            for board_line in board[0]:
                if all([board_item[1] for board_item in board_line]):
                    board[1] = True
                    if one_left and last_num == i:
                        sum = 0
                        for board_line in board[0]:
                            for board_item in board_line:
                                if board_item[1] == False:
                                    sum += board_item[0]
                        return sum*bingo_num
            for column in range(len(board[0][0])):
                if all([row[column][1] for row in board[0]]):
                    board[1] = True
                    if one_left and last_num == i:
                        sum = 0
                        for board_line in board[0]:
                            for board_item in board_line:
                                if board_item[1] == False:
                                    sum += board_item[0]
                        return sum*bingo_num


if __name__ == "__main__":
    print(main())