import unittest

from gilded_rose import Item,GildedRose

class NormalItemTest(unittest.TestCase):
    def test_it_decrease_quality_of_normal_item(self):
        normal_item = Item("normal", 2, 10)
        items = [normal_item]
        GildedRose(items).update_quality()
        self.assertEqual(normal_item.quality,9)

    def test_quality_decreases_faster_after_sellby_date(self):
        normal_item = Item("normal", 0, 10)
        items = [normal_item]
        GildedRose(items).update_quality()
        self.assertEqual(normal_item.quality,8)

    def test_the_quality_it_never_negative_for_normal_item(self):
        normal_item = Item("normal", 2, 0)
        items = [normal_item]
        GildedRose(items).update_quality()
        self.assertEqual(normal_item.quality,0)