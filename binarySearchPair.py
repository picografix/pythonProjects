def mina(a,b,c):
    if a <= min(b,c):
        return a
    elif b <= min(a,c):
        return b
    else:
        return c
def diff(a,b):
    return abs(a-b)
def mixdiff(li):
    n=len(li)
    mixdiffer=10000000
    a=0
    b=0
    for i in range(n//2):
        for j in range(n//2,n):
            if diff(li[i],li[j]) < mixdiffer:
                mixdiffer = diff(li[i],li[j])
                a = li[i]
                b=li[j]
            elif diff(li[i],li[j]) == mixdiffer:
                if li[i] < a:
                    a = li[i]
                    b = li[j]
    return mixdiffer,a,b
def difference(li):
    if len(li)==0:
            return 10000000,0,0
    elif len(li)==1:
            return 10000000,li[0],li[0]
    elif len(li)==2:
        return mixdiff(li)
    else:
        left_differ,a_left,b_left = difference(li[:len(li)//2])
        right_differ,a_right,b_right=difference(li[len(li)//2:])
        mix_differ,a_mix,b_mix =mixdiff(li)
        """if len(li)==0:
            return 10000000,0,0
        elif len(li)==1:
            return 10000000,li[0],li[0]"""
        """if left_differ < right_differ and left_differ < mix_differ :
            return left_differ,a_left,b_left 
        elif left_differ > right_differ and right_differ < mix_differ :
            return right_differ,a_right,b_right
        elif left_differ > mix_differ and right_differ > mix_differ :
            return mix_differ,a_mix,b_mix
        elif"""
        a = mina(left_differ,right_differ,mix_differ)
        if a == left_differ:
            if left_differ==right_differ:
                if min(a_left,b_left) < min(a_right,b_right):
                    return left_differ,a_left,b_left
                else:
                    return right_differ,a_right,b_right
            elif left_differ == mix_differ:
                if min(a_left,b_left) < min(a_mix,b_mix) :
                    return  left_differ,a_left,b_left
                else :
                    return mix_differ,a_mix,b_mix
            else:
                return left_differ,a_left,b_left
        elif a == right_differ:
            if left_differ==right_differ:
                if min(a_left,b_left) < min(a_right,b_right):
                    return left_differ,a_left,b_left
                else:
                    return right_differ,a_right,b_right
            elif right_differ == mix_differ:
                if min(a_left,b_left) < min(a_mix,b_mix) :
                    return  right_differ,a_right,b_right
                else :
                    return mix_differ,a_mix,b_mix
            else:
                return right_differ,a_right,b_right
        elif a == mix_differ:
            if mix_differ==right_differ:
                if min(a_right,b_right) > min(a_mix,b_mix):
                    return mix_differ,a_mix,b_mix
                else:
                    return right_differ,a_right,b_right
            elif left_differ == mix_differ:
                if min(a_left,b_left) < min(a_mix,b_mix) :
                    return  left_differ,a_left,b_left
                else :
                    return mix_differ,a_mix,b_mix
            else:
                return mix_differ,a_mix,b_mix     
print(mina(100,2,1))
print(difference([8,7,3,9]))