import java.util.*;

public class java {

    // Function signature should not be modified
    public static int solve(int n, int[][] edges, int[] siteGuardians, int m) {
        List<List<Integer>> tree = new ArrayList<>();
        for (int i = 0; i < n; i++) tree.add(new ArrayList<>());

        boolean[] hasParent = new boolean[n];
        for (int[] e : edges) {
            tree.get(e[0]).add(e[1]);
            hasParent[e[1]] = true;
        }

        // Find root
        int root = -1;
        for (int i = 0; i < n; i++) {
            if (!hasParent[i]) {
                root = i;
                break;
            }
        }

        // Build left and right children
        int[] left = new int[n];
        int[] right = new int[n];
        Arrays.fill(left, -1);
        Arrays.fill(right, -1);
        for (int i = 0; i < n; i++) {
            if (tree.get(i).size() > 0) left[i] = tree.get(i).get(0);
            if (tree.get(i).size() > 1) right[i] = tree.get(i).get(1);
        }

        // Inorder traversal
        List<Integer> inorder = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        int curr = root;
        while (curr != -1 || !stack.isEmpty()) {
            while (curr != -1) {
                stack.push(curr);
                curr = left[curr];
            }
            curr = stack.pop();
            inorder.add(curr);
            curr = right[curr];
        }

        // Mth site (1-based)
        int siteIndex = inorder.get(m - 1);
        return siteGuardians[siteIndex];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine().trim();
        sc.close();

        // Split input by semicolon
        String[] parts = input.split(";");
        int n = Integer.parseInt(parts[0].trim());

        // Parse guardians
        String[] guardianStr = parts[1].trim().split(" ");
        int[] siteGuardians = new int[n];
        for (int i = 0; i < n; i++) {
            siteGuardians[i] = Integer.parseInt(guardianStr[i]);
        }

        // Parse edges
        int edgeCount = n - 1;
        int[][] edges = new int[edgeCount][2];
        for (int i = 0; i < edgeCount; i++) {
            String[] e = parts[i + 2].trim().split(" ");
            edges[i][0] = Integer.parseInt(e[0]);
            edges[i][1] = Integer.parseInt(e[1]);
        }

        // Festival site
        int m = Integer.parseInt(parts[parts.length - 1].trim());

        System.out.println(solve(n, edges, siteGuardians, m));
    }
}
