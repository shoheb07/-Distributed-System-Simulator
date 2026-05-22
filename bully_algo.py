class Process:

    def __init__(self, pid):

        self.pid = pid
        self.active = True

# Create Processes
processes = [
    Process(1),
    Process(2),
    Process(3),
    Process(4),
    Process(5)
]

# Coordinator
coordinator = 5

print(f"Initial Coordinator: P{coordinator}")

# Simulate Coordinator Failure
processes[4].active = False

print("Coordinator P5 Failed")

# Election Function
def bully_election(starter):

    global coordinator

    print(f"\nP{starter} Starts Election")

    higher_process_found = False

    for process in processes:

        if process.pid > starter and process.active:

            print(
                f"P{starter} sends Election Message to P{process.pid}"
            )

            higher_process_found = True

    if not higher_process_found:

        coordinator = starter

        print(
            f"\nP{starter} becomes New Coordinator"
        )

# Start Election
bully_election(3)

print(f"\nFinal Coordinator: P{coordinator}")
