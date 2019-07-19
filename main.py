import os
import keyboard
import testio
import const


def pause():
    print()
    try:
        input("Press the <ENTER> key to continue...")
    except SyntaxError:
        pass
    clear_screen()


def clear_screen():
    if serial_port.system.lower() == "linux":
        os.system("clear")
    elif serial_port.system.lower() == "windows":
        os.system("cls")


def printer():
    all_count = 0
    fail_count = 0

    while not keyboard.is_pressed('q'):
        print("---Test------------------------------")
        print("Serial port =", serial_port.name)
        print("Baud rate =", const.BAU_RATE)
        print("Time out =", const.TIME_OUT)
        print("-------------------------------------")
        print("Press key 'Q' to quit")

        serial_port.send()
        all_count += 1
        # print(serial_port.read())
        if serial_port.read() == const.NULL_LIST:
            clear_screen()
            print("Status: FAILED ")
            fail_count += 1
        else:
            clear_screen()
            print("Status: PASS ")

    print("--------------------------------------")
    print("Succeed count:", all_count-fail_count)
    print("Failed count:", fail_count)
    print("Success rate:%.2f" % ((all_count-fail_count)/all_count*100)+"%")
    print("--------------------------------------")


if __name__ == '__main__':
    serial_port = testio.SerialPort(None)
    clear_screen()

    # text mode interface
    serial_port.scan()
    print("-------------------------------------")
    serial_port.list()
    print("")
    serial_port.input()
    print('-------------------------------------')

    # serial port settings
    serial_port.config(const.BAU_RATE, const.TIME_OUT)

    # show serial port settings
    if serial_port.port.is_open:
        print("Serial port [", serial_port.name, "] is open")
        pause()
        printer()
