''''1. Two Sum, assuming we have two numbers in a list which adds to target,

if the data set is small, we can use index_of instead of dictionary
using dictionary to store key and index'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key_index_mapping = {}
        for index, value in enumerate(nums):
            if target - value in key_index_mapping:
                return [key_index_mapping[target - value], index]
            else:
                key_index_mapping[value] = index