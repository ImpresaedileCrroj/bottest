import calendar
from collections import defaultdict
from datetime import datetime

def generate_monthly_report(presence_data):
    """
    Generate a monthly presence report from parsed presence data.

    Args:
        presence_data (dict): A dictionary with dates as keys and lists of presence events as values.

    Returns:
        dict: A dictionary with months as keys and summarized presence statistics as values.
    """
    monthly_report = defaultdict(lambda: {'joined': 0, 'left': 0, 'workers': set(), 'presence_days': defaultdict(int)})

    for date, events in presence_data.items():
        month_key = date.strftime('%Y-%m')  # Format: YYYY-MM
        for event in events:
            if event['event'] == 'joined':
                monthly_report[month_key]['joined'] += 1
                monthly_report[month_key]['workers'].add(event['worker_name'])
                # Increment presence days for the worker
                monthly_report[month_key]['presence_days'][event['worker_name']] += 1
                # Increment presence days for the worker
                monthly_report[month_key]['presence_days'][event['worker_name']] += 1
            elif event['event'] == 'left':
                monthly_report[month_key]['left'] += 1
                monthly_report[month_key]['workers'].discard(event['worker_name'])

    # Convert sets of workers to counts for the final report
    for month in monthly_report:
        monthly_report[month]['workers_count'] = len(monthly_report[month]['workers'])
        monthly_report[month]['presence_days'] = dict(monthly_report[month]['presence_days'])
        del monthly_report[month]['workers']  # Remove the set of workers

    return dict(monthly_report)

def format_monthly_report(monthly_report):
    """
    Format the monthly presence report for display.

    Args:
        monthly_report (dict): A dictionary with months as keys and summarized presence statistics as values.

    Returns:
        str: A formatted string representation of the monthly report.
    """
    report_lines = []
    report_lines.append("Monthly Presence Report")
    report_lines.append("=" * 25)

    for month, stats in sorted(monthly_report.items()):
        year, month_num = month.split('-')
        month_name = calendar.month_name[int(month_num)]
        report_lines.append(f"{month_name} {year}")
        report_lines.append(f"  Joined: {stats['joined']}")
        report_lines.append(f"  Left: {stats['left']}")
        report_lines.append(f"  Active Workers: {stats['workers_count']}")
        report_lines.append("  Presence Days:")
        for worker, days in stats['presence_days'].items():
            report_lines.append(f"    {worker}: {days} days")
        report_lines.append("  Presence Days:")
        for worker, days in stats['presence_days'].items():
            report_lines.append(f"    {worker}: {days} days")
        report_lines.append("-" * 25)  # Separator

    return "\\\n".join(report_lines)

if __name__ == "__main__":
    # Example usage
    example_data = {
        datetime(2023, 10, 1).date(): [
            {'worker_name': 'Alice', 'event': 'joined'},
            {'worker_name': 'Bob', 'event': 'joined'},
        ],
        datetime(2023, 10, 2).date(): [
            {'worker_name': 'Alice', 'event': 'left'},
            {'worker_name': 'Charlie', 'event': 'joined'},
        ],
        datetime(2023, 11, 1).date(): [
            {'worker_name': 'Bob', 'event': 'left'},
        ],
    }

    monthly_report = generate_monthly_report(example_data)
    formatted_report = format_monthly_report(monthly_report)
    print(formatted_report)