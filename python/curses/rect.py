import math as m
import curses
from curses.textpad import Textbox, rectangle

def rect():
	stdscr.clear()
	curses.noecho()             # turn off auto echoing of keypress on to screen
	stdscr.refresh()
	uly = (int(stdscr.getbegyx()[0]))
	ulx = (int(stdscr.getbegyx()[1]))
	lry = (int(stdscr.getmaxyx()[0])-1)
	lrx = (int(stdscr.getmaxyx()[1]))
	#for x in range(m.ceil(stdscr.getbegyx()[0])/2):
	for x in range(0,16):
		uly+=1
		ulx+=1
		lry-=1
		lrx-=1
		rectangle(stdscr,uly,ulx,lry,lrx)
		stdscr.refresh()
		#stdscr.addstr(7, 5, str(uly) + " " + str(ulx) + " " + str(lry) + " " + str(lrx))
		curses.napms(50)
		stdscr.clear()
	for x in range(0,15):
		uly-=1
		ulx-=1
		lry+=1
		lrx+=1
		rectangle(stdscr,uly,ulx,lry,lrx)
		stdscr.refresh()
		#stdscr.addstr(7, 5, str(uly) + " " + str(ulx) + " " + str(lry) + " " + str(lrx))
		curses.napms(50)
		stdscr.clear()


### Main Program to start

stdscr = curses.initscr()   # initialize curses screen
curses.noecho()             # turn off auto echoing of keypress on to screen
curses.cbreak()             # enter break mode where pressing Enter key
stdscr.keypad(1)            # enable special Key values such as curses.KEY_LEFT etc

rect()

stdscr.keypad(0)
curses.echo()
curses.nocbreak()
curses.endwin()
