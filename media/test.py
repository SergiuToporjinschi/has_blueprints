import re
import os
import tkinter as tk
from tkinter import filedialog

with open("Cross 3FlatEnd.tap", "r") as file:
    gcode = file.read()
    lines = gcode.split("\n")

    for i in range(len(lines)):
        if "Z5." in lines[i] and not ("F" in lines[i] or "f" in lines[i]):
            lines[i] += " F3000"
        elif "Z-" in lines[i]:
            lines[i] += " F1000"

    modified_gcode = "\n".join(lines)

    with open("filename_new.gcode", "w") as new_file:
        new_file.write(modified_gcode)
