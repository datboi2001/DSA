class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        """
        :param coordinates: List[List[int]] a list of coordinates
        :return: true if the coordinates form a straight line
        """
        if len(coordinates) == 2:
            return True
        # There are 3 cases:
        # 1. The line is vertical
        # 2. The line is horizontal
        # 3. The line is diagonal

        # Case 1: The line is vertical
        if coordinates[0][0] == coordinates[1][0]:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
            return True
        # Case 2: The line is horizontal
        if coordinates [0][1] == coordinates[1][1]:
            for i in range(2, len(coordinates)):
                if coordinates[i][1] != coordinates[0][1]:
                    return False
            return True
        # Case 3: The line is diagonal
        # y = mx + b
        # m = (y2 - y1) / (x2 - x1)

        m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        b = coordinates[0][1] - m * coordinates[0][0]
        for i in range(2, len(coordinates)):
            if coordinates[i][1] != m * coordinates[i][0] + b:
                return False
        return True 
