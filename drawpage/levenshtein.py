from Levenshtein import distance as levdistance

# Return: alphabet labels for each activity within a control flow
# Input: list = list of activities within a control flow
#def label_activities(list: list) -> list:

# Return: distances[[]] between all pairs of control flows (represented by strings) in a list of control flows
# Input: list = list of control flows
def get_levenshtein_distances(list: list) -> list:
    distances = []
    # First pointer, outer loop: traverse each word in the list once
    # The number of inner lists within distances = the number of strings in the first iteration
    for firstStrings in list:
        sub_distances = []
        # Second pointer, inner loop: traverse each word for each time it is traversed in the outer loop
        # The number of output booleans = the number of strings in the second iteration
        for secondStrings in list:
            sub_distances.append(levdistance(firstStrings, secondStrings))
        distances.append(sub_distances)
    #print(distances)
    return distances

# Example list to test
#list = ['AAAABBBCBDB', 'AAABCBAD', 'AAAABBBCBDB', 'AAAABBBCBEG', 'AAAABBBCBDB', 'AAAABCBAD']

# For testing
#get_levenshtein_distances(list)