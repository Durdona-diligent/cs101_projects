def longest_downward_trend(prices):
    current_count = 0
    max_count = 0
    for i in range(1, len(prices)):
        if prices[i] < prices[i-1]:
            if prices[i] > 1:
                current_count += 1
                if current_count > max_count:
                    max_count = current_count
        else:
            current_count = 0
print (longest_downward_trend(prices))