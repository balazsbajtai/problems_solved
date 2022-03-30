def majority_element(nums):
    """ Return the element in a list that occurs the most times.
    # Source: Google Coding Interview Question (Coding Club - LinkedIn), Difficulty: Medium

    :param nums: list of integers
    :return: element that occurs the most times in the list
    """
    value_counts = {}

    for n in nums:
        if n in value_counts.keys():
            value_counts[n] = value_counts[n] + 1
        else:
            value_counts[n] = 1

    highest_value = 0
    highest_key = 0

    for k, v in value_counts.items():
        if v > highest_value:
            highest_value = v
            highest_key = k

    return highest_key
