import sqlite3
import tkinter as tk

conn = sqlite3.connect('music.sql')

# Set up the main user view
mainWindow = tk.Tk()
mainWindow.title('Music Jukebox')
mainWindow.geometry('1024x768')
mainWindow.configure(bg='turquoise')
mainWindow.tk_focusFollowsMouse()

# Main columns
mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)

# Main rows
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# Labels on view
tk.Label(mainWindow, bg='turquoise', text="Artist", font=("Roman", 20, 'bold')).grid(row=0, column=0)
tk.Label(mainWindow, bg='turquoise', text="Albums", font=("Roman", 20, 'bold')).grid(row=0, column=1)
tk.Label(mainWindow, bg='turquoise', text="Songs", font=("Roman", 20, 'bold')).grid(row=0, column=2)

# Artist listbox view
artistLV = tk.Variable(mainWindow)
artistLV.set(("Choose Artist",))
artistList = tk.Listbox(mainWindow, listvariable=artistLV)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.configure(border=2, relief='sunken')
artistList.configure(bg='grey')

# Scrolling feature
artistScroll = tk.Scrollbar(mainWindow, orient=tk.VERTICAL, command=artistList.yview())
artistScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
artistList['yscrollcommand'] = artistScroll.set

# Album list view
albumLV = tk.Variable(mainWindow)
albumLV.set(("Choose Album",))
albumList = tk.Listbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.configure(border=2, relief='sunken')
albumList.configure(bg='grey')

# Scrolling feature
albumScroll = tk.Scrollbar(mainWindow, orient=tk.VERTICAL, command=albumList.yview())
albumScroll.grid(row=1, column=1, sticky='nse')
albumList['yscrollcommand'] = albumScroll.set

# Song list view
songLV = tk.Variable(mainWindow)
songLV.set(("Choose Song",))
songList = tk.Listbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.configure(border=2, relief='sunken')
songList.configure(bg='grey')

mainWindow.mainloop()
print("Closing Database")
conn.close()
