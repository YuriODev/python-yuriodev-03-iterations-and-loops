
import unittest
import subprocess
import os

class TestExercise23(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_23.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_average_sequence_ending_with_0(self):
        output = self.run_exercise("3\n4\n5\n0\n")
        self.assertAlmostEqual(float(output.strip()), 4.0, places=1)

    def test_average_sequence_1_to_5_ending_with_0(self):
        output = self.run_exercise("1\n2\n3\n4\n5\n0\n")
        self.assertAlmostEqual(float(output.strip()), 3.0, places=1)

    def test_average_sequence_10_to_50_by_10_ending_with_0(self):
        output = self.run_exercise("10\n20\n30\n40\n50\n0\n")
        self.assertAlmostEqual(float(output.strip()), 30.0, places=1)

if __name__ == '__main__':
    unittest.main()
