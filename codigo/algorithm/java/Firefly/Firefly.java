package java.Firefly;

import java.util.ArrayList;

/**
 * Represents a firefly with its path and total distance traveled.
 */
public class Firefly {
    private ArrayList<Integer> path;
    private double totalDistance;
    double lambda; // Light Intensity of firefly

    /**
     * Constructs a firefly with the given path and total distance traveled.
     *
     * @param path          The path followed by the firefly represented as a list of node indices.
     * @param totalDistance The total distance traveled by the firefly.
     */
    public Firefly(ArrayList<Integer> path, double totalDistance) {
        this.totalDistance = totalDistance;
        this.path = path;
        lambda = 1 / totalDistance;
    }

    /**
     * Gets the total distance traveled by the firefly.
     *
     * @return The total distance traveled.
     */
    public double getDistance() {
        return totalDistance;
    }

    /**
     * Gets the brightness (light intensity) of the firefly.
     *
     * @return The brightness of the firefly.
     */
    public double getBrightness() {
        return lambda;
    }

    /**
     * Sets the path followed by the firefly.
     *
     * @param path The new path to be followed by the firefly, represented as a list of node indices.
     */
    public void setPath(ArrayList<Integer> path) {
        this.path = path;
    }

    /**
     * Gets the path followed by the firefly.
     *
     * @return The path followed by the firefly, represented as a list of node indices.
     */
    public ArrayList<Integer> getPath() {
        return path;
    }
}
