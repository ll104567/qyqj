import random
import curses
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


def generate_random_array(std_np_puzzle,n=1000,shape=4):
   
    xx_np_puzzle = np.copy(std_np_puzzle)
    s = [move_up,move_left,move_down,move_right]
    for i in range(n):
        move_func = random.choice(s)
        zero_position = find_zero_position(xx_np_puzzle,shape)
        if move_func(zero_position,shape):
            next_position = move_func(zero_position,shape)
            tmp = xx_np_puzzle[zero_position]
            xx_np_puzzle[zero_position] = xx_np_puzzle[next_position]
            xx_np_puzzle[next_position] = tmp
        
    return xx_np_puzzle

if __name__ == '__main__': 
    stdscr = curses.initscr() ### curses ....
    UP,DOWN,LEFT,RIGHT=65,66,68,67
    banner = '//[q]quit/[r]restart'
    author = '//[A]uthor: Hu/[E]mail:ll104567i@163.com'

    puzzle = 15
    shape = get_puzzle_shape(puzzle)
    std_np_puzzle = list_to_np(generate_std_list(puzzle))
    random_np_puzzle = generate_random_array(std_np_puzzle)

    while 1:
        try:
            set_win()
            stdscr.clear()
            display_info(banner,0,1)
            display_info(author,0,2)
            display_info(gui(random_np_puzzle),0,3)

            '''
                Time mode
            '''

            if game_is_ok(std_np_puzzle,random_np_puzzle):
                display_info(banner,0,1)
                display_info(author,0,2)
                display_info(gui(std_np_puzzle),0,3)
                display_info('Niu bi',0,11)

            display_info('>>>',0,12)
            c = get_ch_and_continue()
            if c in (ord('q'),ord('Q')):
                exit()
            if c in (ord('r'),ord('R')):
                random_np_puzzle = generate_random_array(std_np_puzzle)
                stdscr.clear()
                display_info(gui(random_np_puzzle),0,0)

            if c in (ord('x'),ord('X')):
                random_np_puzzle =  np.copy(std_np_puzzle)

            if c in (ord('w'),UP):
                zero_position = find_zero_position(random_np_puzzle,shape)
                if move_up(zero_position,shape):
                    next_position = move_up(zero_position,shape)
                    tmp = random_np_puzzle[zero_position]
                    random_np_puzzle[zero_position] = random_np_puzzle[next_position]
                    random_np_puzzle[next_position] = tmp

            if c in (ord('a'),LEFT):
                zero_position = find_zero_position(random_np_puzzle,shape)
                if move_left(zero_position,shape):
                    next_position = move_left(zero_position,shape)
                    tmp = random_np_puzzle[zero_position]
                    random_np_puzzle[zero_position] = random_np_puzzle[next_position]
                    random_np_puzzle[next_position] = tmp
                    
            if c in (ord('s'),DOWN):
                zero_position = find_zero_position(random_np_puzzle,shape)
                if move_down(zero_position,shape):
                    next_position = move_down(zero_position,shape)
                    tmp = random_np_puzzle[zero_position]
                    random_np_puzzle[zero_position] = random_np_puzzle[next_position]
                    random_np_puzzle[next_position] = tmp

            if c in (ord('d'),RIGHT):
                zero_position = find_zero_position(random_np_puzzle,shape)
                if move_right(zero_position,shape):
                    next_position = move_right(zero_position,shape)
                    tmp = random_np_puzzle[zero_position]
                    random_np_puzzle[zero_position] = random_np_puzzle[next_position]
                    random_np_puzzle[next_position] = tmp
            else:
                continue
        finally:
            unset_win()

