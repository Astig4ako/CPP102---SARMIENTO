
def get_initial_readings():
    """Return the initial device temperature readings."""
    return [28, 31, 35, 37, 29]


def is_whole_number(text):
    """Check if the input contains only whole-number digits."""
    return text.isdigit()


def add_reading(readings):
    """Validate and add a new temperature reading."""
    text = input("Enter new reading: ").strip()

    if len(text) == 0:
        print("\nInvalid input. The reading cannot be empty.")
        return

    if not is_whole_number(text):
        print("\nInvalid input. Enter a whole number only.")
        return

    value = int(text)

    if value < 0 or value > 100:
        print("\nInvalid reading. Enter a value from 0 to 100.")
        return

    readings.append(value)
    print("\nReading added successfully.")


def classify_reading(reading, warning_limit=30, critical_limit=35):
    """Classify a reading based on the temperature limits."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def compute_total(readings):
    """Calculate the total of all readings using a loop."""
    total = 0

    for reading in readings:
        total += reading

    return total


def compute_average(readings):
    """Calculate the average of all readings."""
    if len(readings) == 0:
        return 0.0

    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Find the smallest reading using a loop."""
    if len(readings) == 0:
        return 0

    smallest = readings[0]

    for reading in readings:
        if reading < smallest:
            smallest = reading

    return smallest


def find_maximum(readings):
    """Find the largest reading using a loop."""
    if len(readings) == 0:
        return 0

    largest = readings[0]

    for reading in readings:
        if reading > largest:
            largest = reading

    return largest


def count_category(readings, category):
    """Count how many readings belong to a category."""
    count = 0

    for reading in readings:
        if classify_reading(reading) == category:
            count += 1

    return count


def determine_overall_status(warning_count, critical_count):
    """Determine the overall status of the monitoring system."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_readings(readings):
    """Display all current readings."""
    print("\nCURRENT READINGS")
    print("----------------")

    for index, reading in enumerate(readings, start=1):
        print(f"Reading {index}: {reading} °C")


def display_classifications(readings):
    """Display each reading and its classification."""
    print("\nREADING CLASSIFICATION")
    print("----------------------")

    for reading in readings:
        category = classify_reading(reading)
        print(f"{reading} °C -> {category}")


def display_summary(readings):
    """Display the calculated monitoring summary."""
    total_elements = len(readings)

    if total_elements == 0:
        print("\nNo readings available.")
        return

    total_sum = compute_total(readings)
    avg_temp = compute_average(readings)
    min_temp = find_minimum(readings)
    max_temp = find_maximum(readings)

    normal_count = count_category(readings, "NORMAL")
    warning_count = count_category(readings, "WARNING")
    critical_count = count_category(readings, "CRITICAL")

    normal_pct = (normal_count / total_elements) * 100
    warning_pct = (warning_count / total_elements) * 100
    critical_pct = (critical_count / total_elements) * 100

    status = determine_overall_status(
        warning_count, critical_count
    )

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings   : {total_elements}")
    print(f"Total of readings    : {total_sum}")
    print(f"Average temperature  : {avg_temp:.2f} °C")
    print(f"Minimum temperature  : {min_temp} °C")
    print(f"Maximum temperature  : {max_temp} °C")
    print()
    print(f"NORMAL   : {normal_count} ({normal_pct:.2f}%)")
    print(f"WARNING  : {warning_count} ({warning_pct:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_pct:.2f}%)")
    print()
    print(f"Overall Status: {status}")


def display_menu():
    """Display the available menu options."""
    print("\nDEVICE MONITORING AND ALERT SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def main():
    """Run the device monitoring system."""
    readings = get_initial_readings()

    while True:
        display_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            display_readings(readings)

        elif choice == "2":
            add_reading(readings)

        elif choice == "3":
            display_classifications(readings)

        elif choice == "4":
            display_summary(readings)

        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
