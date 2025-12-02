def get_top_n_frequent(items, n):
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(items)
    items_with_counts = []
    for item in unique_items:
        freq = items.count(item)
        items_with_counts.append((-1 * freq, item))
    print(items_with_counts)
    items_with_counts.sort()
    print(items_with_counts)
    part = items_with_counts[:n]
    print(part)
    result = []
    for t in part:
        result.append(t[1])
        return result