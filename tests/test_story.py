import unittest


class TestStory(unittest.TestCase):
    def setUp(self):
        with open('../story.txt') as file:
            self.story = ''.join(file.readlines())

    def test_once_upon(self):
        self.assertTrue(self.story.startswith('Once upon a time'))

    def test_the_end(self):
        self.assertTrue(self.story.endswith('The End'))

    def test_line_length(self):
        for line in self.story.split('\n'):
            self.assertLessEqual(len(line), 80)

    def test_plot_order(self):
        part_one, part_two = self.story.split('too cold')
        self.assertIn('too hot', part_one)
        self.assertIn('just right', part_two)

        part_one, part_two = self.story.split('too big, too')
        self.assertIn('too big!', part_one)
        self.assertIn('just right', part_two)

        part_one, part_two = self.story.split('too soft')
        self.assertIn('too hard', part_one)
        self.assertIn('just right', part_two)
