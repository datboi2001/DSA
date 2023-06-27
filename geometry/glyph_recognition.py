import math
"""
You are an archaeologist working at an excavation site where your team has found
hundreds of clay tablets containing glyphs written in some ancient language.
Not much is known about the language yet, but you know that there are only
six different glyphs, each of them in the shape of a regular polygon with
one vertex pointing to the right (see Figure 1(a) below). Only the boundary of
each polygon is carved out of the clay.
You want to start analysing the language right away, so you need to get the text on the tablets into some machine readable format. Ideally, you would like to use an OCR (optical character recognition) tool for that, but you do not have one installed on your laptop and there is no internet connection at the site.

Because of this you have devised your own scheme to digitise the ancient writings: for every glyph on a tablet you first find a number of sample points that are in the carved out region, i.e. on the boundary of the polygon. Based on those sample points you then calculate a score for each of the six glyphs and mark the one with the highest score as the recognised glyph.

For a given number of corners k 
 (3 <= k <= 8), the score is computed as follows. Two regular 
-gons are fitted to the sample points, one from the inside and one from the outside, such that the following hold:

Each polygon is centered at the origin, i.e. all vertices have equal distance to (0,0).

Each polygon has a vertex on the positive x-axis.

The inner polygon is the largest such polygon containing none of the sample points.

The outer polygon is the smallest such polygon containing all of the sample points.

The score for k is the ratio of the area of the inner polygon to the area of the outer polygon.
Output the optimal number of corners 
k ( 3 <= k <= 8)
, followed by the score obtained for that value of k.
Your answer will be accepted if the absolute error does not exceed 
10**-6. If several values of result in a score that is within 
10**-6 of the optimal score, any one of them will be accepted.

"""


def get_score(points: list[list[int]]) -> (int, float):
    """
    :param points: list of sample points
    :return: optimal number of corners k and score obtained for that value of k
    """
    if len(points) == 0:
        return 0,0
    if len(points) == 1:
        return 3, 0
    # Main idea: brute force. We try all possible values of k and calculate the score for each of them.
    # Time complexity: O(n^2)
    # Space complexity: O(1) 

    def get_score_for_k(k: int) -> float:
        """
        
        """

    best_score = 0
    best_k = 0
    for k in range(3, 9):
        score = get_score_for_k(k)
        if score > best_score:
            best_score = score
            best_k = k
    return best_k, best_score


n = int(input())
points = []
for i in range(n):
    coor = [float(x) for x in input().split()]
    points.append(coor)
print(get_score(points))