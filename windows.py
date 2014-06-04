import os
import sys
from tkinter import *
from tkinter import ttk


class NamePrompt:
    """Opens a Tkinter window to prompt for player name input."""

    def __init__(self):
        self.promptBox = Tk()              # Initialize the window object
        self.promptBox.title("Blackjack")  # Put a name in the title bar
        self.promptBox.resizable(0, 0)     # Disable ability to resize window

        self.entryText = StringVar()  # Set a variable to store entry text
        self.playerID = None          # Initialize the playerID as None

        self._build_window()       # Setup the window widgets
        self.promptBox.mainloop()  # Begin capturing events

        self._check_playerid()  # Validate player name entry
        
    def __str__(self):
        return self.playerID

    def _cancel_handler(self, keypress=False):
        """Destroy the window and exit the program when cancel is clicked or the
        user presses the Esc key.
        """

        self.promptBox.destroy()  # Destroy the window
        sys.exit()                # Exit the program

    def _play_handler(self, keypress=False):
        """Destroy the window when the Play button is clicked or the user
        presses the Enter key while the text entry box is active.
        """

        self.promptBox.destroy()  # Destroy the window
        
    def _build_window(self):
        """Setup the Tkinter and ttk window widgets and attributes."""

        self.promptBox.bind('<Escape>', self._cancel_handler)  # Bind Esc
        promptFrame = ttk.Frame(self.promptBox, padding="3 3 12 12")
        promptFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        promptLabel = ttk.Label(promptFrame, text='Enter your name:')
        promptLabel.grid(column=0, row=0)  # Add the text label to window
        entryBox = ttk.Entry(promptFrame, textvariable=self.entryText)
        entryBox.grid(column=0, row=1, columnspan=2, sticky=(E, W))
        entryBox.bind('<Return>', self._play_handler)  # Bind Enter key
        entryBox.focus()  # Focus is on entry box when window is opened
        playButton = ttk.Button(promptFrame, text='Play',
                                command=self._play_handler)
        playButton.grid(column=0, row=3)  # Add Play button to the window
        cancelButton = ttk.Button(promptFrame, text='Cancel',
                                  command=self._cancel_handler)
        cancelButton.grid(column=1, row=3)  # Add Canel button to window

    def _check_playerid(self):
        """Check for player name input and set a safe default if blank. If not
        blank, ensure the length is 12 characters or less.
        """
        self.playerID = self.entryText.get()

        if not self.playerID:  # Entry box was left blank
            self.playerID = "Player"
        elif len(self.playerID) > 12:
            self.playerID = self.playerID[:12]

    def player_id(self):
        """Return the player name."""

        return self.playerID


class HelpAboutWindow:
    """Create a window for the About option in the Help menu."""

    def __init__(self):
        pass


class GameWindow:
    """
    Create an initial Tkinter window for the main game
    """
    def __init__(self, playerid):

        self.playerid = playerid

        self.root = Tk()
        self.root.title("Blackjack")
        self.tableColor = "#339955"
        self.root.geometry("800x600")

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_rowconfigure(0, weight=1)

        self.tableStyle = ttk.Style()
        self.tableStyle.configure("Felt.TFrame", background=self.tableColor,
                                  foreground="white")

        self.statStyle = ttk.Style()
        self.statStyle.configure("Stats.TLabel", background="white",
                                 foreground="black")

        self.tableTextStyle = ttk.Style()
        self.tableTextStyle.configure("Table.TLabel",
                                      background=self.tableColor,
                                      foreground="white",
                                      font="default 12 bold")

        self.tableButtonStyle = ttk.Style()
        self.tableButtonStyle.configure("GreenBG.TButton",
                                        background=self.tableColor)

        self.tableMessage = None  # Initialize empty table action message

        self._menu_bar()
        self._left_side_bar()
        #self._card_table()

        self.root.mainloop()

    def tester(self):
        ##########################
        """
        REMOVE ME WHEN DEBUGGING IS COMPLETE, SERIOUSLY
        I'M JUST ABOUT THE MOST USELESS METHOD IN THE WORLD
        """
        pass #####################

    def _exit_handler(self):
        """
        Destroy the window and exit the program immediately
        """
        self.root.destroy()
        sys.exit()

    def _help_about(self):
        aboutWindow = HelpAboutWindow()

    def _menu_bar(self):
        """
        Create the top menu bar UI elements, assign commands to them
        """
        menuBar = Menu(self.root)
        fileMenu = Menu(menuBar, tearoff=False)
        fileMenu.add_command(label="Deal", command=self.tester)
        fileMenu.add_command(label="Quit", command=self._exit_handler)
        helpMenu = Menu(menuBar, tearoff=False)
        helpMenu.add_command(label="About", command=self.tester)
        menuBar.add_cascade(label="File", menu=fileMenu)
        menuBar.add_cascade(label="Help", menu=helpMenu)
        self.root.config(menu=menuBar)

    def _left_side_bar(self):
        """Create and pack all of the side bar widgets into the left frame."""

        betText = "{0}'s current bet:".format(self.playerid)
        cashText = "{0}'s total cash:".format(self.playerid)
        wonText = "{0}'s highest win:".format(self.playerid)
        lossText = "{0}'s highest loss:".format(self.playerid)
        leftFrame = ttk.Frame(self.mainframe, padding="12 8 12 8")
        leftFrame.pack(expand=True, side=LEFT, fill=BOTH)

        ### Separators instantiation ###
        sepFrame1 = ttk.Frame(leftFrame, padding="12 10 12 10")
        statSeparator1 = ttk.Separator(sepFrame1, orient=HORIZONTAL)
        statSeparator1.pack(expand=True, fill=BOTH)  # Add to new frame
        sepFrame2 = ttk.Frame(leftFrame, padding="12 10 12 10")
        statSeparator2 = ttk.Separator(sepFrame2, orient=HORIZONTAL)
        statSeparator2.pack(expand=True, fill=BOTH)  # Add to new frame
        sepFrame3 = ttk.Frame(leftFrame, padding="12 10 12 10")
        statSeparator3 = ttk.Separator(sepFrame3, orient=HORIZONTAL)
        statSeparator3.pack(expand=True, fill=BOTH)  # Add to new frame

        ### Statistics boxes instantiation ###
        cashLabel = ttk.Label(leftFrame, text=cashText)
        cashTotalLabel = ttk.Label(leftFrame, text="$500", relief=SUNKEN,
                                   style="Stats.TLabel")
        betLabel = ttk.Label(leftFrame, text=betText)
        betAmountLabel = ttk.Label(leftFrame, text="$5", relief=SUNKEN,
                                   style="Stats.TLabel")
        highWonLabel = ttk.Label(leftFrame, text=wonText)
        highWonStatLabel = ttk.Label(leftFrame, text="$50", relief=SUNKEN,
                                   style="Stats.TLabel")
        highLossLabel = ttk.Label(leftFrame, text=lossText)
        highLossStatLabel = ttk.Label(leftFrame, text="$30", relief=SUNKEN,
                                   style="Stats.TLabel")
        minBetLabel = ttk.Label(leftFrame, text="Minimum allowed bet:")
        minBetStatLabel = ttk.Label(leftFrame, text="$5")
        maxBetLabel = ttk.Label(leftFrame, text="Maximum allowed bet:")
        maxBetStatLabel = ttk.Label(leftFrame, text="$5000")

        ### Action buttons instantiation ###
        hitButton = ttk.Button(leftFrame, text='Hit', padding=8,
                               command=self.tester)
        standButton = ttk.Button(leftFrame, text='Stand', padding=8,
                                 command=self.tester)
        doubleButton = ttk.Button(leftFrame, text='Double down',
                                  padding=8, command=self.tester)
        splitButton = ttk.Button(leftFrame, text='Split', state=DISABLED,
                                 padding=8, command=self.tester)
        surrenderButton = ttk.Button(leftFrame, text='Surrender', padding=8,
                                     state=DISABLED, command=self.tester)

        ### Configure all elements in side bar ###
        cashLabel.pack_configure(expand=True, fill=BOTH)
        cashTotalLabel.pack_configure(expand=True, fill=BOTH)
        betLabel.pack_configure(expand=True, fill=BOTH)
        betAmountLabel.pack_configure(expand=True, fill=BOTH)
        sepFrame1.pack_configure(expand=True, fill=BOTH)
        hitButton.pack_configure(expand=True, fill=BOTH, pady=4)
        standButton.pack_configure(expand=True, fill=BOTH, pady=4)
        doubleButton.pack_configure(expand=True, fill=BOTH, pady=4)
        splitButton.pack_configure(expand=True, fill=BOTH, pady=4)
        surrenderButton.pack_configure(expand=True, fill=BOTH, pady=4)
        sepFrame2.pack_configure(expand=True, fill=BOTH)
        highWonLabel.pack_configure(expand=True, fill=BOTH)
        highWonStatLabel.pack_configure(expand=True, fill=BOTH)
        highLossLabel.pack_configure(expand=True, fill=BOTH)
        highLossStatLabel.pack_configure(expand=True, fill=BOTH)
        sepFrame3.pack_configure(expand=True, fill=BOTH)
        minBetLabel.pack_configure(expand=True, fill=BOTH)
        minBetStatLabel.pack_configure(expand=True, fill=BOTH)
        maxBetLabel.pack_configure(expand=True, fill=BOTH)
        maxBetStatLabel.pack_configure(expand=True, fill=BOTH)

    def _card_table(self):
        tableFrame = ttk.Frame(self.mainframe, style="Felt.TFrame")
        tableFrame.pack_configure(expand=True, side=LEFT, fill=BOTH)

        buttonFrame = ttk.Frame(tableFrame, style="Felt.TFrame")
        buttonFrame.pack_configure(expand=True, side=TOP, fill=BOTH,
                                   anchor='center')

        dealerCardFrame = ttk.Frame(tableFrame, style="Felt.TFrame")
        dealerCardFrame.pack_configure(expand=True, fill=BOTH)

        messageFrame = ttk.Frame(tableFrame, style="Felt.TFrame")
        messageFrame.pack_configure(expand=True, fill=BOTH)

        playerCardFrame = ttk.Frame(tableFrame, style="Felt.TFrame")
        playerCardFrame.pack_configure(expand=True, fill=BOTH)

        #tableFrame.grid(column=1, row=0, sticky=(N, S, E, W))
        #tableFrame.grid_columnconfigure(0, weight=1)
        #tableFrame.grid_rowconfigure(0, weight=1)
        
        dealButton = ttk.Button(buttonFrame, text='Deal', padding=8,
                                style="GreenBG.TButton", command=self.tester)

        shuffleButton = ttk.Button(buttonFrame, text='Shuffle', padding=8,
                                   style="GreenBG.TButton", command=self.tester)

        img2_path = os.path.join('images', 'Blue_Back.gif')
        self.card2_img = PhotoImage(file=img2_path)
        
        card2ImgLabel = ttk.Label(dealerCardFrame, image=self.card2_img,
                                 background=self.tableColor)
        
        img_path = os.path.join('images', 'KH.gif')
        self.card_img = PhotoImage(file=img_path)
        
        cardImgLabel = ttk.Label(dealerCardFrame, image=self.card_img,
                                 background=self.tableColor)

        card3ImgLabel = ttk.Label(playerCardFrame, image=self.card_img,
                                 background=self.tableColor)
        
        card4ImgLabel = ttk.Label(playerCardFrame, image=self.card_img,
                                 background=self.tableColor)

        card5ImgLabel = ttk.Label(playerCardFrame, image=self.card_img,
                                 background=self.tableColor)

        messageLabel = ttk.Label(messageFrame,
                                 text='Dealer: "What would you like to do?"',
                                 style="Table.TLabel")

        dealButton.grid_configure(column=0, row=0, padx=4, sticky=(N, S, E, W))
        shuffleButton.grid_configure(column=1, row=0, padx=4, sticky=(N, S, E, W))

        card2ImgLabel.grid_configure(column=0, row=0, sticky=(N, S, E, W))
        cardImgLabel.grid_configure(column=1, row=0, sticky=(N, S, E, W))

        messageLabel.pack_configure(expand=True, fill=BOTH, anchor="center")

        card3ImgLabel.grid_configure(column=0, row=0, sticky=(N, S, E, W))
        card4ImgLabel.grid_configure(column=1, row=0, sticky=(N, S, E, W))

        card5ImgLabel.grid_configure(column=2, row=0, sticky=(N, S, E, W))

