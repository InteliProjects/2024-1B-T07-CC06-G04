package java;

/**
 * Represents a geographical place with latitude and longitude coordinates.
 */
public class Place {
    private double latitude; // Latitude coordinate of the place
    private double longitude; // Longitude coordinate of the place
    private int indice; // Index of the place
    private String codigoRota; // Route code associated with the place
    private String logradouro; // Street name of the place
    private int numero; // Street number of the place

    /**
     * Constructs a Place object with the given latitude, longitude, index, route code, street name, and street number.
     *
     * @param latitude    The latitude coordinate of the place.
     * @param longitude   The longitude coordinate of the place.
     * @param indice      The index of the place.
     * @param codigoRota  The route code associated with the place.
     * @param logradouro  The street name of the place.
     * @param numero      The street number of the place.
     */
    public Place(double latitude, double longitude, int indice, String codigoRota, String logradouro, int numero) {
        this.latitude = latitude;
        this.longitude = longitude;
        this.indice = indice;
        this.codigoRota = codigoRota;
        this.logradouro = logradouro;
        this.numero = numero;
    }

    /**
     * Gets the latitude coordinate of the place.
     *
     * @return The latitude coordinate.
     */
    public double getLatitude() {
        return latitude;
    }

    /**
     * Gets the longitude coordinate of the place.
     *
     * @return The longitude coordinate.
     */
    public double getLongitude() {
        return longitude;
    }
}
