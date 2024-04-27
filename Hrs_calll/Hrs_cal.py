import tkinter as tk
from datetime import datetime

# Function to calculate time difference

def time_elapsed_in_hours_minutes(input_time):
    try:
        # Check for time range format like "19:00-22:00" or "19.00-22.00"
        if '-' in input_time:
            start_time, end_time = map(str.strip, input_time.split('-'))
            input_format = None

            if ':' in start_time:
                input_format = "%H:%M"
            elif '.' in start_time:
                input_format = "%H.%M"
            else:
                raise ValueError

            start_datetime = datetime.strptime(start_time, input_format)
            end_datetime = datetime.strptime(end_time, input_format)

            time_difference = end_datetime - start_datetime
            total_hours, remainder = divmod(time_difference.seconds, 3600)
            total_minutes = remainder // 60
            return total_hours, total_minutes

        # Check for single time format like "19:00" or "19.00"
        elif ':' in input_time or '.' in input_time:
            input_format = None

            if ':' in input_time:
                input_format = "%H:%M"
            elif '.' in input_time:
                input_format = "%H.%M"
            else:
                raise ValueError

            input_datetime = datetime.strptime(input_time, input_format)
            current_datetime = datetime.now()
            time_difference = current_datetime - input_datetime
            hours, seconds = divmod(time_difference.seconds, 3600)
            minutes = seconds // 60
            return hours, minutes

        else:
            raise ValueError

    except ValueError:
        return None

# Function to update the result label
def update_result(event=None):
    input_time = entry.get()
    result = time_elapsed_in_hours_minutes(input_time)
    
    if result is not None:
        hours, minutes = result
        result_label.config(text=f"Time spent from {input_time} to now: {hours} hours and {minutes} minutes", fg="red")
    else:
        result_label.config(text="Invalid time format. Please use HH:MM or HH.MM.", fg="red")

# Function to update the clock display
def update_clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title("Time Calculator⌚")
root.geometry("420x300")
root.resizable(False, False)
root.configure(bg="#F0F0F0")

# Set a custom icon
root.iconphoto(False, tk.PhotoImage(file="dist/clock_icon.png"))

# Create and place widgets with better styling
title_label = tk.Label(root, text="Time Calculator⏲️", font=("Helvetica", 16), bg="#F0F0F0")
title_label.pack(pady=15)

label = tk.Label(root, text="Enter time (HH:MM or HH.MM):", font=("Helvetica", 12), bg="#F0F0F0")
label.pack()

entry = tk.Entry(root, font=("Helvetica", 12))
entry.pack()
entry.bind('<Return>', update_result)  # Bind the Enter key to the update_result function

calculate_button = tk.Button(root, text="Calculate", command=update_result, font=("Helvetica", 12), bg="#008CBA", fg="white")
calculate_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#F0F0F0")
result_label.pack()

# Clock display label
clock_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#F0F0F0")
clock_label.pack()

# Center the window on the screen
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry(f"+{position_right}+{position_down}")

# Start the Tkinter main loop
root.after(0, update_clock)
root.mainloop()
