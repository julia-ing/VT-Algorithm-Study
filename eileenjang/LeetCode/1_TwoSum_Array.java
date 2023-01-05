import java.util.*;

// Brute Force
class Solution {
    public int[] twoSum(int[] nums, int target) {

        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }

        return null;
    }
}

// TC: O(n^2); SC: O(1)

// HashMap
class Solution2 {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            Integer idx = map.get(diff);

            if (map.containsKey(target - nums[i])) {
                return new int[] {idx, i};
            }

            map.put(nums[i], i);
        }

        return null;
    }
}

// TC: O(n); SC: O(n)
