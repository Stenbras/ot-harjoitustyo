import unittest
import frequencyToNote as frqTN

class TestFrqToNote(unittest.TestCase):

    def test_get_frequency_note_note(self):
        self.assertEqual(frqTN.GetFrequencyNote(440)[0],"A")
        
    def test_get_frequency_note_octave(self):
        self.assertEqual(frqTN.GetFrequencyNote(440)[1],4)
    
    def test_tune_frequency_to_note(self):
        self.assertEqual(frqTN.TuneFrequencyToNote(["A",4]),440)
        
