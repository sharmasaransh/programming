import math
import curses

def main_menu():
 stdscr.clear()
 stdscr.refresh()
 stdscr.border(0)

 stdscr.addstr(5, 5, 'Calulator', curses.A_BOLD)
 stdscr.addstr(6, 5, 'Press a for arithematic :', curses.A_BOLD)
 stdscr.addstr(7, 5, 'Press g for geometry :', curses.A_BOLD)
 stdscr.addstr(12, 5, 'Press q to close this screen', curses.A_NORMAL)
 while True:
  # stay in this loop till the user presses 'q'
  ch = stdscr.getch(12,50)
  if ch == ord('q'):
   break
  elif ch == ord('a'):
   a_menu()
  elif ch == ord('g'):
   g_menu()
  # -- End of user code -

def r_menu():
 stdscr.clear()
 stdscr.refresh()
 stdscr.border(0)

 stdscr.addstr(5, 5, 'Area Calulator', curses.A_BOLD)
 stdscr.addstr(6, 5, 'Press p for parallelogram :', curses.A_BOLD)
 stdscr.addstr(7, 5, 'Press s for square :', curses.A_BOLD)
 stdscr.addstr(8, 5, 'Press c for circle :', curses.A_BOLD)
 stdscr.addstr(12, 5, 'Press q to close this screen', curses.A_NORMAL)
 while True:
  # stay in this loop till the user presses 'q'
  ch = stdscr.getch(12,50)
  if ch == ord('q'):
   break
  elif ch == ord('p'):
   apar()
  elif ch == ord('s'):
   asub()
  elif ch == ord('c'):
   acir()
  # -- End of user code -

def a_menu():
 stdscr.clear()
 stdscr.refresh()
 stdscr.border(0)

 stdscr.addstr(5, 5, 'Area Calulator', curses.A_BOLD)
 stdscr.addstr(6, 5, 'Press a for addition :', curses.A_BOLD)
 stdscr.addstr(7, 5, 'Press s for substraction :', curses.A_BOLD)
 stdscr.addstr(8, 5, 'Press m for multiplication :', curses.A_BOLD)
 stdscr.addstr(9, 5, 'Press d for division :', curses.A_BOLD)
 stdscr.addstr(10, 5, 'Press e for exponential :', curses.A_BOLD)
 stdscr.addstr(11, 5, 'Press o for modulus :', curses.A_BOLD)
 stdscr.addstr(12, 5, 'Press f for floor division :', curses.A_BOLD)
 stdscr.addstr(15, 5, 'Press q to close this screen', curses.A_NORMAL)
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
  elif ch == ord('e'):
   exp()
  elif ch == ord('o'):
   mod()
  elif ch == ord('f'):
   fdi()
  # -- End of user code -

def g_menu():
 stdscr.clear()
 stdscr.refresh()
 stdscr.border(0)

 stdscr.addstr(5, 5, 'Area Calulator', curses.A_BOLD)
 stdscr.addstr(6, 5, 'Press p for perimeter :', curses.A_BOLD)
 stdscr.addstr(8, 5, 'Press a for area :', curses.A_BOLD)
 stdscr.addstr(12, 5, 'Press q to close this screen', curses.A_NORMAL)
 while True:
  # stay in this loop till the user presses 'q'
  ch = stdscr.getch(12,50)
  if ch == ord('q'):
   break
  elif ch == ord('a'):
   r_menu()
  elif ch == ord('p'):
   p_menu()
  # -- End of user code -

def p_menu():
 stdscr.clear()
 stdscr.refresh()
 stdscr.border(0)

 stdscr.addstr(5, 5, 'Perimeter Calulator', curses.A_BOLD)
 stdscr.addstr(6, 5, 'Press p for parallelogram :', curses.A_BOLD)
 stdscr.addstr(7, 5, 'Press s for square :', curses.A_BOLD)
 stdscr.addstr(8, 5, 'Press c for circle :', curses.A_BOLD)
 stdscr.addstr(12, 5, 'Press q to close this screen', curses.A_NORMAL)
 while True:
  # stay in this loop till the user presses 'q'
  ch = stdscr.getch(12,50)
  if ch == ord('q'):
   break
  elif ch == ord('p'):
   ppar()
  elif ch == ord('s'):
   psqu()
  elif ch == ord('c'):
   pcir()
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
 i = int(i)
 n = int(n)
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
 i = int(i)
 n = int(n)
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
 i = int(i)
 n = int(n)
 a = str(i * n)
 stdscr.refresh()
 stdscr.addstr(7,5, "product is " + a)
 stdscr.refresh()
 curses.napms(9000)
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
 i = int(i)
 n = int(n)
 a = str(i / n)
 stdscr.refresh()
 stdscr.addstr(7,5, "quotient is " + a)
 stdscr.refresh()
 curses.napms(2000)
 main_menu()

def fdi():
 stdscr.clear()
 stdscr.refresh()
 curses.echo()
 stdscr.addstr(1,5, 'In Floor divsion', curses.A_BOLD)
 stdscr.addstr(3,5, 'enter 1 number', curses.A_NORMAL)
 i = stdscr.getstr(3, 50, 20).decode(encoding="utf-8")
 stdscr.addstr(4,5, 'enter other number', curses.A_NORMAL)
 n = stdscr.getstr(4, 50, 20).decode(encoding="utf-8")
 i = int(i)
 n = int(n)
 a = str(i // n)
 stdscr.refresh()
 stdscr.addstr(7,5, "floor quotient is " + a)
 stdscr.refresh()
 curses.napms(9000)
 main_menu()

def mod():
 stdscr.clear()
 stdscr.refresh()
 curses.echo()
 stdscr.addstr(1,5, 'In Modulus', curses.A_BOLD)
 stdscr.addstr(3,5, 'enter 1 number', curses.A_NORMAL)
 i = stdscr.getstr(3, 50, 20).decode(encoding="utf-8")
 stdscr.addstr(4,5, 'enter other number', curses.A_NORMAL)
 n = stdscr.getstr(4, 50, 20).decode(encoding="utf-8")
 i = int(i)
 n = int(n)
 a = str(i % n)
 stdscr.refresh()
 stdscr.addstr(7,5, "remainder is " + a)
 stdscr.refresh()
 curses.napms(2000)
 main_menu()

def exp():
 stdscr.clear()
 stdscr.refresh()
 curses.echo()
 stdscr.addstr(1,5, 'In Exponential', curses.A_BOLD)
 stdscr.addstr(3,5, 'enter base', curses.A_NORMAL)
 i = stdscr.getstr(3, 50, 20).decode(encoding="utf-8")
 stdscr.addstr(4,5, 'enter exponent', curses.A_NORMAL)
 n = stdscr.getstr(4, 50, 20).decode(encoding="utf-8")
 i = int(i)
 n = int(n)
 a = str(i ** n)
 stdscr.refresh()
 stdscr.addstr(7,5, "exponential is " + a)
 stdscr.refresh()
 curses.napms(9000)
 main_menu()

def apar():
  stdscr.clear()
  stdscr.refresh()
  curses.echo()
  stdscr.addstr(1,5, 'In a parallelogram', curses.A_BOLD)
  stdscr.addstr(3,5, 'enter 1 side')
  i = stdscr.getstr(3, 50, 20).decode(encoding="utf-8")
  stdscr.addstr(4,5, 'enter other side')
  n = stdscr.getstr(4, 50, 20).decode(encoding="utf-8")
  i = int(i)
  n = int(n)
  a = str(i * n)
  stdscr.addstr(5,5, "area is"  + " "  +a)
  stdscr.refresh()
  curses.napms(9000)
  main_menu()

def asqu():
  stdscr.clear()
  stdscr.refresh()
  curses.echo()
  stdscr.addstr(1,5, 'In a square', curses.A_BOLD)
  stdscr.addstr(3,5, 'enter a side')
  i = stdscr.getstr(3, 50, 20).decode(encoding="utf-8")
  i = int(i)
  a = str(i * i)
  stdscr.addstr(5,5, "area is" + " " + a)
  stdscr.refresh()
  curses.napms(2000)
  main_menu()

def acir():
  stdscr.clear()
  stdscr.refresh()
  curses.echo()
  stdscr.addstr(1,5, 'In a circle', curses.A_BOLD)
  stdscr.addstr(3,5, 'enter the radius')
  i = stdscr.getstr(3, 50, 20).decode(encoding="utf-8")
  i = int(i)
  a = str(math.pi * i * i)
  stdscr.addstr(5,5, "area is" + " " + a)
  stdscr.refresh()
  curses.napms(9000)
  g_menu()

def ppar():
  stdscr.clear()
  stdscr.refresh()
  curses.echo()
  stdscr.addstr(1,5, 'In a parallelogram', curses.A_BOLD)
  stdscr.addstr(3,5, 'enter 1 side')
  i = stdscr.getstr(3, 50, 20).decode(encoding="utf-8")
  stdscr.addstr(4,5, 'enter other side')
  n = stdscr.getstr(4, 50, 20).decode(encoding="utf-8")
  i = int(i)
  n = int(n)
  a = str(2 * (i + n))
  stdscr.addstr(5,5, "area is" + " " + a)
  stdscr.refresh()
  curses.napms(2000)
  g_menu()

def psqu():
  stdscr.clear()
  stdscr.refresh()
  curses.echo()
  stdscr.addstr(1,5, 'In a square', curses.A_BOLD)
  stdscr.addstr(3,5, 'enter a side')
  i = stdscr.getstr(3, 50, 20).decode(encoding="utf-8")
  i = int(i)
  a = str(i * 4)
  stdscr.addstr(5,5, 'area is' + " " + a)
  stdscr.refresh()
  curses.napms(9000)
  g_menu()

def pcir():
  stdscr.clear()
  stdscr.refresh()
  curses.echo()
  stdscr.addstr(1,5, 'In a circle', curses.A_BOLD)
  stdscr.addstr(3,5, 'enter the radius')
  i = stdscr.getstr(3, 50, 20).decode(encoding="utf-8")
  i = int(i)
  a = str(math.pi * i * 2)
  stdscr.addstr(5,5, 'area is' + " " + a)
  stdscr.refresh()
  curses.napms(2000)
  main_menu()

stdscr = curses.initscr()            # initialize curses screen
curses.noecho()             # turn off auto echoing of keypress on to screen
curses.cbreak()             # enter break mode where pressing Enter key
stdscr.keypad(1)            # enable special Key values such as curses.KEY_LEFT etc

main_menu()

stdscr.keypad(0)
curses.echo()
curses.nocbreak()
curses.endwin()
