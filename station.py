class station:
    def __init__(self,station_name,kms,price,stat_num) -> None:
        self.station_name=station_name
        self.kms=kms
        self.price=price
        self.stat_num=stat_num

    def print_station(self):
        print("The price from majestic to "+self.station_name+" is "+str(self.price))
        print("The distance from majestic to "+self.station_name+" is "+str(self.kms))
        print("The station number is "+str(self.stat_num))
        

