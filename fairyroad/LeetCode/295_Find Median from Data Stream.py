class MedianFinder(object):

    def __init__(self):
        self.arr = []
        self.result = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.arr.append(num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        self.arr.sort()
        tmp = len(self.arr)/2.0
        if tmp != int(tmp):
            tmp = int(tmp)
            return self.arr[tmp]
        else:
            tmp = int(tmp)
            return (self.arr[tmp - 1] + self.arr[tmp])/2.0
