import re
file_name = 'input.txt'
input = open(file_name, 'r').readline().rstrip('\n').lstrip('target area: ')
ta_x_min,ta_x_max,ta_y_min,ta_y_max = [int(val) for val in re.findall(r"-*\d+",input)]  
  
def move(x_pos,y_pos,x_vel,y_vel):
    x_pos += x_vel
    y_pos += y_vel
    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1
    y_vel -= 1
    return x_pos,y_pos,x_vel,y_vel
  
def is_target_reached(x_pos,y_pos):
    return x_pos >= ta_x_min and x_pos <= ta_x_max and y_pos >= ta_y_min and y_pos <= ta_y_max

def is_targed_missed(x_pos,y_pos):
    return x_pos > ta_x_max or y_pos < ta_y_min
  
def main():
    num_of_correct_vel = 0
    for x_start_vel in range(0,1000):
        for y_start_vel in range(-1000,1000):
            x_pos = 0
            y_pos = 0
            x_vel = x_start_vel
            y_vel = y_start_vel
            while not is_targed_missed(x_pos,y_pos):
                if is_target_reached(x_pos,y_pos):
                    num_of_correct_vel += 1
                    break
                x_pos,y_pos,x_vel,y_vel = move(x_pos,y_pos,x_vel,y_vel)
    return num_of_correct_vel


if __name__ == "__main__":
    print(main())
