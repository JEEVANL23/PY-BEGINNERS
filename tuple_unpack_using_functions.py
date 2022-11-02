work_hours = [("jeevan",10),("kumar",12),("ajith",131)]

def employee_check(work_hours):
    current = 0
    employee = ''
    
    for employe,hours in work_hours:
        if hours > current:
            current = hours
            employee = employe
        else:
            pass    
    print(employee,current)
    
employee_check(work_hours)
    