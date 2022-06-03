def solution(id_list, report, k):
    # ver2
    '''
    val_ssin = {}
    table = {}
    ans_table = {}
    for id in id_list:
        val_ssin[id] = 0
        ans_table[id] = 0
        table[id] = ['']
        
    report = set(report)
    
    for names in report:
        user, targ = names.split(' ')
        
        val_ssin[targ] += 1
        table[user] += [targ]
        
        #if user not in table:
        #    table[user] = [targ]
        #else:
        #    if targ not in table[user]:
        #        table[user] += [targ]

    #print(val_ssin)
    #print(table)
    
    for idd, val in val_ssin.items():
        if val >= k:
            for name in table.keys():
                if idd in table[name]:
                    ans_table[name] += 1
    
    answer = list(ans_table.values())
    '''
    # ver1
    id_dict = dict.fromkeys(id_list,0)
    val_ssin = {}
    usr_ssin = {}
    
    for i in range(len(report)):
        user = report[i].split()[0]
        ssin_id = report[i].split()[1]
        
            
        if user in usr_ssin:
            if ssin_id in usr_ssin[user]:
                continue
            else:
                usr_ssin[user] += [ssin_id]
        else:
            usr_ssin[user] = [ssin_id]
            
        if ssin_id in val_ssin:
            val_ssin[ssin_id] += 1
        else:
            val_ssin[ssin_id] = 1
            
    for key in val_ssin:
        if val_ssin[key] >= k:
            for name in usr_ssin:
                if key in usr_ssin[name]:
                    id_dict[name] += 1
        
    
    answer = list(id_dict.values())
    
    
    return answer
