package java;

/**
 * Represents a route between two places.
 */
public class Route {
    private Place placeOrigin; // The origin place of the route
    private Place placeDestiny; // The destination place of the route

    /**
     * Constructs a Route object with the given origin and destination places.
     *
     * @param placeOrigin  The origin place of the route.
     * @param placeDestiny The destination place of the route.
     */
    public Route(Place placeOrigin, Place placeDestiny) {
        this.placeOrigin = placeOrigin;
        this.placeDestiny = placeDestiny;
    }

    /**
     * Gets the origin place of the route.
     *
     * @return The origin place.
     */
    private Place getOrigin() {
        return placeOrigin;
    }

    /**
     * Gets the destination place of the route.
     *
     * @return The destination place.
     */
    private Place getDestiny() {
        return placeDestiny;
    }

    /**
     * Calculates the distance between the origin and destination places using the Haversine formula.
     *
     * @return The distance between the origin and destination places in kilometers.
     */
    private double harvesine() {
        // Data
        double lat1 = placeOrigin.getLatitude();
        double lat2 = placeDestiny.getLatitude();
        double lon1 = placeOrigin.getLongitude();
        double lon2 = placeDestiny.getLongitude();
        double R = 6371.0; // Earth radius in kilometers

        double latDistance = toRad(lat2 - lat1);
        double lonDistance = toRad(lon2 - lon1);
        double a = Math.sin(latDistance / 2) * Math.sin(latDistance / 2) +
                   Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) *
                   Math.sin(lonDistance / 2) * Math.sin(lonDistance / 2);
        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        double haversine = R * c;

        return haversine;
    }

    /**
     * Converts degrees to radians.
     *
     * @param value The value in degrees.
     * @return The value converted to radians.
     */
    private static Double toRad(Double value) {
        return value * Math.PI / 180;
    }

    /**
     * Main method to test the Route class.
     *
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        // Create two place objects
        Place point1 = new Place(-22.811205, -43.320963, 0, null, null, 0);
        Place point2 = new Place(-22.810982, -43.321017, 0, null, null, 0);

        // Create a route object
        Route route = new Route(point1, point2);

        // Calculate and print the distance between the places
        System.out.println(route.harvesine());
    }
}
