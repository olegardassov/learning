import math

def max_height():
    try:
        v0, a, g = input(
            "Please input starting speed, angle and acceleration using coma between parameters \nExample: 1.5,2.7,3.5 or 1,2.5,3 for round numbers. \n-->").split(
            ",")
        v0 = float(v0) # check if inputed data is a number
        a = float(a)
        g = float(g)
    except:
        print("Error, Please use numbers only!")
        max_height() # if error, restarts program
    else:
        hmax = ((float(v0)**2) * (math.sin(float(a)) * math.sin(float(a)) / (2 * float(g))))
        L = ((float(v0)**2) * (math.sin(2 * float(a)))) / float(g)
        print('Maximum height is ' + '%.2f' % (L) +'m' + "\nMaximum distance is " + '%.2f' % (hmax) + 'm')

((float(v0)**2) * 2 * math.sin(float(a) * math.cos(float(a)))) / float(g)
max_height()


