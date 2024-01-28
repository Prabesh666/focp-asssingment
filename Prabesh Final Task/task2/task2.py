import re


def parse_line(line):
    cat, entry_time, exit_time = line.strip().split(",")
    return cat, int(entry_time), int(exit_time)


def analyze_log(log_data):
    cat_visits = 0
    other_cats = 0
    total_time_ours = 0
    visit_lengths_ours = []
    for line in log_data:
        if line == "END":
            break
        cat, entry_time, exit_time = parse_line(line)
        if cat == "OURS":
            cat_visits += 1
            visit_lengths_ours.append(exit_time - entry_time)
            total_time_ours += exit_time - entry_time
        else:
            other_cats += 1
    average_visit_ours = total_time_ours / cat_visits if cat_visits else 0
    longest_visit_ours = max(visit_lengths_ours) if visit_lengths_ours else 0
    shortest_visit_ours = min(visit_lengths_ours) if visit_lengths_ours else 0
    total_time_ours_hours, total_time_ours_minutes = divmod(total_time_ours, 60)
    return (
        cat_visits,
        other_cats,
        f"{total_time_ours_hours} Hours, {total_time_ours_minutes} Minutes",
        f"{average_visit_ours:.2f} Minutes",
        f"{longest_visit_ours} Minutes",
        f"{shortest_visit_ours} Minutes",
    )


def main():
    try:
        with open("first.log", "r") as file:
            log_data = file.readlines()
    except FileNotFoundError:
        print("Error: The file 123.txt was not found.")
        return

    cat_visits, other_cats, total_time_ours, average_visit_ours, longest_visit_ours, shortest_visit_ours = analyze_log(
        log_data
    )
    print("Log File Analysis")
    print("==================")
    print(f"Cat Visits: {cat_visits}")
    print(f"Other Cats: {other_cats}")
    print(f"Total Time in House: {total_time_ours}")
    print(f"Average Visit Length: {average_visit_ours}")
    print(f"Longest Visit:        {longest_visit_ours}")
    print(f"Shortest Visit:       {shortest_visit_ours}")


if __name__ == "__main__":
    main()
