def solution(num_list):
    answer = 0
    
    summation = sum(num_list)**2
    mat = 1
    
    for n in num_list:
        mat *= n
        
    if mat < summation:
        answer = 1
    return answer