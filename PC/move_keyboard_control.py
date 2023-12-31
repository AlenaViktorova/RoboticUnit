import tkinter as tk
import serial
from enum import Enum
import visu_format as visual


class MotorState(Enum):
    FORWARD = 1
    BACK = 2
    RIGHT = 3
    LEFT = 4
    STOP = 5


motorState = MotorState.STOP


def send_command(command):
    # send the command character to Arduino
    ser.write(command.encode())
    global motorState
    if command == 'w':
        motorState = MotorState.FORWARD
    elif command == 's':
        motorState = MotorState.BACK
    elif command == 'a':
        motorState = MotorState.LEFT
    elif command == 'd':
        motorState = MotorState.RIGHT
    else:
        motorState = MotorState.STOP


def update_display():
    # Clear previous highlighting
    visual.change_key_background_color(canvas, "W", "white")
    visual.change_key_background_color(canvas, "A", "white")
    visual.change_key_background_color(canvas, "S", "white")
    visual.change_key_background_color(canvas, "D", "white")

    # Highlight the corresponding arrow
    if motorState == MotorState.FORWARD:
        visual.change_key_background_color(canvas, "W", "lightblue")
    elif motorState == MotorState.BACK:
        visual.change_key_background_color(canvas, "S", "lightblue")
    elif motorState == MotorState.LEFT:
        visual.change_key_background_color(canvas, "A", "lightblue")
    elif motorState == MotorState.RIGHT:
        visual.change_key_background_color(canvas, "D", "lightblue")

    # Update the state label
    state_label.config(text=f"Current State: {motorState.name}")

    # Call the function again after 100 ms
    root.after(100, update_display)


# Initialize the serial port
ser = serial.Serial('COM3', 9600)  # Set the correct COM port and communication speed

# Create the main window
root = tk.Tk()
root.title("Motor Control")

# Set the fixed window size
root.geometry("300x240")

# Add keyboard buttons and texts
canvas = tk.Canvas(root, width=220, height=140)
desc_label = tk.Label(root, text="Hold Key on Keyboard for Robot Motion.", font=("Arial", 12), width=33, height=2)
desc_label.grid(row=1, column=1)

canvas.grid(row=2, column=1)

forward_arrow = visual.draw_key(canvas, "W", 80, 10, 50, 50)
back_arrow = visual.draw_key(canvas, "A", 20, 70, 50, 50)
left_arrow = visual.draw_key(canvas, "S", 80, 70, 50, 50)
right_arrow = visual.draw_key(canvas, "D", 140, 70, 50, 50)

state_label = tk.Label(root, text="Current State: STOP", font=("Arial", 12), width=20, height=2)
state_label.grid(row=3, column=1)

# Add keyboard actions
root.bind("<KeyPress>", lambda event: send_command(event.char.lower()))
root.bind("<KeyRelease>", lambda event: send_command('q'))  # Send 'q' when a key is released

# Run the function to update the display
update_display()

# Run the main loop
root.mainloop()
