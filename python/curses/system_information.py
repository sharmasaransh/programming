import os
import platform
import psutil
import math
import curses

def main_menu():
     stdscr.clear()
     stdscr.refresh()
     stdscr.border(0)

     stdscr.addstr(5, 5, 'Get information about your system', curses.A_BOLD)
     stdscr.addstr(6, 5, 'Press t for terminal :', curses.A_BOLD)
     stdscr.addstr(7, 5, 'Press s for system :', curses.A_BOLD)
     stdscr.addstr(8, 5, 'Press m for memory :', curses.A_BOLD)
     stdscr.addstr(9, 5, 'Press d for disk :', curses.A_BOLD)
     stdscr.addstr(10, 5, 'Press w for swap_memory :', curses.A_BOLD)
     stdscr.addstr(12, 5, 'Press q to close this screen', curses.A_NORMAL)
     while True:
            # stay in this loop till the user presses 'q'
            ch = stdscr.getch(12,50)
            if ch == ord('q'):
                break
            elif ch == ord('t'):
                terminal()
            elif ch == ord('s'):
                system()
            elif ch == ord('m'):
                memory()
            elif ch == ord('d'):
                disk()
            elif ch == ord('w'):
                swap_memory()
        # -- End of user code
def system():
  stdscr.clear()
  stdscr.refresh()
  curses.echo()
  stdscr.addstr(2, 5, "---------------------------------------------------------------------------")
  stdscr.addstr(3, 5, "The name of the system is " + str(platform.node()))
  stdscr.addstr(4, 5, "The platform of the system is " + str(platform.platform()))
  stdscr.addstr(5, 5, "The architecture of the system is " + str(platform.architecture()))
  stdscr.addstr(6, 5, "The version of the system is " + str(platform.release()))
  stdscr.addstr(7, 5, "---------------------------------------------------------------------------")
  stdscr.refresh()
  curses.napms(6000)
  main_menu()
def terminal():
  stdscr.clear()
  stdscr.refresh()
  curses.echo()
  stdscr.addstr(2, 5, "---------------------------------------------------------------------------")
  stdscr.addstr(3, 5, "the number of characters in your terminal is " + str(os.get_terminal_size().columns))
  stdscr.addstr(4, 5, "the number of lines in your terminal is " + str(os.get_terminal_size().lines))
  stdscr.addstr(5, 5, "---------------------------------------------------------------------------")
  stdscr.refresh()
  curses.napms(3000)
  main_menu()
def memory():
  stdscr.clear()
  stdscr.refresh()
  curses.echo()
  stdscr.addstr(2, 5, "---------------------------------------------------------------------------")
  stdscr.addstr(3, 5, "the total memory in your RAM is " + str(math.ceil(psutil.virtual_memory().total / 1024**3)) + "GB")
  stdscr.addstr(4, 5, "the available memory in your RAM is " + str(math.ceil(psutil.virtual_memory().available / 1024**3)) + "GB")
  stdscr.addstr(5, 5, "the used memory in your RAM is " + str(math.ceil(psutil.virtual_memory().used / 1024**3)) + "GB")
  stdscr.addstr(6, 5, "the free memory in your RAM is " + str(math.ceil(psutil.virtual_memory().free / 1024**3)) + "GB")
  stdscr.addstr(7, 5, "---------------------------------------------------------------------------")
  stdscr.refresh()
  curses.napms(6000)
  main_menu()
def swap_memory():	
  stdscr.clear()
  stdscr.refresh()
  curses.echo()
  stdscr.addstr(2, 5, "---------------------------------------------------------------------------")
  stdscr.addstr(3, 5, "the total swap memory is " + str(math.ceil(psutil.swap_memory().total / 1024**3)) + "GB")
  stdscr.addstr(4, 5, "the swap memory percent is " + str(math.ceil(psutil.swap_memory().percent)))
  stdscr.addstr(5, 5, "the used swap memory is " + str(math.ceil(psutil.swap_memory().used / 1024**3)) + "GB")
  stdscr.addstr(6, 5, "the free swap memory is " + str(math.ceil(psutil.swap_memory().free / 1024**3)) + "GB")
  stdscr.addstr(7, 5, "---------------------------------------------------------------------------")
  stdscr.refresh()
  curses.napms(6000)
  main_menu()
def disk():
  stdscr.clear()
  stdscr.refresh()
  curses.echo()
  stdscr.addstr(2, 5, "---------------------------------------------------------------------------")
  stdscr.addstr(4, 5, "the total disk memory is " + str(math.ceil(psutil.disk_usage('/').total / 1024**3)) + "GB")
  stdscr.addstr(5, 5, "the disk memory percent is " + str(math.ceil(psutil.disk_usage('/').percent)) + "%")
  stdscr.addstr(6, 5, "the used disk memory is " + str(math.ceil(psutil.disk_usage('/').used / 1024**3)) + "GB")
  stdscr.addstr(7, 5, "the free disk memory is " + str(math.ceil(psutil.disk_usage('/').free / 1024**3)) + "GB")
  stdscr.addstr(8, 5, "---------------------------------------------------------------------------")
  stdscr.refresh()
  curses.napms(7500)
  main_menu()



stdscr = curses.initscr()  
curses.noecho()             
curses.cbreak()             
stdscr.keypad(1)            

main_menu()

stdscr.keypad(0)
curses.echo()
curses.nocbreak()
curses.endwin()
