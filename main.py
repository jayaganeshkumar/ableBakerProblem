from dataProcessing import *                  

def main():
    
    #Input data ->Mahdi
    customerInterArrivalTime = [1,2,3,4]  
    ableServiceTime = [2,3,4,5] 
    bakerServiceTime = [4,5,6,7] 
    ableBakerPriority = 0 #If 0 => Able is first if 1 => baker is first if 2 => randomly chosen
    
    selectCustomerOrTime = True #If true customer number is given if false time period is given
    
    customerCount = 100  
    timeLength = 0 
    
    
    
    # Data processing  -> MrHs
    if(selectCustomerOrTime):
        count = customerCount
    else:
        count = timeLength
    lili = customerGenerator(customerInterArrivalTime, ableServiceTime, bakerServiceTime, ableBakerPriority, selectCustomerOrTime, count)
    
    
    # printing output using django -> Mahdi
    def test(lili):
        for i in range(len(lili)):
            k = lili[i]
            print str(i)+" | "+str(k.interArrivalTime)+" | "+str(k.arrivalTime)+" | "+str(k.whenAbleAvailable)+" | "+str(k.whenBakerAvailable)+" | "+str(k.serverChosen)+" | "+str(k.serviceTime)+" | "+str(k.timeServiceBegins)+" | "+str(k.ableServiceCompletedTime)+" | "+str(k.bakerServiceCompletedTime)+" | "+str(k.callerDelay)+" | "+str(k.timeInsystem)+" | ";
    
    return 0

main()