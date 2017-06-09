import tkinter as tk
ShareStartCol = 9

counter = 0
def count():
    global counter
    counter += 1
    label.config(text=str(counter))

players = ["Zihui","Alex","Oscar","Titan","Martin"]

corps = ["RRR","WSD","WED","FFS","RWE"]

root = tk.Tk()
root.title("1846")

r = 0;
for p in players:
    tk.Label(text=p,bg="white", width=8).grid(row=0, column=r)
    tk.Entry(text="400", width=8).grid(row=1, column=r)

    r +=1
r = 0
for p in corps:
    tk.Label(text=p,bg="gray",width=8).grid(row=2, column=r)
    tk.Entry(text="400", width=8).grid(row=3, column=r)
    r +=1

tk.Label(text = "Earnings", bg = "white",width = 8).grid(row= 4,column = 0)
tk.Label(text = "Distribution", bg = "white",width = 24).grid(row= 4,column = 1,columnspan = 3)
tk.Label(text = "Share worth", bg = "white",width = 8).grid(row= 4,column = 4,columnspan = 3)
tk.Label(text = "Own", bg = "yellow",width = 12).grid(row= 4,column = ShareStartCol,columnspan = 3)
r = ShareStartCol+3
for p in players:
    tk.Label(text=p, bg="yellow", width=12).grid(row=4, column=r,columnspan = 3)
    r+=3
r = 5
for c in corps:
    tk.Entry(text="0", width=8).grid(row=r, column=0) #Earnings
    tk.Button(text="0%", width=8).grid(row=r, column=1)  # Distribution
    tk.Button(text="50%", width=8).grid(row=r, column=2)  # Distribution
    tk.Button(text="100%", width=8).grid(row=r, column=3)  # Distribution

    tk.Button(text="-", width=3).grid(row=r, column=4)  # company's own shares
    tk.Label(text="0", width=4).grid(row=r, column=5) # Share Price
    tk.Button(text="+", width=3).grid(row=r, column=6)

    w = ShareStartCol
    tk.Label(text=c, width=3,bg= "red").grid(row=r, column=w-1)  # company's own shares
    tk.Button(text="-", width=3).grid(row=r, column=w)  # company's own shares
    tk.Entry(text="10", width=4).grid(row=r, column=w+1)
    tk.Button(text="+", width=3).grid(row=r, column=w+2)
    for p in players:
        w += 3
        tk.Button(text="-", width=3).grid(row=r, column=w)  # player shares
        tk.Entry(text="10", width=4).grid(row=r, column=w+1)
        tk.Button(text="+", width=3).grid(row=r, column=w+2)
    r+=1

root.mainloop()
