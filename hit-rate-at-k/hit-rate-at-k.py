def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    u = len(recommendations)
    recs = [set(i[: k]) for i in recommendations]
    gt = [set(i[: k]) for i in ground_truth]
    intsec = [bool(recs[i].intersection(gt[i])) for i in range(u)]
    return sum(intsec) / u