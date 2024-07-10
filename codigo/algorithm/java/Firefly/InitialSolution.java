package java.Firefly;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Random;

/**
 * Represents a class to find the initial solution for the TSP using a heuristic.
 */
public class InitialSolution {
    private int n; // Number of cities
    private double[][] distanceMatrix; // Distance matrix between cities
    private double totalDistance = 0; // Total distance of the initial solution
    private ArrayList<Integer> path; // Initial path found

    /**
     * Constructs an InitialSolution object with the given number of cities and distance matrix.
     *
     * @param n             The number of cities in the TSP.
     * @param distanceMatrix The distance matrix representing distances between cities.
     */
    public InitialSolution(int n, double[][] distanceMatrix) {
        this.n = n;
        this.distanceMatrix = distanceMatrix;
    }

    /**
     * Finds the initial solution using a heuristic approach.
     * It initializes the path by randomly selecting the first city and then greedily adding the nearest cities.
     */
    public void findInitial() {
        Random random = new Random();
        int first = random.nextInt(n);

        path = new ArrayList<Integer>();
        path.add(first);
        ArrayList<Integer> locals = new ArrayList<Integer>(n);

        for (int i = 0; i < n; i++) {
            locals.add(i);
        }

        for (int i = 0; i < n - 1; i++) {
            Iterator<Integer> x = locals.iterator();
            int best = x.next();
            if (!path.contains(best)) {
                for (int j = 0; j < n; j++) {
                    if (!path.contains(j)) {
                        if (distanceMatrix[first][best] > distanceMatrix[first][j]) best = j;
                    }
                }
                totalDistance += distanceMatrix[first][best];
                path.add(best);
                first = best;
            }
        }
    }

    /**
     * Gets the total distance of the initial solution.
     *
     * @return The total distance of the initial solution.
     */
    public double getDistance() {
        return totalDistance;
    }

    /**
     * Gets the path of the initial solution.
     *
     * @return The path of the initial solution, represented as a list of city indices.
     */
    public ArrayList<Integer> getPath() {
        return path;
    }
}
