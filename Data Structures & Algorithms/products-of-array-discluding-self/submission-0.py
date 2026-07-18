class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productsList: list[int] = list()
        for index, number in enumerate(nums):
            product: int = 1
            for i, n in enumerate(nums):
                if i != index:
                    product *= n
            productsList.append(product)
        return productsList