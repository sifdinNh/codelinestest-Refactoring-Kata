# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):


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
        
    def test_it_never_have_to_high_quality(self):
        items_names = ["Good Wine","Backstage passes for Re:Factor","Backstage passes for HAXX"]
        items = [Item(name,2,49) for name in items_names]
        GildedRose(items).update_quality()
        for item in items:
            self.assertEqual(item.quality,50)

    def test_quality_of_good_wine_increases_over_time(self):
        item = Item("Good Wine",2,1)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality,2)

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
    
    def test_that_quality_of_legendary_item_never_change(self):
        item = Item("B-DAWG Keychain",2,80)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality,80)
    
    
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

        
if __name__ == '__main__':
    unittest.main()
