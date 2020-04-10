from serial import Serial
import time
import smbus
serialPort = Serial("/dev/ttyAMA0", 9600)
screen = [["0"] * 24] * 80
I2C_ADDR = 0x21
CMD_code = 0b01000000
bus = smbus.SMBus(1)
if (serialPort.isOpen() == False):
    serialPort.open()


def paddleA(i):
    serialPort.write('\033['+str(i)+';3H')
    serialPort.write("\x1b[48;5;255m")
    serialPort.write(" ")


def paddleB(i):
    serialPort.write('\033['+str(i)+';77H')
    serialPort.write('\x1b[48;5;255m')
    serialPort.write('\033['+str(i)+';40H')
    serialPort.write('\x1b[48;5;255m')
    serialPort.write(' ')

topA = 1
botA = 5
topB = 1
botB = 5
check = False


def ball(x, y):
    serialPort.write('\033['+str(y)+';'+str(x)+'H')
    serialPort.write("\x1b[48;5;255m")
    serialPort.write(' ')
    return x, y


def moveball(ballx, bally):

    ballx += balldx
    bally += balldy

    return(ballx, bally)


def edge(balldx, balldy):
    if ballx == 80 or ballx == 0:
        balldx /= -1
    if bally == 24 or bally == 0:
        balldy /= -1
    return balldx, balldy


def dis(ballx, bally):
    serialPort.write('\033['+str(bally)+';'+str(ballx)+'H')
    serialPort.write('\x1b[48;5;0m')
    serialPort.write(' ')


def hit(balldx, ballx, bally, topA, botA):
    if balldx == -1 and (ballx == 4 or ballx == 3) and topA <= bally and botA > bally:
        return -1
    elif balldx == 1 and (ballx == 76 or ballx == 77) and topB <= bally and botB >= bally:
        return -1
    else:
        return 1


def scA(ballx, bally):
    if ballx < 3:
        check = True


def score0B():
    serialPort.write('\033[2;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[3;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[3;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    screen[46][2] = '178'
    screen[47][2] = '178'
    screen[48][2] = '178'
    screen[46][6] = '178'
    screen[47][6] = '178'
    screen[48][6] = '178'
    screen[46][3] = '178'
    screen[46][4] = '178'
    screen[46][5] = '178'
    screen[48][3] = '178'
    screen[48][4] = '178'
    screen[48][5] = '178'


def score1B():
    serialPort.write('\033[2;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    screen[46][2] = '178'

    serialPort.write('\033[2;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    screen[47][2] = '178'

    serialPort.write('\033[6;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    screen[46][6] = '178'
    serialPort.write('\033[6;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    screen[47][6] = '178'
    serialPort.write('\033[6;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    screen[48][6] = '178'
    serialPort.write('\033[3;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    screen[46][3] = '178'
    serialPort.write('\033[4;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    screen[47][4] = '178'
    serialPort.write('\033[5;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    screen[48][5] = '178'


def score2B():
    serialPort.write('\033[2;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;48H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    screen[46][2] = '178'
    screen[47][2] = '178'
    screen[48][2] = '178'
    screen[46][6] = '178'
    screen[47][6] = '178'
    screen[48][6] = '178'
    screen[46][3] = '178'
    screen[46][4] = '178'
    screen[46][5] = '178'
    screen[48][3] = '178'
    screen[48][4] = '178'
    screen[48][5] = '178'


def score3B():
    serialPort.write('\033[2;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;48H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def score4B():
    serialPort.write('\033[2;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;47H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;47H')
    serialPort.write('\x1b[48;5;178m')

    serialPort.write('\033[3;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[6;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def score5B():
    serialPort.write('\033[2;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;48H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def score6B():
    serialPort.write('\033[2;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;48H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def score7B():
    serialPort.write('\033[2;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;48H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def score8B():
    serialPort.write('\033[2;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;48H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def score9B():
    serialPort.write('\033[2;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;48H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;48H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;46H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;47H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def score0A():
    serialPort.write('\033[2;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;36H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    screen[34][2] = '178'
    screen[35][2] = '178'
    screen[36][2] = '178'
    screen[34][6] = '178'
    screen[35][6] = '178'
    screen[36][6] = '178'
    screen[34][4] = '178'
    screen[34][5] = '178'
    screen[34][6] = '178'
    screen[36][3] = '178'
    screen[36][4] = '178'
    screen[36][5] = '178'


def score1A():
    serialPort.write('\033[2;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[6;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    screen[34][2] = '178'
    screen[35][2] = '178'
    screen[34][6] = '178'
    screen[35][6] = '178'
    screen[36][6] = '178'
    screen[35][4] = '178'
    screen[34][5] = '178'
    screen[34][6] = '178'
    screen[36][3] = '178'
    screen[36][4] = '178'
    screen[36][5] = '178'


def score2A():
    serialPort.write('\033[2;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;36H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def score3A():
    serialPort.write('\033[2;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;36H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def score4A():
    serialPort.write('\033[2;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;36H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;35H')
    serialPort.write('\x1b[48;5;178m')

    serialPort.write('\033[3;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[6;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def score5A():
    serialPort.write('\033[2;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;36H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def score6A():
    serialPort.write('\033[2;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;36H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def score7A():
    serialPort.write('\033[2;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;36H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def score8A():
    serialPort.write('\033[2;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;36H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[6;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def score9A():
    serialPort.write('\033[2;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[2;36H')
    serialPort.write("\x1b[48;5;178m")
    serialPort.write(' ')

    serialPort.write('\033[6;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[5;36H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[3;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')
    serialPort.write('\033[4;34H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')

    serialPort.write('\033[4;35H')
    serialPort.write('\x1b[48;5;178m')
    serialPort.write(' ')


def downA(topA, botA):
    serialPort.write('\033['+str(topA)+';3H')
    serialPort.write("\x1b[48;5;0m")
    serialPort.write(' ')
    topA += 1
    serialPort.write('\033['+str(botA)+';3H')
    serialPort.write("\x1b[48;5;255m")
    serialPort.write(' ')
    botA += 1
    return(topA, botA)


def upA(topA, botA):
    serialPort.write('\033['+str(botA)+';3H')
    serialPort.write("\x1b[48;5;0m")
    serialPort.write(' ')
    botA -= 1
    serialPort.write('\033['+str(topA)+';3H')
    serialPort.write("\x1b[48;5;255m")
    serialPort.write(' ')
    topA -= 1
    return(topA, botA)


x = 0
y = 0
scoreA = 0
scoreb = 0
ballx = 4
bally = 3
balldx = 1
balldy = 1
checka = False
checkb = False

tmp = 0
def main():
    for p in range(topA, botA):
        paddleA(p)
        paddleB(p)
    for n in range(2, 81, 2):
        net(n)
    global ballx, bally, balldx, balldy, scoreA, scoreb, x, y, tmp
    score0A()
    score0B()
    while True:
        x, y = ball(ballx, bally)
        ballx, bally = moveball(ballx, bally)
        balldx, balldy = edge(balldx, balldy)
        balldx = balldx * hit(balldx, ballx, bally, topA, botA)
        dis(x, y)
        bus.write_byte(I2C_ADDR,0b11110000)
        tmp =bus.read_word_data(I2C_ADDR, 0x00)

    #    if  bus.read_byte(I2C_ADDR)== 's' and botA < 24:
        #    topA, botA = downA(topA, botA)
    #    if serialPort.read() == 'w' and topA > 1:
        #    topA, botA = upA(topA, botA)
        if ballx < 3:
            checka = True
            scoreA += 1
        if ballx > 77:
            checkb = True
            scoreb += 1
        if scoreA == 1and checka is True:
            score1A()
            checka is False
        elif scoreA == 2and checka is True:
            score2A()
            checka is False
        elif scoreA == 3and checka is True:
            score3A()
            checka is False
        elif scoreA == 4and checka is True:
            score4A()
            checka is False
        elif scoreA == 5and checka is True:
            score5A()
            checka is False
        elif scoreA == 6and checka is True:
            score6A()
            checka is False
        elif scoreA == 7and checka is True:
            score7A()
            checka is False
        elif scoreA == 8and checka is True:
            score8A()
            checka is False
        elif scoreA == 9and checka is True:
            score9A()
            checka is False
        elif scoreA == 10and checka is True:
            serialPort.write('\033[2 J')
            serialPort.write('P1 wins')
        if scoreb == 1and checkb is True:
            score1B()
            checkb is False
        elif scoreb == 2and checkb is True:
            score2B()
            checkb is False
        elif scoreb == 3and checkb is True:
            score3B()
            checkb is False
        elif scoreb == 4and checkb is True:
            score4B()
            checkb is False
        elif scoreb == 5and checkb is True:
            score5B()
            checkb is False
        elif scoreb == 6and checkb is True:
            score6B()
            checkb is False
        elif scoreb == 7and checkb is True:
            score7B()
            checkb is False
        elif scoreb == 8and checkb is True:
            score8B()
            checkb is False
        elif scoreb == 9and checkb is True:
            score9B()
            checkb is False
        elif scoreb == 10and checkb is True:
            serialPort.write('\033[2 J')
            serialPort.write('P2 wins')
while True:
    bus.write_byte(I2C_ADDR,CMD_code)
    tmp =bus.read_word_data(I2C_ADDR, 0x00)
    tmp = (tmp >> 8) | ((tmp & 0b11111111) << 8) & 0b0000111111111111
    print(tmp)
if __name__ == '__main__':
    main()

serialPort.close()
