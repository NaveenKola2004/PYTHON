def solution(l1,l2):
    l1_sum=0
    l2_sum=0
    for i in range(len(l1)-1,-1,-1):
        l1_sum=(l1_sum*10)+l1[i]
    for k in range(len(l2)-1,-1,-1):
        l2_sum=(l2_sum*10)+l2[k]
    ou=[]
    sum=l1_sum+l2_sum
    while(sum>0):
        digit=sum%10
        ou.append(digit)
        sum//=10
    print(ou)
solution([2,4,3],[5,6,4]) # [7,0,8]