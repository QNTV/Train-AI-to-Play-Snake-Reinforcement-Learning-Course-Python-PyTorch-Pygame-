# import curses
#
#
# # setup window
# curses.initscr()
# win = curses.newwin(20, 60, 0, 0) # 20 rows, 60 columns, 0 row, 0 column
# win.keypad(1)
# curses.noecho()
# curses.curs_set(0)
# win.border(0)
# win.nodelay(1) # -1 for blocking, 0 for non-blocking
#
# # snake and food
# snake = [(4,10), (4,9), (4,8)]
# food = (10,20)
#
#
#
# # game logic
# score = 0
#
# ESC = 27
# key = curses.KEY_RIGHT
#
#
# while True:
#     event = win.getch()
#
#     for c in snake:
#         win.addch(c[0], c[1], '*')
#
#     win.addch(food[0], food[1], '#')
#
#
#
# curses.endwin()
# print(f"Final score = {score}")

#https://www.youtube.com/watch?v=M_npdRYD4K0
#09:00

