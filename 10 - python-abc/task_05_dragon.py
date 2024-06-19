#!/usr/bin/ptyhon3
"""Design two mixin classes
Your aim is to show that a Dragon instance can both swim and fly.
"""


class SwimMixin:
    """swmi class"""
    def swim(self):
        """print"""
        print("The creature swims!")


class FlyMixin:
    """sly class"""
    def fly(self):
        """print fly"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """mix class fly and swim"""
    def roar(self):
        """print roar"""
        print("The dragon roars!")

    def scratch(self):
        """print scratch"""
        print("the dragon scratch your face!")
    
    def moonwalk(self):
        """print dragon do the moonwalk"""
        print("the dragon does the moonwalk in front of you Oo")
