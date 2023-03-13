
def Hamming_Dist(str1, str2):
    dist = 0.0
    str1_set = set()
    str2_set = set()
    for i in range(0, len(str1)):
        str1_set.add(str1[i])
    # print(str1_set)
    for i in range(0, len(str2)):
        str2_set.add(str2[i])
    # print(str2_set)
    Num_of_same_char = len(str1_set.intersection(str2_set))
    # print(Num_of_same_char)
    if len(str1_set) >= len(str2_set):
        dist = len(str1_set) - Num_of_same_char
        # print(len(str1_set))
    if len(str2_set) > len(str1_set):
        dist = len(str2_set) - Num_of_same_char

    return dist