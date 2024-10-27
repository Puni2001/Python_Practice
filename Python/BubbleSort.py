nums = [8,9,7,0,5,6,7,6,0,1]

def BubbleSort(nums):
    for i in range(nums[0],len(nums)-1):
        for j in range(len(nums)-1):
            if nums[i] > nums[j+1]:
                nums[i],nums[j+1] = nums[j+1],nums[i]
    print(nums)
    return nums

if __name__ == "__main__":
    BubbleSort(nums)