# ------ #
# Graphs #
# ------ #

class MarineAnimalNode(object):
    """Node in a graph representing a marine animal."""

    def __init__(self, name, prey=None):
        """Create a marine animal node with prey"""

        prey = prey or set()
        assert isinstance(prey, set), \
            "prey must be a set!"
        self.name = name
        self.prey = set(prey)

    def __repr__(self):
        """Debugging-friendly representation"""

        return "<MarineAnimalNode: {}>".format(self.name)


class MarineFoodChainGraph(object):
    """Graph holding marine animals and their predator/prey relationships."""

    def __init__(self):
        """Create an empty graph"""

        self.nodes = set()

    def __repr__(self):
        """Debugging-friendly representation"""

        return "<MarineFoodChainGraph: {}>".format([n.name for n in self.nodes])

    def add_animal(self, animal):
        """Add an animal to our graph"""

        self.nodes.add(animal)

    def add_animals(self, animals):
        """Add animals to our graph"""

        for animal in animals:
            self.nodes.add(animal)

    def is_prey(self, animal1, animal2):
        """Determine whether animal1 is prey of animal2

        >>> krill = MarineAnimalNode('krill')
        >>> squid = MarineAnimalNode('squid', set([krill]))
        >>> seal = MarineAnimalNode('seal', set(['squid']))
        >>> baleen_whale = MarineAnimalNode ('baleen whale', set([krill]))
        >>> orca = MarineAnimalNode('orca', set([seal, baleen_whale]))
        >>> aquarium = MarineFoodChainGraph()
        >>> aquarium.add_animals([krill, squid, seal, baleen_whale, orca])
        >>> aquarium.is_prey(krill, baleen_whale)
        True
        >>> aquarium.is_prey(squid, krill)
        False
        >>> aquarium.is_prey(krill, orca)
        False

        """

        if animal1 in animal2.prey:
            return True
        else:
            return False

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
