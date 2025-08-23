def solution(data, ext, val_ext, sort_by):
    temp_list = []
    answer = []
    data_type = {
        'code' : 0 ,
        'date' : 1,
        'maximum' : 2,
        'remain' : 3
    }
    for i in data:
        if i[data_type[ext]] < val_ext:
            temp_list.append(i)
    
    answer = sorted(temp_list, key = lambda x:x[data_type[sort_by]])
    
    return answer
    
            
    
    return answer