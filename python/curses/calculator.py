import math
import curses

def main_menu():
 stdscr.clear()
 stdscr.refresh()
 stdscr.border(0)

 stdscr.addstr(5, 5, 'Area Calulator', curses.A_BOLD)
 stdscr.addstr(6, 5, 'Press a for addition :', curses.A_BOLD)
 stdscr.addstr(7, 5, 'Press s for substraction :', curses.A_BOLD)
 stdscr.addstr(8, 5, 'Press m for multiplication :', curses.A_BOLD)
 stdscr.addstr(9, 5, 'Press d for division :', curses.A_BOLD)
 stdscr.addstr(12, 5, 'Press q to close this screen', curses.A_NORMAL)
 while True:
  # stay in this loop till the user presses 'q'
  ch = stdscr.getch(12,50)
  if ch == ord('q'):
   break
  elif ch == ord('a'):
   add()
  elif ch == ord('s'):
   sub()
  elif ch == ord('m'):
   mul()
  elif ch == ord('d'):
   div()
  # -- End of user code -


def add():
 stdscr.clear()
 stdscr.refresh()
 curses.echo()
 stdscr.addstr(1,5, 'In Addition', curses.A_BOLD)
 stdscr.addstr(3,5, 'enter 1 number', curses.A_NORMAL)
 i = stdscr.getstr(3, 50, 20).decode(encoding="utf-8")
 stdscr.addstr(4,5, 'enter other number', curses.A_NORMAL)
 n = stdscr.getstr(4, 50, 20).decode(encoding="utf-8")
 n = int(n)
 i = int(i)
 a = str(i + n)
 stdscr.refresh()
 stdscr.addstr(7,5, "sum is " + a)
 stdscr.refresh()
 curses.napms(2000)
 main_menu()


def sub():
 stdscr.clear()
 stdscr.refresh()
 curses.echo()
 stdscr.addstr(1,5, 'In Substraction', curses.A_BOLD)
 stdscr.addstr(3,5, 'enter number to be substracted from', curses.A_NORMAL)
 i = stdscr.getstr(3, 50, 20).decode(encoding="utf-8")
 stdscr.addstr(4,5, 'enter number to be substracted', curses.A_NORMAL)
 n = stdscr.getstr(4, 50, 20).decode(encoding="utf-8")
 n = int(n)
 i = int(i)
 a = str(i - n)
 stdscr.refresh()
 stdscr.addstr(7,5, "difference is " + a)
 stdscr.refresh()
 curses.napms(2000)
 main_menu()

def mul():
 stdscr.clear()
 stdscr.refresh()
 curses.echo()
 stdscr.addstr(1,5, 'In multiplication', curses.A_BOLD)
 stdscr.addstr(3,5, 'enter 1st number', curses.A_NORMAL)
 i = stdscr.getstr(3, 50, 20).decode(encoding="utf-8")
 stdscr.addstr(4,5, 'enter other number', curses.A_NORMAL)
 n = stdscr.getstr(4, 50, 20).decode(encoding="utf-8")
 n = int(n)
 i = int(i)
 a = str(i * n)
 stdscr.refresh()
 stdscr.addstr(7,5, "product is " + a)
 stdscr.refresh()
 curses.napms(2000)
 main_menu()

def div():
 stdscr.clear()
 stdscr.refresh()
 curses.echo()
 stdscr.addstr(1,5, 'In Division', curses.A_BOLD)
 stdscr.addstr(3,5, 'enter divident', curses.A_NORMAL)
 i = stdscr.getstr(3, 50, 20).decode(encoding="utf-8")
 stdscr.addstr(4,5, 'enter divisor', curses.A_NORMAL)
 n = stdscr.getstr(4, 50, 20).decode(encoding="utf-8")
 n = int(n)
 i = int(i)
 a = str(i / n)
 stdscr.refresh()
 stdscr.addstr(7,5, "quotient is " + a)
 stdscr.refresh()
 curses.napms(2000)
 main_menu()

stdscr = curses.initscr()   # initialize curses screen
curses.noecho()             # turn off auto echoing of keypress on to screen
curses.cbreak()             # enter break mode where pressing Enter key
stdscr.keypad(1)            # enable special Key values such as curses.KEY_LEFT etc

main_menu()

stdscr.keypad(0)
curses.echo()
curses.nocbreak()
curses.endwin()
