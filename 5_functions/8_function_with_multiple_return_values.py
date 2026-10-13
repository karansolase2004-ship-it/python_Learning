import statistics

def mean_median_mode1(list1) :
    # below return statement return values bind in tuple
    return statistics.mean(list1), statistics.median(list1), statistics.mode(list1)

print(mean_median_mode1([3, 5, 45, 3, 2, 1, 89]))

def mean_median_mode2(list1) :
    return statistics.mean(list1), statistics.median(list1), statistics.mode(list1)

# capturing values in 3 different variables 
a, b, c = (mean_median_mode2([3, 5, 45, 3, 2, 1, 89]))
print(f"Mean : {a}, Median : {b}, Mode : {c}")

def add(a, b) : 
    if a == 0 and b == 0 : 
        # it will return none for below 
        return
    else:
        return a + b
    
print(add(9, 0))