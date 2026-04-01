class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;  // slow pointer
        
        for (int i = 0; i < nums.size(); i++) {  // fast pointer
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }
        
        return k;
    }
};