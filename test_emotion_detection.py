"""Unit tests for the emotion detector."""
import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check that the dominant emotion matches the expected emotion."""

    def test_joy(self):
        """Joy statement."""
        self.assertEqual(emotion_detector("I am glad this happened")['dominant_emotion'], 'joy')

    def test_anger(self):
        """Anger statement."""
        self.assertEqual(emotion_detector("I am really mad about this")['dominant_emotion'], 'anger')

    def test_disgust(self):
        """Disgust statement."""
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'], 'disgust')

    def test_sadness(self):
        """Sadness statement."""
        self.assertEqual(emotion_detector("I am so sad about this")['dominant_emotion'], 'sadness')

    def test_fear(self):
        """Fear statement."""
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
