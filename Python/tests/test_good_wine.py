import unittest

from gilded_rose import Item,GildedRose

class GoodWineTest(unittest.TestCase):
    def test_quality_of_good_wine_increases_over_time(self):
        item = Item("Good Wine",2,1)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality,2) 
