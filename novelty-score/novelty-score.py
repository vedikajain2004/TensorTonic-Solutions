def novelty_score(recommendations, item_counts, n_users):
    """
    Compute the average novelty of a recommendation list.
    """
    # Write code here
    import math
    nov = []
    for i in recommendations:
        nov.append(-math.log2(item_counts[i] / n_users))
    avg = sum(nov) / len(recommendations)
    return avg