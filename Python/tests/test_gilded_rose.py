# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
        
    def test_it_never_have_to_high_quality(self):
        items_names = ["Good Wine","Backstage passes for Re:Factor","Backstage passes for HAXX"]
        items = [Item(name,2,49) for name in items_names]
        GildedRose(items).update_quality()
        for item in items:
            self.assertEqual(item.quality,50)   
    
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

        
if __name__ == '__main__':
    unittest.main()
