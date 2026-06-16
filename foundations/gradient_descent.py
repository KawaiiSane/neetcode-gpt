class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        for i in range(iterations):
            d = 2 * init
            init = init - d * learning_rate

        return round(init,5)