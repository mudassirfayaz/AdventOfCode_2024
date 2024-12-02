def count_safe_reports(reports):
    answer = 0  # To count the safe reports
    
    for report in reports:
        is_safe = True
        trend = None  # None initially, 'increasing' or 'decreasing'
        
        for i in range(len(report) - 1):
            diff = report[i + 1] - report[i]
            
            # Check if the difference is out of the allowed range
            if abs(diff) < 1 or abs(diff) > 3:
                is_safe = False
                break
            
            # Determine the trend (increasing or decreasing)
            current_trend = 'increasing' if diff > 0 else 'decreasing'
            
            # If the trend switches, the report is unsafe
            if trend is None:
                trend = current_trend  # Set initial trend
            elif trend != current_trend:
                is_safe = False
                break
        
        if is_safe:
            answer += 1  # Increment the count if the report is safe
    
    return answer



with open("./Day2/input.txt") as f:
    reports = [[int(i) for i in l.split()] for l in f]
# Test the function
print("Safe reports:", count_safe_reports(reports))
