// Problem Name: 380. Insert Delete GetRandom O(1)
// Problem Link: https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet {

    private Map<Integer,Integer> map;
    private ArrayList<Integer> list;

    public RandomizedSet() {
        map = new HashMap<>();
        list = new ArrayList<>();
    }
    
    public boolean insert(int val) {
        if (map.containsKey(val)) return false;
        list.add(val);
        map.put(val,list.size()-1);
        return true;
    }
    
    public boolean remove(int val) {
        if (!map.containsKey(val)) return false;
        int newValIndex = map.get(val);
        list.set(newValIndex, list.get(list.size()-1));
        map.put(list.get(newValIndex), newValIndex);
        list.remove(list.size()-1);
        map.remove(val);
        return true;
    }
    
    public int getRandom() {
        Random rand = new Random();
        return list.get(rand.nextInt(list.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
