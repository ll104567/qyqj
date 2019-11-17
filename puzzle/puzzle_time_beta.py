import random
import curses
import time
import numpy as np

###### some curses func <I just use...>
def display_info(str, x, y,):
    global stdscr
    stdscr.addstr(y,x,str)
    stdscr.refresh()

def get_ch_and_continue():
    global stdscr
    try:
        stdscr.nodelay(0)
        ch=stdscr.getch()
        stdscr.nodelay(1)
    except:
        exit(2)
    return ch

def set_win():
    global stdscr
    curses.noecho()
    curses.cbreak()
    stdscr.nodelay(1)

def unset_win():
    global stdscr
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()
###################   over

def generate_std_list(puzzle=15):
    
    '''
        return [1,2,...15,0]
    '''

    std = list(range(1,puzzle+1)) + list(range(1))
    return std

def generate_random_list(puzzle=15):

    '''
        return [1,4,2,0,....]
    '''
    std = generate_std_list(puzzle)
    random.shuffle(std)
    return std

def get_puzzle_shape(puzzle=15):
    '''
        return a number n*n
    '''
    
    return int(np.sqrt(puzzle+1))


def list_to_np(list_puzzle,shape=4):
    '''
        convert a list to array
    '''
    np_puzzle = np.array(list_puzzle)
    
    return np_puzzle.reshape((shape,shape))
    
def find_zero_position(np_puzzle,shape=4):
    '''
        get 0 position at array
    '''
    for i in range(shape):
        for j in range(shape):
            if np_puzzle[i,j] == 0:
                return (i,j)

def game_is_ok(np_puzzle,np_std_puzzle):
    
    is_ok = np_puzzle == np_std_puzzle
    if is_ok.all():
        return True
    else:
        return False

def move_up(zero_position,shape=4):
    
    if zero_position[0] == shape - 1 :
        return False

    else:
        swap_position = (zero_position[0]+1,zero_position[1])
        return swap_position

def move_down(zero_position,shape=4):
    
    if zero_position[0] == 0:
        return False
    
    else:
        swap_position = (zero_position[0]-1,zero_position[1])
        return swap_position

def move_left(zero_position,shape=4):
    
    if zero_position[1] == shape - 1:
        return False
    else:
        swap_position = (zero_position[0],zero_position[1]+1)
        return swap_position

def move_right(zero_position,shape=4):

    if zero_position[1] == 0:
        return False
    else:
        swap_position = (zero_position[0],zero_position[1]-1)
        return swap_position

def gui(np_array):
    
    size = len(np_array)
    length = get_puzzle_shape(puzzle=15)

    gui_str = ''
    init_str = '+' + ('-'*length + '+')*size
    gui_str += init_str + '\n'

    for i in np_array:
        for j in i:
            if j == 0:
                j = ' '
            space = length - len(str(j))
            gui_str += '|' + ' '*space + str(j)
        gui_str += '|\n'
        gui_str += init_str + '\n'
    return gui_str

def str_time(timex):
    try: 
        a = str(timex).split()
        return a[0]+'.'+a[1][:3]
    except:
        return '1.001'

if __name__ == '__main__':
   
    stdscr = curses.initscr() ### curses ....
    UP,DOWN,LEFT,RIGHT=65,66,68,67

    puzzle = 15
    shape = get_puzzle_shape(puzzle)
    std_np_puzzle = list_to_np(generate_std_list(puzzle))
    random_np_puzzle = list_to_np(generate_random_list(puzzle))

    time_flag = False
    fake_time = -1
    while 1:
        try:
            set_win()
            stdscr.clear()
            display_info(gui(random_np_puzzle),0,0)

            '''
                Time mode
            '''
            if time_flag:
                start_time = time.time()

            if game_is_ok(std_np_puzzle,random_np_puzzle):
                if time_flag:
                    used_time = time.time() - start_time
                    x_time = str_time(used_time)
                    display_info('Time: {}'.format(x_time),0,10)
                    time_flag = False
                display_info(gui(std_np_puzzle),0,0)
                display_info('Niu bi',0,11)

            display_info('>>>',0,12)
            c = get_ch_and_continue()
            if c in (ord('q'),ord('Q')):
                exit()
            if c in (ord('r'),ord('R')):
                random_np_puzzle = list_to_np(generate_random_list(puzzle))
                stdscr.clear()
                display_info(gui(random_np_puzzle),0,0)
                
                time_flag = False

            if c in (ord('x'),ord('X')):
                time_flag = False
                random_np_puzzle = list_to_np(generate_std_list(puzzle))

            if c in (ord('w'),UP):
                zero_position = find_zero_position(random_np_puzzle,shape)
                if move_up(zero_position,shape):
                    next_position = move_up(zero_position,shape)
                    tmp = random_np_puzzle[zero_position]
                    random_np_puzzle[zero_position] = random_np_puzzle[next_position]
                    random_np_puzzle[next_position] = tmp
                    zero_position = next_position

                    if not time_flag:
                        time_flag = True
                
            if c in (ord('a'),LEFT):
                zero_position = find_zero_position(random_np_puzzle,shape)
                if move_left(zero_position,shape):
                    next_position = move_left(zero_position,shape)
                    tmp = random_np_puzzle[zero_position]
                    random_np_puzzle[zero_position] = random_np_puzzle[next_position]
                    random_np_puzzle[next_position] = tmp
                    zero_position = next_position
                    
                    if not time_flag:
                        time_flag = True
            if c in (ord('s'),DOWN):
                zero_position = find_zero_position(random_np_puzzle,shape)
                if move_down(zero_position,shape):
                    next_position = move_down(zero_position,shape)
                    tmp = random_np_puzzle[zero_position]
                    random_np_puzzle[zero_position] = random_np_puzzle[next_position]
                    random_np_puzzle[next_position] = tmp
                    zero_position = next_position
                    if not time_flag:
                        time_flag = True

            if c in (ord('d'),RIGHT):
                zero_position = find_zero_position(random_np_puzzle,shape)
                if move_right(zero_position,shape):
                    next_position = move_right(zero_position,shape)
                    tmp = random_np_puzzle[zero_position]
                    random_np_puzzle[zero_position] = random_np_puzzle[next_position]
                    random_np_puzzle[next_position] = tmp
                    zero_position = next_position
                    if not time_flag:
                        time_flag = True

            else:
                continue
        finally:
            unset_win()
