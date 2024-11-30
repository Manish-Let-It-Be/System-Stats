# Program without UI
import psutil

def display_processes(order_by='cpu_desc'):
    processes = []
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        processes.append({
            'PID': process.info['pid'],
            'Name': process.info['name'],
            'CPU%': process.info['cpu_percent'],
            'Memory (MB)': process.info['memory_info'].rss / (1024 * 1024)
        })
    
    if order_by == 'cpu_asc':
        processes.sort(key=lambda x: x['CPU%'])
    elif order_by == 'cpu_desc':
        processes.sort(key=lambda x: x['CPU%'], reverse=True)
    elif order_by == 'memory_asc':
        processes.sort(key=lambda x: x['Memory (MB)'])
    elif order_by == 'memory_desc':
        processes.sort(key=lambda x: x['Memory (MB)'], reverse=True)

    return processes

def main():
    order_by = 'cpu_desc'  # Default sorting order
    while True:
        print("\n===== Task Manager =====")
        print("PID    | Name                        | CPU%   | Memory (MB)")
        print("=" * 60)
        
        processes = display_processes(order_by)
        for process in processes:
            print(f"{process['PID']:<7}| {process['Name']:<28}| {process['CPU%']:<7}| {process['Memory (MB)']:.2f}")
        
        print("\nOptions:")
        print("1. Ascending Order CPU")
        print("2. Ascending Order Memory")
        print("3. Descending Order CPU")
        print("4. Descending Order Memory")
        print("5. Highest Usage of Memory")
        print("6. Highest Usage of CPU")
        print("7. Quit")
        print("8. Refresh")
        
        action = input("Choose an option: ")
        
        if action == '1':
            order_by = 'cpu_asc'
        elif action == '2':
            order_by = 'memory_asc'
        elif action == '3':
            order_by = 'cpu_desc'
        elif action == '4':
            order_by = 'memory_desc'
        elif action == '5':
            order_by = 'memory_desc'  # Highest usage of memory is handled by descending order
        elif action == '6':
            order_by = 'cpu_desc'  # Highest usage of CPU is handled by descending order
        elif action == '7':
            break
        elif action == '8':
            continue  # Refresh will automatically happen in the next loop

if __name__ == "__main__":
    main()
