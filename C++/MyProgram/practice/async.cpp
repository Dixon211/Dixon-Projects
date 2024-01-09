#include <iostream>
//#include "cleanup/cleanup.h"
#include <thread>
#include <mutex>

std::mutex mutex;
bool newDataAvailable = false;
int shareddata;


void myFunction (bool& newDataAvailable, int& shareddata) {
    int i = 0;
    int x = 0;
    while (true) {
        i++;
        //std::cout << "\n " << i << std::endl;
        if (i==42000) {
            x++;
            i = 0;
        }
        if (x!=0 && newDataAvailable == false) {
            {
                std::unique_lock<std::mutex> lock(mutex);
                newDataAvailable = true;
                shareddata = x;
            }
            x = 0;
        }
    }
}


int main () {
   

    //open the thread and detach it to run on its own
    std::thread myThread(myFunction, std::ref(newDataAvailable), std::ref(shareddata));
    myThread.detach();
    std::cout << "\nThread Running and detached..." <<std::endl;
    
    std::cout <<"\nEntering Loop..." <<std::endl;
    while (true){
            
            if (newDataAvailable == true) {
                {
                    std::unique_lock<std::mutex> lock(mutex);
                    newDataAvailable = false;
                }
                std::cout << "\nthe loop made " << shareddata << " passes" << std::endl;
            }
  
    }
 
    
    //Cleanup ();
    return 0;
}