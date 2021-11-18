#from django.test import TestCase
from kmedoids import cluster_kmedoids
from agglomerative import cluster_agglomerative
from distance_techniques import LevenshteinDistance, BooleanDistance, EuclideanDistance
import numpy as np

# Create your tests here.


lev_activities = [['eat', 'sleep', 'rave', 'repeat'],
                   ['eat', 'sleep', 'rave', 'Not repeat'],
                   ['eat', 'sleep', 'Not rave', 'Not repeat'],
                   ['eat', 'Not sleep', 'Not rave', 'Not repeat'],
                   ['Not eat', 'Not sleep', 'Not rave', 'Not repeat']]

bool_activities = ['Not eat', 'Not sleep', 'Not rave', 'Not repeat', 'eat', 
                    'Not sleep', 'Not rave', 'Not repeat', 'Not eat', 'Not sleep', 
                    'Not rave', 'Not repeat', 'eat', 'Not sleep', 'Not rave', 
                    'Not repeat']

euc_activities = np.random.randint(20, size=(3,35))


test_lev = LevenshteinDistance(lev_activities).get_levenshtein_distances(lev_activities)
print("Calculated Levenshtein distances:\n", test_lev, "\n-----------")
test_bool = BooleanDistance(bool_activities).get_boolean_distances(bool_activities)
print("Calculated Boolean distances:\n", test_bool, "\n-----------")
test_euc = EuclideanDistance(euc_activities).get_euclidean_distances(euc_activities)
print("Calculated Euclidean distances:\n", test_euc, "\n-----------")

# Test k_medoids

print("Calculated clusters for k-medoids clustering with Levenshtein distances:\n", cluster_kmedoids(distance_matrix=test_lev), "\n-----------")
print("Calculated clusters for k-medoids clustering with Boolean distances:\n", cluster_kmedoids(distance_matrix=test_bool), "\n-----------")
print("Calculated clusters for k-medoids clustering with Euclidean distances:\n", cluster_kmedoids(distance_matrix=test_euc), "\n-----------")

# Test agglomerative

print("Calculated clusters for hierarchical clustering with Levenshtein distances:\n", cluster_agglomerative(distance_matrix=test_lev), "\n-----------")
print("Calculated clusters for hierarchical clustering with Boolean distances:\n", cluster_agglomerative(distance_matrix=test_bool), "\n-----------")
print("Calculated clusters for hierarchical clustering with Euclidean distances:\n", cluster_agglomerative(distance_matrix=test_euc), "\n-----------")