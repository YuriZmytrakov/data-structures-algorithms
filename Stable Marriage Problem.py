#Yurii Zmytrakov, student number: 501074085

#Question 1c:

def orders(arr, start, end):
    if len(start) < 1: 
        arr.append(end)
        return arr
    else:
        n = len(start)
        i = 0
        while i <= n-1:
                next_end = end + start[i:i+1]
                next_start = start[:i] + start[i+1:]
                i = i+1
                orders(arr, next_start, next_end) 
    return arr

#creating all possible combinations of women
women_list = (orders([], ['w0','w1','w2','w3','w4','w5','w6'], []))

#creating the list of man as standard and it does not change
man_list = ['m0','m1','m2','m3','m4','m5','m6']

#creating the dictionary as input with all possible marriages of men with women: the output is list of dictionaries 
# example of the list {'w0': 'm0', 'w1': 'm1', 'w2': 'm2', 'w3':'m3', 'w4':'m4', 'w5': 'm5', 'w6', 'm6'}
final = []
for i in women_list:
    dic_a = dict(zip(i, man_list))
    final.append(dic_a)


 
men_prefers = {
 'm0': ['w5', 'w6', 'w4', 'w2', 'w0', 'w3', 'w1'],
 'm1': ['w0', 'w5', 'w1', 'w2', 'w4', 'w3', 'w6'],
 'm2': ['w3', 'w6', 'w1', 'w2', 'w5', 'w0', 'w4'],
 'm3': ['w1', 'w2', 'w5', 'w0', 'w6', 'w4', 'w3'],
 'm4': ['w6', 'w0', 'w2', 'w4', 'w3', 'w1', 'w5'],
 'm5': ['w2', 'w1', 'w4', 'w0', 'w3', 'w6', 'w5'],
 'm6': ['w5', 'w6', 'w4', 'w2', 'w0', 'w1', 'w3']}

women_prefers = {
 'w0': ['m0', 'm4', 'm3', 'm1', 'm5', 'm2', 'm6'],
 'w1': ['m5', 'm1', 'm4', 'm6', 'm3', 'm2', 'm0'],
 'w2': ['m1', 'm5', 'm4', 'm2', 'm6', 'm3', 'm0'],
 'w3': ['m0', 'm1', 'm4', 'm5', 'm3', 'm2', 'm6'],
 'w4': ['m5', 'm2', 'm4', 'm1', 'm0', 'm6', 'm3'],
 'w5': ['m5', 'm6', 'm3', 'm2', 'm0', 'm1', 'm4'],
 'w6': ['m2', 'm6', 'm5', 'm3', 'm4', 'm0', 'm1']}
 
guys = sorted(men_prefers.keys())
gals = sorted(women_prefers.keys())
 
def FindAllStableMatchings(engaged):
    stable_marriage_counter = 0
    unstable_marriage_counter = 0
    inverse = dict((v,k) for k,v in engaged.items())
    for woman, man in engaged.items():
        women_prefers_l = women_prefers[woman]
        women_prefers_better = women_prefers_l[:women_prefers_l.index(man)]
        helikes = men_prefers[man]
        for man in women_prefers_better:
            menwomen = inverse[man]
            men_like = men_prefers[man]
            if men_like.index(menwomen) > men_like.index(woman):
                unstable_marriage_counter = unstable_marriage_counter +1
            else:
                stable_marriage_counter = stable_marriage_counter + 1
    print('stable', stable_marriage_counter)
    print('unstable', unstable_marriage_counter)
    return stable_marriage_counter

#element by element, we are checking if this combination is stable or not, and incrementing the counter if true
for marriage_dict in final:
    stable_counter = FindAllStableMatchings(marriage_dict)

print('number of stable marriages ->', stable_counter)