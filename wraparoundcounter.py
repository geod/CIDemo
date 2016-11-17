

class WrapAroundCounter:

    def __init__(self, maximum):
        self.max = maximum

    def increment(self, n):
        """
        Wrap around counter - (horrible code)
        https://medium.com/@bartobri/applying-the-linus-tarvolds-good-taste-coding-requirement-99749f37684a#.mqleno435
        :param n:
        :return 1..9 then n+1 else 1 :
        """
        if n == max:
            n = 1
        else:
            n += 1
        return n