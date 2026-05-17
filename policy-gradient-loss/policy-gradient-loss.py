def policy_gradient_loss(log_probs, rewards, gamma):
    """
    Compute REINFORCE policy gradient loss with mean-return baseline.
    """
    # Write code here
    t, g = len(rewards), 0
    disc_ret = []
    for i in range(-1, -t - 1, -1):
        g = rewards[i] + gamma * g
        disc_ret.insert(0, g)
    mg = sum(disc_ret) / t
    a = [disc_ret[i] - mg for i in range(t)]
    loss = -sum([log_probs[i] * a[i] for i in range(t)]) / t
    return loss