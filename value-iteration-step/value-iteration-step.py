def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    # Write code here
    vs = []
    for s in range(len(values)):
        vs.append(max(rewards[s][a] + gamma * sum(transitions[s][a][sn] * values[sn] for sn in range(len(values))) for a in range(len(rewards[s]))))
    return vs