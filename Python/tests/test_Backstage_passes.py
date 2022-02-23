import unittest
from gilded_rose import Item, GildedRose

class BackstagePassesTest(unittest.TestCase):
    def test_quality_of_Backstage_passes_increases_with_less_than_5days(self):
        items_names = ["Backstage passes for Re:Factor","Backstage passes for HAXX"]
        items = [Item(name,4,1) for name in items_names]
        GildedRose(items).update_quality()
        for item in items:
            self.assertEqual(item.quality,4)

    def test_quality_of_Backstage_passes_increases_with_less_than_10days(self):
        items_names = ["Backstage passes for Re:Factor","Backstage passes for HAXX"]
        items = [Item(name,9,1) for name in items_names]
        GildedRose(items).update_quality()
        for item in items:
            self.assertEqual(item.quality,3)
    def test_quality_of_Backstage_passes_decreases_on_day_of_concert(self):
        items_names = ["Backstage passes for Re:Factor","Backstage passes for HAXX"]
        items = [Item(name,0,10) for name in items_names]
        GildedRose(items).update_quality()
        for item in items:
            self.assertEqual(item.quality,0)