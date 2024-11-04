import random
import unittest

# Constants
DEPARTMENTS = ['Engineering', 'Marketing', 'Finance', 'HR', 'Science']

def generate_random_data(num_users):
    """Generate random threat scores and importance for a given number of users."""
    threat_scores = [random.randint(0, 90) for _ in range(num_users)]
    importance = random.randint(1, 5)
    return threat_scores, importance

def calculate_mean(threat_scores):
    """Calculate the mean threat score from a list of threat scores."""
    return sum(threat_scores) / len(threat_scores) if threat_scores else 0

def aggregate_threat_score(departments):
    """
    Calculate the aggregated cybersecurity threat score based on the mean scores 
    and importance of each department.
    """
    total_importance = sum(dep['importance'] for dep in departments)
    aggregated_score = sum(
        (calculate_mean(dep['scores']) * dep['importance']) / total_importance
        for dep in departments
    )
    return aggregated_score

class TestCybersecurityAggregation(unittest.TestCase):

    def test_mean_calculation(self):
        # Test mean calculation with a normal case
        scores = [10, 20, 30, 40, 50]
        self.assertEqual(calculate_mean(scores), 30)

    def test_empty_mean(self):
        # Test mean calculation with an empty list
        scores = []
        self.assertEqual(calculate_mean(scores), 0)

    def test_aggregate_score_with_equal_importance(self):
        # All departments have the same importance and threat scores
        departments = [
            {'scores': [10, 20, 30], 'importance': 1},
            {'scores': [20, 30, 40], 'importance': 1},
            {'scores': [30, 40, 50], 'importance': 1},
            {'scores': [40, 50, 60], 'importance': 1},
            {'scores': [50, 60, 70], 'importance': 1},
        ]
        self.assertAlmostEqual(aggregate_threat_score(departments), 40)

    def test_aggregate_score_with_varying_importance(self):
        # Departments have varying importance
        departments = [
            {'scores': [10, 20, 30], 'importance': 2},
            {'scores': [20, 30, 40], 'importance': 3},
            {'scores': [30, 40, 50], 'importance': 1},
        ]
        # Calculation:
        # Department 1 mean = 20, weighted = 20 * 2 = 40
        # Department 2 mean = 30, weighted = 30 * 3 = 90
        # Department 3 mean = 40, weighted = 40 * 1 = 40
        # Total importance = 2 + 3 + 1 = 6
        # Aggregated score = (40 + 90 + 40) / 6 = 22.5
        self.assertAlmostEqual(aggregate_threat_score(departments), 22.5)

    def test_random_data_integration(self):
        # Test integration with random data
        departments = []
        for _ in range(len(DEPARTMENTS)):
            num_users = random.randint(10, 200)
            scores, importance = generate_random_data(num_users)
            departments.append({'scores': scores, 'importance': importance})
        # Just ensure no exceptions occur; actual values will vary
        try:
            aggregate_threat_score(departments)
        except Exception as e:
            self.fail(f"aggregate_threat_score raised {type(e).__name__} unexpectedly: {e}")

if __name__ == '__main__':
    unittest.main()
