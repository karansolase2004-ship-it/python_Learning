def formatname(f_name, l_name) : 
    f_name.title()
    l_name.title()
    print(f"{f_name, l_name}")

formatname("Karan", "Solase")

# f stand for formatted 

def formatname2(f_name, l_name) : 
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # we can return formatted string aswell  
    return f"{formatted_f_name} {formatted_l_name}"


print(formatname2("Karan", "Solase"))