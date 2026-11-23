class ProductOfNumbers:

    def __init__(self):
        # Stores running products of non-zero elements since the last zero.
        # Sentinel 1 allows dividing by the element right before the k-window.
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Any window crossing a zero will evaluate to 0
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k reaches into or before the most recent zero, product is 0
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]