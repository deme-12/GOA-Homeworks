def spot_diff(s1,s2):
    differences = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            differences.append(i)
    return differences