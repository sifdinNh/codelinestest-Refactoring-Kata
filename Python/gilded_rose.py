# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "B-DAWG Keychain":
                continue
            item.sell_in = item.sell_in - 1  
            #update quality statement
            if item.name == "Good Wine" :
                    self.increment(item)
            elif item.name in ["Backstage passes for Re:Factor" ,"Backstage passes for HAXX"]:
                       self.increment(item)
                       if item.sell_in < 11:
                           self.increment(item)
                       if item.sell_in < 6:
                           self.increment(item)
            else:
                self.decrement(item)

            # passed sell_in statement
            if item.sell_in < 0:
                if item.name == "Good Wine":
                    self.increment(item)
                elif item.name in ["Backstage passes for Re:Factor" ,"Backstage passes for HAXX"]:
                        item.quality = item.quality - item.quality
                else:
                    self.decrement(item)
                    
    def increment(self,item):
        if item.quality < 50:
            item.quality = item.quality + 1
            
    def decrement(self,item):
        if item.quality > 0:
            item.quality = item.quality - 1
            


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
