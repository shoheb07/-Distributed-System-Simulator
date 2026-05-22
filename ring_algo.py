processes = [1, 2, 3, 4, 5]

active = {
    1: True,
    2: True,
    3: True,
    4: True,
    5: False
}

print("Process P5 Failed")

def ring_election(starter):

    print(f"\nP{starter} Starts Election")

    ring = []

    current = starter

    while True:

        if active[current]:

            ring.append(current)

        current = current % len(processes) + 1

        if current == starter:
            break

    print("Election Ring:", ring)

    coordinator = max(ring)

    print(
        f"New Coordinator is P{coordinator}"
    )

ring_election(2)
