from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename


class MRS:

    def __init__(self, master):

        self.style = ttk.Style()
        self.style.configure("BW.TLabel", foreground="black", background="white", font=('Courier', 14))

        self.labelFrame = ttk.Frame(master)
        ttk.Label(self.labelFrame, text="Movie Recommendation System", style="BW.TLabel")\
            .grid(row=0, column=0, columnspan=2)
        self.labelFrame.pack()

        self.userPanelFrame = ttk.Frame(master)
        ttk.Label(self.userPanelFrame, text="Open file:").grid(row=0, column=0)
        self.filepath = StringVar()
        self.filenameEntry = ttk.Entry(self.userPanelFrame, textvariable=self.filepath)
        self.filenameEntry.grid(row=0, column=1)
        self.fileUpdateButton = ttk.Button(self.userPanelFrame, text="...", command=self.openfile)
        self.fileUpdateButton.grid(row=0, column=2)
        self.userPanelFrame.pack(side=BOTTOM)

    def openfile(self):

        file = askopenfilename()
        self.filepath.set(file)


def main():

    root = Tk()
    app = MRS(root)
    root.mainloop()

if __name__ == "__main__":
    main()
