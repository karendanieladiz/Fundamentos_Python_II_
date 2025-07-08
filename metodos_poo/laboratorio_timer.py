def format_time(h,m,s):
    return f'{h:02}:{m:02}:{s:02}'


class Timer:

    def __init__(self, hours=0, minutes=0,seconds=0):

        self.__hours = hours
        self.__minutes= minutes
        self.__seconds = seconds

    def __str__(self):
        return format_time(self.__hours,self.__minutes, self.__seconds)
    
    def next_second(self):
        self.__seconds +=1
        if self.__seconds== 60:
            self.__seconds= 0
            self.__minutes += 1 
            if self.__minutes== 60:
                self.__minutes= 0
                self.__hours += 1
                if self.__hours== 24:
                    self.__hours= 0
                   
   
    def previous_second(self):
        self.__seconds -=1
        
     

cronometro = Timer(3,58,58)
print(cronometro)
cronometro.next_second()
print(cronometro)
cronometro.next_second()
print(cronometro)
cronometro.next_second()
print(cronometro)
# cronometro.previous_second()
# print(cronometro)




    


        
