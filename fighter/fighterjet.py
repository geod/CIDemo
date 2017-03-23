from collections import namedtuple

class WeaponsSystem:

    def fire(self, radar_signature):
        # peow peow
        # again - in the production system this would be implemented
        # we would want to mock
        pass


class RadarSystem:

    def __init__(self):
        self.data = {}

    def scan(self):
        # in a real system this would be implemented
        # perhaps it would expect to call sensors or controllers
        pass

    def get_closest(self):
        closest = None
        for x in self.data:
            if closest is None or x.distance < closest.distance:
                closest = x
        return x


RadarSignature = namedtuple('RadarSignature', 'id type distance friendly')


class FighterJet:

    def __init__(self, radar_data, weapons_system):
        self.radar_data = radar_data
        self.weapons_system = weapons_system

    def reassess(self):
        plane = self.radar_data.get_closest()
        if plane is not None and not plane.friendly:
            self.weapons_system.fire(plane)