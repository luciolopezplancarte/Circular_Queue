"""
Lucio Plancarte
"""
from Queue import Queue

class Advertisement():
    
    def __init__(self, slogan):
        """
        Constructor for the Advertisment class.
        This creates an object with a slogan.
        PARAMETERS:
        ------------
        String : slogan. The slogan for the Advertisement object
        """
        self._slogan = slogan

    
    def get_slogan(self):
        """
        Method returns the slogan for an advertisement
        """
        return self._slogan




class AdRotator(Queue):
    """
    Stores Advertisements and simulates their display
    """

    def __init__(self, list_capacity):
        """
        Constructor for the AdRotator class.
        PARAMETERS:
        -----------
        - list_capacity (int): The maximum capacity of the list
        """
        super().__init__(list_capacity)


    def add_ad(self, slogan):
        """
        Add an Advertisement object to the queue of ads.
        It creates a NEW OBJECT for an advertisement using the 
        given slogan.
        PARAMETERS:
        ------------
        - slogan (str): The slogan of the advertisement to be added to the list
        """
        new_ad = Advertisement(slogan)
        self.enqueue(new_ad)
        print(f"Added '{new_ad.get_slogan()}' to the ad manager.")



    def rotate(self, num_ads):
        """
        Simulate rotating a specified number of ads from the queue.
        It first shows. "Rotating ## ads:"
        Then, it shows "Now displaying: ___ slogan ___"
        
        The ads are NOT removed from the queue.
        
        PARAMETERS:
        ------------
        num_ads (int): The number of ads to rotate
        """
        front_ind = self.get_front()
        front_ad = self.array[front_ind]
        print(f"Rotating {num_ads} ads:")
        for i in range(num_ads):
            print(f"Now displaying: {front_ad.get_slogan()}")
            front_ind = self.compute_front()
            front_ad = self.array[front_ind]
            self.set_front(front_ind)


    def display_list(self):
        """Display the CURRENT order of slogans in the queue"""
        data = self.array[:len(self)]
        for ad in data:
            print(ad.get_slogan())




