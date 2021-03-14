def toggleCount(ans):  # to toggle count displayed in labels
    global ripecount, rawcount, midcount
    if (ans == 1):
        rawcount += 1

    elif (ans == 2):
        ripecount += 1
    else:
        midcount += 1
    ri.set(f'Ans = {rawcount:.2f}')
    # print(ri.get())
    # ripe.configure(text = re.get())


root = Tk()
root.title('Durian Classification Machine')
root.geometry('400x300')
root.configure(bg='#d6efc7')
# root.iconbitmap('co.ico')


photo5 = PhotoImage(file="durian.png")
photo5 = photo5.subsample(20, 20)
photo6 = PhotoImage(file="on.png")
photo6 = photo6.subsample(5, 5)
photo7 = PhotoImage(file="off.png")
photo7 = photo7.subsample(5, 5)

ri = StringVar()

# Button on/off
button = Button(root,
                text='OFF',
                command=switch,
                bg="#d6efc7",
                image=photo7,
                bd=0,
                )
button.grid(column=1, row=0, padx=5, pady=5)

# Labels for durian classifed according to their ripeness

ripe = Label(root,
             width=117,
             height=100,
             font="none 12 bold",
             # text="RIPE: "+str(ripecount),
             text=ri.get(),
             command=toggleCount(ans),
             bg="#96bb7c",
             image=photo5,
             compound=LEFT,
             )
ripe.grid(column=0, row=1, padx=5, pady=5)
raw = Label(root,
            width=117,
            height=100,
            text="RAW: ",
            # text="RAW: "+str(rawcount),
            command=toggleCount(ans),
            font="none 12 bold",
            bg="#96bb7c",
            image=photo5,
            compound=LEFT,
            )
raw.grid(column=1, row=1, padx=5, pady=5)
mid = Label(root,
            width=117,
            height=100,
            text="MID: ",
            # text="MID: "+str(midcount),
            command=toggleCount(ans),
            font="none 12 bold",
            bg="#96bb7c",
            image=photo5,
            compound=LEFT,
            )
mid.grid(column=2, row=1, padx=5, pady=5)

### Main ###
if __name__ == "__main__":
    root.mainloop()
    GPIO.cleanup()  # reset all GPIO
