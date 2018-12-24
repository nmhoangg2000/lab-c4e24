from ex11 import is_inside
k = is_inside([100, 120], [140, 60, 100, 200])
if k == False:
    print("Your function is correct")
else:
    print("Oops, there's a bug")