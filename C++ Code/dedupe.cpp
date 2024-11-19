#include <iostream>
#include <vector>

//Given an integer array nums sorted in non-decreasing order, remove the duplicates 
//in-place such that each unique element appears only once. The relative order of the 
//elements should be kept the same. Then return the number of unique elements in nums.
//Consider the number of unique elements of nums to be k, to get accepted, you need to 
//do the following things:
//Change the array nums such that the first k elements of nums contain the unique elements 
//in the order they were present in nums initially. The remaining elements of nums are not 
//important as well as the size of nums.Return k.
int removeDuplicates(std::vector<int>& nums) {
    if (nums.empty()) {
        return 0;
    }
    
    int k = 1; // The first element is always unique
    for (int i = 1; i < nums.size(); ++i) {
        if (nums[i] != nums[k - 1]) {
            nums[k] = nums[i];
            ++k;
        }
    }
    
    return k;
}

int main() {
    std::vector<int> nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int k = removeDuplicates(nums);
    std::cout << "Number of unique elements: " << k << std::endl;
    std::cout << "Modified array: ";
    for (int i = 0; i < k; ++i) {
        std::cout << nums[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}
