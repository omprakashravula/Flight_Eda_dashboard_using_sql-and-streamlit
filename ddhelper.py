import mysql.connector
class DB:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="omprakash1212",
                database="flight"
            )
            self.mycursor= self.conn.cursor()
            print('database connected')
        except:
            print('connection error')
    def fetch_city_names(self):
        city=[]
        self.mycursor.execute("""SELECT distinct(Destination) FROM flight.flights
        union
        SELECT distinct(source) FROM flight.flights;""")
        data=self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
        return city
    def fetch_all_flights(self,source,destination):
        self.mycursor.execute("""SELECT * FROM flight.flights;
                where source='{}' and destination='{}'
                """.format(source,destination))
        data=self.mycursor.fetchall()
        #print(data)
        return data
#print('hello')
    def fetch_airline_frequency(self):
        airline=[]
        frequency=[]
        self.mycursor.execute("""SELECT Airline,count(*) FROM flight.flights
        group by Airline""")
        data=self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
        return airline,frequency
    def fetch_airline_avg_price(self):
        airline=[]
        avg_price=[]
        self.mycursor.execute("""SELECT Airline,AVG(price) as avg_price from flight.flights 
        group by Airline""")
        data=self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            avg_price.append(item[1])
        return airline,avg_price
    def busy_airport(self):
        city=[]
        frequency=[]
        self.mycursor.execute("""select Source,count(*)from (SELECT Source FROM flight.flights
                                    union all
                                    SELECT Destination FROM flight.flights) t
                                    group by t.Source""")
        data=self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])
        return city,frequency
    def daily_frequency(self):
        date=[]
        frequency=[]
        self.mycursor.execute("""select Date_of_Journey,count(*) from flight.flights
                             group by Date_of_Journey""")
        data=self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
            frequency.append(item[1])
        return date,frequency

