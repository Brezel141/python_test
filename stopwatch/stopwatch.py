import time

# Initialize the stopwatch
start_time = None

while True:
    # Ask the user to press a key to control the stopwatch
    input("Press Enter to start/stop the stopwatch...")
    
    if start_time is None:
        # Start the stopwatch
        start_time = time.time()
        print("Stopwatch started.")
    else:
        # Stop the stopwatch
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        print(f"Elapsed time: {minutes} minutes {seconds} seconds")
        start_time = None  # Reset the stopwatch

