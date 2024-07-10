package java;

import java.Firefly.Solver;

import java.io.FileReader;
import java.util.Scanner;
import java.util.Arrays;
import java.util.List;
import java.util.HashMap;
import java.util.Map;

/**
 * Represents the main class for solving the Traveling Salesman Problem using the Firefly Algorithm.
 */
public class Main {
    private final String filepath; // The filepath of the CSV data file
    private double[][] matrix; // Distance matrix calculated from the CSV data

    /**
     * Constructs a Main object with the given filepath of the CSV data file.
     *
     * @param filepath The filepath of the CSV data file.
     */
    public Main(String filepath) {
        this.filepath = filepath;
    }

    /**
     * Reads the CSV data file, calculates the distance matrix, and solves the TSP using the Firefly Algorithm.
     */
    public void reader() {
        Map<Integer, List<String>> points = new HashMap<Integer, List<String>>();
        try {
            int i = 0;
            Scanner scanner = new Scanner(new FileReader(filepath));
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                List<String> lines = Arrays.asList(line.split(";"));
                if (lines.get(3).equals("72_203")) {
                    points.put(i, lines);
                    i++;
                }
            }
            scanner.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

        int n = points.size();
        this.matrix = new double[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) matrix[i][j] = 0;

                double lat1 = Double.parseDouble(points.get(i).get(1));
                double lat2 = Double.parseDouble(points.get(j).get(1));
                double long1 = Double.parseDouble(points.get(i).get(2));
                double long2 = Double.parseDouble(points.get(j).get(2));
                matrix[i][j] = haversine(lat1, long1, lat2, long2);
                matrix[j][i] = haversine(lat1, long1, lat2, long2);
            }
        }
        Solver solver = new Solver(n, 10, matrix);
        solver.solver();
    }

    /**
     * Calculates the Haversine distance between two points specified by their latitude and longitude.
     *
     * @param lat1 Latitude of the first point.
     * @param lon1 Longitude of the first point.
     * @param lat2 Latitude of the second point.
     * @param lon2 Longitude of the second point.
     * @return The Haversine distance between the two points.
     */
    private double haversine(double lat1, double lon1, double lat2, double lon2) {
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
     * Main method to run the TSP solver.
     *
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        Main main = new Main("../data_source/amostra_menor.csv");
        main.reader();
    }
}
