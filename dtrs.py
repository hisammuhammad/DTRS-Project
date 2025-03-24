# Import required libraries
import psutil  # For monitoring processes
import time    # For adding delays
import os      # For running system commands

# List of processes we don’t want to kill (safe system processes)
WHITELIST = ['python.exe', 'cmd.exe', 'System', 'svchost.exe', 'explorer.exe']

def monitor_processes():
    """
    Monitors all running processes and checks for threats.
    Runs in a loop forever until manually stopped (Ctrl+C).
    """
    print("Starting Dynamic Threat Response System...")
    print("Monitoring processes... Press Ctrl+C to stop.")
    
    while True:  # Infinite loop to keep checking
        # Loop through all running processes
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                # Get CPU usage (first call initializes, second call gets value)
                proc.cpu_percent()  # Initialize CPU measurement
                time.sleep(0.1)     # Small delay for accurate reading
                cpu_usage = proc.cpu_percent()  # Get the CPU usage percentage

                # Check if CPU usage is above 70% and process isn’t in whitelist
                if cpu_usage > 70 and proc.info['name'] not in WHITELIST:
                    # Print threat details
                    print(f"Threat detected! Process: {proc.info['name']}, "
                          f"PID: {proc.info['pid']}, CPU: {cpu_usage}%")
                    respond_to_threat(proc.info['pid'])  # Take action
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # Skip if process disappears or we don’t have permission
                continue
        
        # Wait 2 seconds before checking again
        time.sleep(2)

def respond_to_threat(pid):
    """
    Terminates the threatening process using its PID.
    Args:
        pid (int): Process ID of the threat.
    """
    try:
        # Use Windows 'taskkill' command to force terminate the process
        os.system(f"taskkill /PID {pid} /F")
        print(f"Terminated threat: PID {pid}")
    except Exception as e:
        # If termination fails, print the error
        print(f"Failed to terminate PID {pid}: {e}")

# Start the program
if __name__ == "__main__":
    try:
        monitor_processes()  # Run the monitoring function
    except KeyboardInterrupt:
        # Handle Ctrl+C to stop the program gracefully
        print("\nStopped by user. Exiting...")