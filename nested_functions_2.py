#def disp():
   # def show():
    #    print("Show Function")
   # print("Disp Function")
   # show()

#disp()

#nested function with return statement
def disp(xz):
    def show():
        return "Show Function"
    result = show() +" " + xz + " Disp Function"
    return result

print(disp("GeekyShows"))