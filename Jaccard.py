
__author__ = '{BENMOUSSA Younes}'
__email__ = '{benmoussayounes00@gmail.com}'

from math import exp
def jaccard_similarity(list1, list2):
    intersection = abs(len(set(list1).intersection(list2)))
    union = abs((len(list1) + len(list2)))
    return float(intersection/union)


# Unlike the Jaccard similarity (Jaccard index),
# the Jaccard distance is a measure of dissimilarity between two sets.
def jaccard_dissimilarity(list1, list2):
    intersection = len(set(list1).intersection(list2))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection)/union
# Consider the two sets a and b
A = {1, 2, 3, 5, 7}
B = {1, 2, 4, 8, 9}
print('Jaccard similarity : ', jaccard_similarity(A, B))
a = [1,2,3]
b = [2, 3, 4, 5]
print('Jaccard dissimilarity : ', jaccard_dissimilarity(a,b))


sentences = ["The bottle is empty",
"There is nothing in the bottle"]
sentences = [sent.lower().split(" ") for sent in sentences]
print('Similarity : ', jaccard_similarity(sentences[0], sentences[1]))

"""

"""

def distance_to_similarity(distance):
  return 1/exp(distance)

#distance_to_similarity(distance)