from __future__ import annotations

class Kangaroo:
    def __init__(self, pouch_contents=None)->Kangaroo:
        if pouch_contents:
            self.pouch_contents = pouch_contents
        else:
            self.pouch_contents = []

    def __str__(self):
        r_str = ''
        for item in self.pouch_contents:
            r_str = r_str + " " + object.__str__(item)
        return r_str

    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)
        # if isinstance(obj, Kangaroo):
        #     for item in obj.pouch_contents:
        #         self.pouch_contents.append(item)
        # else:
        #     self.pouch_contents.append(obj)


    
if __name__ == '__main__':
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch('gloves')
    roo.put_in_pouch('mittens')
    kanga.put_in_pouch(roo)
    print(kanga)
    print(roo)