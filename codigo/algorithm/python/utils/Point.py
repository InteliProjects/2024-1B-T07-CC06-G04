class Point:
    """
    Represents a geographical point with latitude and longitude coordinates.

    Attributes:
        index (int): The unique identifier for the point.
        latitude (float): The latitude coordinate of the point.
        longitude (float): The longitude coordinate of the point.
    """

    def __init__(self, index, latitude, longitude):
        """
        Constructs a new Point instance.

        Parameters:
            index (int): The unique identifier for this point.
            latitude (float): The latitude coordinate of the point.
            longitude (float): The longitude coordinate of the point.
        """
        self.index = index
        self.latitude = latitude
        self.longitude = longitude