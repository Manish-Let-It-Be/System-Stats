#Program with UI

import psutil
import tkinter as tk
from tkinter import ttk

def display_processes(order_by='CPU_Dsc'):
    processes = []
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        processes.append({
            'PID': process.info['pid'],
            'Name': process.info['name'],
            'CPU%': process.info['cpu_percent'],
            'Memory (MB)': process.info['memory_info'].rss / (1024 * 1024)
        })
    
    if order_by == 'CPU_Asc':
        processes.sort(key=lambda x: x['CPU%'])
    elif order_by == 'CPU_Dsc':
        processes.sort(key=lambda x: x['CPU%'], reverse=True)
    elif order_by == 'Memory_Asc':
        processes.sort(key=lambda x: x['Memory (MB)'])
    elif order_by == 'Memory_Dsc':
        processes.sort(key=lambda x: x['Memory (MB)'], reverse=True)

    return processes

def refresh_processes():
    order_by = order_var.get()
    processes = display_processes(order_by)
    update_process_table(processes)

def update_process_table(processes):
    for row in tree.get_children():
        tree.delete(row)  
    for process in processes:
        tree.insert("", tk.END, values=(process['PID'], process['Name'], f"{process['CPU%']}%", f"{process['Memory (MB)']:.2f} MB"))

def on_quit():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Task Manager")
root.geometry("600x400")

# Create a Treeview for displaying processes
tree = ttk.Treeview(root, columns=("PID", "Name", "CPU%", "Memory (MB)"), show='headings')
tree.heading("PID", text="PID")
tree.heading("Name", text="Name")
tree.heading("CPU%", text="CPU%")
tree.heading("Memory (MB)", text="Memory (MB)")
tree.column("PID", width=80)
tree.column("Name", width=200)
tree.column("CPU%", width=80)
tree.column("Memory (MB)", width=100)

# Add a scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Pack the Treeview
tree.pack(pady=10, fill=tk.BOTH, expand=True)

# Create a dropdown for sorting options
order_var = tk.StringVar(value='CPU_Dsc')
order_menu = ttk.Combobox(root, textvariable=order_var, values=[
    'CPU_Asc', 'CPU_Dsc', 'Memory_Asc', 'Memory_Dsc'
])
order_menu.pack(pady=10)

# Create a button to refresh the process list
refresh_button = tk.Button(root, text="Refresh", command=refresh_processes)
refresh_button.pack(pady=5)

# Create a button to quit the application
quit_button = tk.Button(root, text="Quit", command=on_quit)
quit_button.pack(pady=5)

# Initial population of the process list
refresh_processes()

# Start the GUI event loop
root.mainloop()
