def solution(chicken):
    
    cou=chicken
    service_c=0
    
    while cou>=10:
        buy_c=cou//10
        service_c+=buy_c
        cou=buy_c+(cou%10)

        if cou==10:
            buy_c+=1
    return service_c
        