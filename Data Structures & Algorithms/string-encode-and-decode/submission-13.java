class Solution {

    public String encode(List<String> strs) {
        String join = String.join(";", strs);
        System.out.println(join);
        return join;
    }

    public List<String> decode(String str) {
        List<String> list = new ArrayList();
        if (str == "") {
            return list;
        }
        String[] strarr = str.split(";");
        for (String s : strarr ) {
            list.add(s);
        }
        return list;
    }
}
