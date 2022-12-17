class Solution {
public:
    int maximumProduct(vector<int>& nums, int k) {
            make_heap(begin(nums), end(nums), greater<int>());
    while (k--) {
        pop_heap(begin(nums), end(nums), greater<int>());
        ++nums.back();
        push_heap(begin(nums), end(nums), greater<int>());        
    }
    return accumulate(begin(nums), end(nums), 1LL, [](long long res, int n) { return res * n % 1000000007; });

    }
};