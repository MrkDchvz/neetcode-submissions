class Solution {

    public String encode(List<String> strs) {
        String result = "";
        for (String s : strs) {
            result += Integer.toString(s.length()) + "#" + s;  
        }
        System.out.println(result);
        return result;
    }

    public List<String> decode(String str) {
        List<String> list = new ArrayList();
        int i = 0;
        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') {
                j += 1;
            }
            int length = Integer.parseInt(str.substring(i, j));
            list.add(str.substring(j + 1, j + 1 + length));
            i = j + length + 1;
        
        }
        return list;
    }
}
