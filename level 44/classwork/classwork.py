def most_frequent_item_count(collection):
    if collection == []:
        return 0
    return max([collection.count(i) for i in collection])