class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for i in range(n)] for j in range(n)]
        results_list = [i for i in range(1, n ** 2 + 1)]
        left_index = 0
        right_index = len(result[0]) - 1
        top_index = 0
        bottom_index = len(result) -1
        
        while left_index <= right_index and top_index <= bottom_index:
            for i in range(left_index, right_index  + 1):
                result[top_index][i] = results_list.pop(0)

            top_index += 1

            for i in range(top_index, bottom_index + 1):
                result[i][right_index] = results_list.pop(0)

            right_index -= 1

            if top_index <= bottom_index:
                for i in range(right_index, left_index - 1, -1):
                    result[bottom_index][i] = results_list.pop(0)

            bottom_index -= 1

            if left_index <= right_index:
                for i in range(bottom_index, top_index - 1, -1):
                    result[i][left_index] = results_list.pop(0)

            left_index += 1

        return result