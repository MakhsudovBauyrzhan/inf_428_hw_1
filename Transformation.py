import math
import unittest

def time_to_radians(time_str):
    """Convert a time string 'HH:MM' to radians."""
    hours, minutes = map(int, time_str.split(':'))
    total_hours = hours + minutes / 60
    return (2 * math.pi * total_hours) / 24

def calculate_time_difference(start_time, end_time):
    """Calculate the cyclic time difference between two time strings."""
    start_rad = time_to_radians(start_time)
    end_rad = time_to_radians(end_time)
    
    # Calculate the difference in radians
    diff_rad = end_rad - start_rad
    
    # Normalize the difference to the range [0, 2*pi)
    if diff_rad < 0:
        diff_rad += 2 * math.pi
    
    # Convert radians back to hours
    difference_in_hours = (diff_rad / (2 * math.pi)) * 24
    return difference_in_hours

class TestTimeDifference(unittest.TestCase):

    def test_time_difference_midnight_crossing(self):
        """Test time difference crossing midnight."""
        self.assertAlmostEqual(calculate_time_difference("23:00", "01:00"), 2.0)

    def test_time_difference_same_day(self):
        """Test time difference within the same day."""
        self.assertAlmostEqual(calculate_time_difference("12:00", "14:00"), 2.0)

    def test_time_difference_exactly_24_hours(self):
        """Test time difference exactly 24 hours."""
        self.assertAlmostEqual(calculate_time_difference("01:00", "01:00"), 24.0)

    def test_time_difference_exactly_half_day(self):
        """Test time difference of exactly half a day."""
        self.assertAlmostEqual(calculate_time_difference("12:00", "00:00"), 12.0)

    def test_time_difference_full_circle(self):
        """Test time difference where the end time is one full circle ahead."""
        self.assertAlmostEqual(calculate_time_difference("00:00", "24:00"), 0.0)

    def test_time_difference_five_hours(self):
        """Test time difference of five hours."""
        self.assertAlmostEqual(calculate_time_difference("10:00", "15:00"), 5.0)

if __name__ == '__main__':
    unittest.main()
