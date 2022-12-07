class Solution {
    public String kthLargestNumber(String[] nums, int K) {
        shuffle(nums);
        K--;
        int len =  nums.length, l = 0, r = len - 1;
        int mid = 0;
        while (l <= r) {
            mid = partition(nums, l, r);
            if (mid == K) break;
            if (mid < K) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        } 
        return nums[K];
    }
    

    private int partition(String[] nums, int l, int r) {
        String pivot = nums[l];
        while (l < r) {
            while (l < r && compare(nums[r], pivot) >= 0) r--;
            nums[l] = nums[r];
            while (l < r && compare(nums[l], pivot) < 0) l++;
            nums[r] = nums[l];
        }
        nums[l] = pivot;
        return l;
    }

    private int compare(String p1, String p2) {
        return p1.length() == p2.length() ? p2.compareTo(p1) : Integer.compare(p2.length(), p1.length());
    }
    
    private void shuffle(String a[]) {
        Random random = new Random();
        for(int ind = 1; ind < a.length; ind++) {
            final int r = random.nextInt(ind + 1);
            exch(a, ind, r);
        }
    }
    
    private void exch(String[] a, int i, int j) {
        final String tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
}
