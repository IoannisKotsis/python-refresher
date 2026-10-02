def make_alert(limit):
    def fever(n):
        return n > limit

    return fever


fever = make_alert(38)
fever(38)
