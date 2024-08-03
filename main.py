#  Copyright 2024 Patrick L. Branson
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
#  See the License for the specific language governing permissions and
#  limitations under the License.

import tkinter as tk
from time import strftime
from tkinter.font import Font


class DigitalClock(object):
    """
    The Digital Clock Application
    """

    __master = tk.Tk
    """
    The tkinter Master Widget 
    """

    __main_label: tk.Label
    """
    The tkinter Label used as the main label
    """

    def __init__(self, master: tk.Tk):
        """
        Initializes the DigitalClock class

        :param master: the master (root) GUI
        """
        self.__master = master
        self.__master.title(string="Digital Clock")
        self.__master.geometry(newGeometry="200x100")
        self.__master.configure(background="black")
        self.__master.resizable(width=False, height=False)

        self.__main_label = tk.Label(
            master=self.__master,
            background="black",
            foreground="white",
            relief="flat",
            font=Font(family="Ariel", size=30, weight="bold")
        )
        self.__main_label.place(x=20, y=20)

        self.__update()

    def __update(self) -> None:
        """
        Constantly updates the clock

        :return: None - "void" function
        """
        current = strftime("%H:%M:%S\n %m-%d-%y")
        self.__main_label.configure(text=current)
        self.__main_label.after(ms=80, func=self.__update)
        self.__main_label.pack(anchor="center")


if __name__ == "__main__":
    root: tk.Tk = tk.Tk()
    DigitalClock(root)
    root.mainloop()
