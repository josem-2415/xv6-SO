from collections import deque


def print_frames(frames):
    """
    Prints the current state of the page frames.
    """
    print("| ", end="")
    for page in frames:
        if page is None:
            print("- ", end="")
        else:
            print(f"{page} ", end="")
    print("|", end="")


def fifo_page_replacement(num_frames, reference_string):

    frames = [None] * num_frames
    fifo_queue = deque()

    page_faults = 0
    hits = 0

    print("\n" + "=" * 72)
    print("               FIFO PAGE REPLACEMENT SIMULATOR")
    print("=" * 72)

    print(f"\nFrames: {num_frames}")
    print("Reference String:", reference_string)

    print("\n" + "-" * 72)
    print("{:<10} {:<25} {:<15}".format("Reference", "Frames", "Result"))
    print("-" * 72)

    for page in reference_string:

        # PAGE HIT
        if page in frames:
            hits += 1

            print("{:<10}".format(page), end="")
            print_frames(frames)
            print("   HIT")

        # PAGE FAULT
        else:

            page_faults += 1

            # Empty frame available
            if None in frames:

                index = frames.index(None)
                frames[index] = page
                fifo_queue.append(page)

            else:

                oldest = fifo_queue.popleft()

                replace_index = frames.index(oldest)

                frames[replace_index] = page

                fifo_queue.append(page)

            print("{:<10}".format(page), end="")
            print_frames(frames)
            print("   PAGE FAULT")

    print("-" * 72)

    print(f"\nTotal References : {len(reference_string)}")
    print(f"Page Faults      : {page_faults}")
    print(f"Hits             : {hits}")

    fault_rate = (page_faults / len(reference_string)) * 100
    hit_rate = (hits / len(reference_string)) * 100

    print(f"Fault Rate       : {fault_rate:.2f}%")
    print(f"Hit Rate         : {hit_rate:.2f}%")

    print("=" * 72)


def main():

    print("=" * 50)
    print("FIFO PAGE REPLACEMENT TEST")
    print("=" * 50)

    num_frames = int(input("Enter the number of page frames: "))

    total_references = int(input("Enter the number of page references: "))

    while True:

        sequence = input(
            f"Enter {total_references} page references separated by spaces:\n"
        ).split()

        if len(sequence) != total_references:
            print("\nIncorrect number of references. Try again.\n")
        else:
            break

    reference_string = [int(x) for x in sequence]

    fifo_page_replacement(num_frames, reference_string)


if __name__ == "__main__":
    main()