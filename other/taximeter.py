
class TaxiMeter:

    def calculate_fare(self, miles, time):
        """
        (**some** mistakes intentional)
        $2.50 minimum
        If less than 50 miles then 25c a minute else then $5 surcharge
        :param miles travelled, time taken:
        :return total cost :
        """
        timecost = 2.5 + (time * 0.25)
        distcost = 0
        if(miles > 50):
            distcost = "$5"
        return timecost + distcost
