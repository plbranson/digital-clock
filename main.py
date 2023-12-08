#  Copyright 2023 Patrick L. Branson
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
#  See the License for the specific language governing permissions and
#  limitations under the License.

from time import strftime
from tkinter import Label, Tk


def main():
    """
    Runs the Clock GUI and calculations

    :return: None - "void" function
    """

    def update():
        """
        Constantly updates the clock

        :return: None - "void" function
        """
        current = strftime("%H: %M: %S\n %m-%d-%y ")
        label.configure(text=current)
        label.after(80, update)
        label.pack(anchor="center")

    # Defines and initializes the main window
    window = Tk()
    window.title("Clock")
    window.geometry("200x100")
    window.configure(bg="green")
    window.resizable(False, False)

    # Defines and initializes the main window label
    label = Label(window, bg="black", fg="cyan", font=("Arial", 30, "bold"), relief="flat")
    label.place(x=20, y=20)

    # Runs the loop
    update()
    window.mainloop()


if __name__ == '__main__':
    main()
