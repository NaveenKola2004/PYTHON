def solution(s):
    l=list(s)
    l2=[]
    for i in l:
        if i not in l2:
            l2.append(i)
    print(len(l2))
solution("abcabcbb")