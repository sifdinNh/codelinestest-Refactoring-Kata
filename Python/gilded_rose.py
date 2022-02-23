# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "B-DAWG Keychain":
                continue
            item.sell_in = item.sell_in - 1  
            
            if item.quality < 50 :
                if item.name == "Good Wine" :
                        item.quality = item.quality + 1
                elif item.name in ["Backstage passes for Re:Factor" ,"Backstage passes for HAXX"]:
                       item.quality = item.quality + 1
                       if item.sell_in < 11:
                           if item.quality < 50:
                               item.quality = item.quality + 1
                       if item.sell_in < 6:
                           if item.quality < 50:
                               item.quality = item.quality + 1
                elif item.quality > 0:
                    item.quality = item.quality - 1

            if item.sell_in < 0:
                if item.name == "Good Wine":
                    if item.quality < 50:
                        item.quality = item.quality + 1
                elif item.name in ["Backstage passes for Re:Factor" ,"Backstage passes for HAXX"]:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality > 0:
                                item.quality = item.quality - 1
            


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
