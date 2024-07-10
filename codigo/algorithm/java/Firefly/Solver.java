package java.Firefly;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;
import java.util.Random;

/**
 * Represents a solver for the Traveling Salesman Problem (TSP) using the Firefly Algorithm.
 */
public class Solver {
    private final int n; // Number of nodes
    private final int f; // Number of fireflies
    private final double[][] distanceMatrix; // Distance matrix between nodes
    private final double gamma = 1.0; // Scaling parameter for attractiveness calculation
    private final int iter = 5; // Number of iterations
    private final int m = 5; // Number of updated fireflies

    /**
     * Constructs a Solver object with the given number of nodes, number of fireflies, and distance matrix.
     *
     * @param n             The number of nodes in the TSP.
     * @param f             The number of fireflies used in the algorithm.
     * @param distanceMatrix The distance matrix representing distances between nodes.
     */
    public Solver(int n, int f, double[][] distanceMatrix) {
        this.f = f;
        this.n = n;
        this.distanceMatrix = distanceMatrix;
    }

    /**
     * Solves the TSP using the Firefly Algorithm.
     */
    public void solver() {
        List<Firefly> temp = new ArrayList<Firefly>();
        Firefly[] x = new Firefly[f];
        for (int i = 0; i < f; i++) {
            InitialSolution solution = new InitialSolution(n, distanceMatrix);
            x[i] = new Firefly(solution.getPath(), solution.getDistance());
        }

        for (int i = 0; i < iter; i++) {
            for (int j = 0; j < f; j++) {
                Firefly f = getMostAttractive(x[i], x);
                if (f != null) {
                    for (int k = 0; k < m; k++) {
                        Firefly fnew = moveFirefly(x[i], f);
                        temp.add(fnew);
                    }
                } else {
                    for (int k = 0; k < m; k++) {
                        Firefly fnew = moveRandom(x[i]);
                        temp.add(fnew);
                    }
                }
            }
            x = getBrightestFireflies(temp);
            temp.clear();
        }
        double minDist = Double.MAX_VALUE;
        for (Firefly f : x) {
            if (f.getDistance() < minDist) {
                minDist = f.getDistance();
            }
        }
        System.out.println(minDist);
    }

    private Firefly getMostAttractive(Firefly f, Firefly[] x) {
        double mostAttractiveValue = 0;
        Firefly mostAttractive = null;
        for (Firefly i : x) {
            double newAttractive = calculateAttractive(f, i);
            if (newAttractive > mostAttractiveValue) {
                mostAttractiveValue = newAttractive;
                mostAttractive = i;
            }
        }
        return mostAttractive;
    }

    private double calculateAttractive(Firefly f1, Firefly f2) {
        double beta0 = Math.max(f1.lambda, f2.lambda);
        double A = hammingDistance(f1, f2);
        double r = (A / n) * 10;
        double attractive = beta0 * Math.exp(-gamma * Math.pow(r, 2));

        return attractive;
    }

    private Firefly moveFirefly(Firefly f1, Firefly f2) {
        // Copy the path of f1 to a new list to work with
        ArrayList<Integer> newPath = new ArrayList<>(f1.getPath());

        double hammingDistance = hammingDistance(f1, f2);

        // Find a random index where paths differ
        int randomIndex = -1;
        for (int i = 0; i < hammingDistance; i++) {
            int index = (int) (Math.random() * f1.getPath().size());
            if (!f1.getPath().get(index).equals(f2.getPath().get(index))) {
                randomIndex = index;
                break;
            }
        }

        // If a random index is found, perform a swap
        if (randomIndex != -1) {
            int valueToCopy = f2.getPath().get(randomIndex);
            int indexToMove = newPath.indexOf(valueToCopy);
            // Swap the elements
            int temp = newPath.get(randomIndex);
            newPath.set(randomIndex, newPath.get(indexToMove));
            newPath.set(indexToMove, temp);
        }

        // Create and return the new Firefly with the updated path
        return new Firefly(newPath, calculateDistance(newPath));
    }

    private Firefly moveRandom(Firefly f) {
        ArrayList<Integer> newPath = new ArrayList<>(f.getPath());

        Random random = new Random();
        int index1 = random.nextInt(newPath.size());
        int index2 = random.nextInt(newPath.size());

        int temp = newPath.get(index1);
        newPath.set(index1, newPath.get(index2));
        newPath.set(index2, temp);

        return new Firefly(newPath, calculateDistance(newPath));
    }

    /**
     * Calculates the Hamming distance between two fireflies.
     *
     * @param f1 The first firefly.
     * @param f2 The second firefly.
     * @return The Hamming distance between the two fireflies.
     */
    public double hammingDistance(Firefly f1, Firefly f2) {
        double distance = 0;
        for (int i = 0; i < f1.getPath().size(); i++) {
            if (!f1.getPath().get(i).equals(f2.getPath().get(i))) distance++;
        }
        return distance;
    }

    /**
     * Calculates the total distance of a given path in the TSP.
     *
     * @param path The path to calculate the distance for.
     * @return The total distance of the path.
     */
    public double calculateDistance(ArrayList<Integer> path) {
        double distance = 0;
        for (int i = 1; i < path.size(); i++) {
            distance += distanceMatrix[path.get(i - 1)][path.get(i)];
        }

        distance += distanceMatrix[path.get(path.size() - 1)][path.get(0)];

        return distance;
    }

    private Firefly[] getBrightestFireflies(List<Firefly> temp) {
        sortFirefliesByBrightness(temp);
        Firefly[] brightestFireflies = new Firefly[f];
        for (int i = 0; i < f; i++) {
            brightestFireflies[i] = temp.get(i);
        }
        return brightestFireflies;
    }

    /**
     * Sorts the list of fireflies by their brightness (light intensity).
     *
     * @param fireflies The list of fireflies to be sorted.
     */
    public void sortFirefliesByBrightness(List<Firefly> fireflies) {
        Collections.sort(fireflies, new Comparator<Firefly>() {
            @Override
            public int compare(Firefly f1, Firefly f2) {
                return Double.compare(f2.getBrightness(), f1.getBrightness());
            }
        });
    }
}
