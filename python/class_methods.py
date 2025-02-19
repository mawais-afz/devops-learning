class DateConverter:
    @classmethod
    def from_string(cls, date_string):
        # Convert date string in format "YYYY-MM-DD" to a tuple
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def from_timestamp(cls, timestamp):
        # Convert Unix timestamp to date components
        import datetime
        date = datetime.datetime.fromtimestamp(timestamp)
        return cls(date.year, date.month, date.day)
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month 
        self.day = day
        
    def to_string(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

def main():
    # Create date using constructor
    date1 = DateConverter(2024, 1, 15)
    print("Date 1:", date1.to_string())
    
    # Create date using class method from string
    date2 = DateConverter.from_string("2024-02-20")
    print("Date 2:", date2.to_string())
    
    # Create date using class method from timestamp
    import time
    current_timestamp = time.time()
    date3 = DateConverter.from_timestamp(current_timestamp)
    print("Date 3:", date3.to_string())

if __name__ == "__main__":
    main()
