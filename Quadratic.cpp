/*
  This program solves the quadratic equation in the form "ax^2 + bx + c = 0" 
  and draws a graph to it
*/

#include <matplotlibcpp.h>
#include <vector>
#include <cmath>
#include <iostream>

namespace plt = matplotlibcpp;

int main() {
    double a, b, c;
    std::cout << "Enter coefficients a, b and c: ";
    std::cin >> a >> b >> c;

    // Calculate the quadratic function values
    std::vector<double> x_values, y_values;
    for (double x = -5; x <= 5; x += 0.1) {
        double y = a * x * x + b * x + c;
        x_values.push_back(x);
        y_values.push_back(y);
    }

    // Calculate specific points to mark
    std::vector<double> mark_x_values = {-4, -2, 0, 2, 4};
    std::vector<double> mark_y_values;
    for (double x : mark_x_values) {
        mark_y_values.push_back(a * x * x + b * x + c);
    }

    // Plot the quadratic function curve
    plt::plot(x_values, y_values, "b");

    // Plot the points
    plt::scatter(mark_x_values, mark_y_values, 100, {{"color", "orange"}});

    // Set the grid and labels
    plt::grid(true);
    plt::xlabel("x");
    plt::ylabel("y");

    // Show the plot
    plt::show();

    return 0;
}
