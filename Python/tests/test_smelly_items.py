import unittest

from gilded_rose import Item,GildedRose

class SmellyItemTest(unittest.TestCase):
    def test_it_decrease_quality_by_normal_rate(self):
        semlly_items = ["Duplicate Code", "Long Methods", "Ugly Variable Names"]
        items = [Item(item, 2, 2) for item in semlly_items]
        GildedRose(items).update_quality()
        for item in items:
            self.assertEqual(item.quality,0)

    def test_quality_decreases_faster_after_sellby_date(self):
        semlly_items = ["Duplicate Code", "Long Methods", "Ugly Variable Names"]
        items = [Item(item, 2, 4) for item in semlly_items]
        GildedRose(items).update_quality()
        for item in items:
            self.assertEqual(item.quality,0)

    def test_the_quality_it_never_negative_for_normal_item(self):
        semlly_items = ["Duplicate Code", "Long Methods", "Ugly Variable Names"]
        items = [Item(item, 2, 0) for item in semlly_items]
        GildedRose(items).update_quality()
        for item in items:
            self.assertEqual(item.quality,0)