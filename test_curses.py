import curses

screen = curses.initscr()
screen.addstr(0,0,"text 1")
screen.addstr(3,1,"text 2")

screen.refresh()

curses.napms(2000)
curses.endwin()

