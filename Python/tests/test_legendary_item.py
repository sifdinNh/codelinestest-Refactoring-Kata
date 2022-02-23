import unittest

from gilded_rose import Item,GildedRose

class LegandaryItemTest(unittest.TestCase):
    def test_that_quality_of_legendary_item_never_change(self):
        item = Item("B-DAWG Keychain",2,80)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality,80)
