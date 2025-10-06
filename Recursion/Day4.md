## SubSequence 

## 📌 What is a Subsequence?

A **subsequence** of an array or string is a sequence that can be formed by **deleting zero or more elements without changing the relative order** of the remaining elements.

---

### ✅ Example

For the array: `A = [3, 1, 2]`

All possible subsequences are:

```python
3 1 2
3 1
3 2
3
1 2
1
2
{}
```

Total number of subsequences = **2ⁿ** (where `n` is the number of elements)

---

### 🔄 Subsequence vs Subarray

| Concept     | Contiguous Elements? | Order Preserved? | Example from `[3,1,2]` |
|------------|-----------------------|------------------|------------------------|
| Subsequence | ❌ No                | ✅ Yes           | `[3,2]` ✅              |
| Subarray    | ✅ Yes               | ✅ Yes           | `[1,2]` ✅, but `[3,2]` ❌ |

---

### ✨ Applications

- ✅ **Longest Increasing Subsequence (LIS)**
- ✅ **Longest Common Subsequence (LCS)**
- ✅ **Power Set Generation**
- ✅ **Subset / Sum Problems (Backtracking & DP)**

---

#### Example  code 

```python

def print_subsequences(ind, ds, arr, n):
    if ind == n:
        if ds:
            print(" ".join(map(str, ds)))
        else:
            print("{}")   # To match the behavior of printing "{}" for empty subsequence
        return
    
    # Take / pick the element at current index
    ds.append(arr[ind])
    print_subsequences(ind + 1, ds, arr, n)
    ds.pop()   # Backtrack

    # Not take / skip the element
    print_subsequences(ind + 1, ds, arr, n)


if __name__ == "__main__":
    arr = [3, 1, 2]
    n = len(arr)
    ds = []
    print_subsequences(0, ds, arr, n)

```

### OUTPUT

```python

3 1 2
3 1
3 2
3
1 2
1
2
{}


```

