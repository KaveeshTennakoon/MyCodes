#include <iostream>
#include <iomanip>
#include <limits>
#include <vector>
#include <algorithm>

using namespace std;

// Function to convert Celsius to Fahrenheit
double celsiusToFahrenheit(double celsius) {
    return (celsius * 1.8) + 32;
}

int main() {
    const int NUM_READINGS = 12;
    const double MIN_CELSIUS = 35.0;
    const double MAX_CELSIUS = 42.0;
    const double MIN_FAHRENHEIT = 95.0;
    const double MAX_FAHRENHEIT = 108.0;

    vector<double> temperatures(NUM_READINGS);
    double sum = 0.0;
    double minTemp = MAX_CELSIUS;
    double maxTemp = MIN_CELSIUS;

    for (int i = 0; i < NUM_READINGS; i++) {
        double celsius;
        int hour = i * 2;
        cout << "Enter temperature at " << hour << " hours (in Celsius): ";
        cin >> celsius;

        // Input validation
        if (celsius < MIN_CELSIUS || celsius > MAX_CELSIUS) {
            cout << "Invalid temperature! Please enter a value between " << MIN_CELSIUS << " and " << MAX_CELSIUS << " Celsius." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            i--;
            continue;
        }

        double fahrenheit = celsiusToFahrenheit(celsius);
        temperatures[i] = fahrenheit;
        sum += fahrenheit;
        minTemp = min(minTemp, celsius);
        maxTemp = max(maxTemp, celsius);
    }

    double avgTemp = sum / NUM_READINGS;

    // Print temperature summary
    cout << "\nTemperature Summary for a day" << endl;
    cout << "-----------------------------" << endl;
    cout << "Average Temperature: " << fixed << setprecision(2) << avgTemp << "F" << endl;
    cout << "Maximum Temperature: " << fixed << setprecision(2) << celsiusToFahrenheit(maxTemp) << "F" << endl;
    cout << "Minimum Temperature: " << fixed << setprecision(2) << celsiusToFahrenheit(minTemp) << "F" << endl;
    cout << "-----------------------------" << endl;

    // Create bar chart
    cout << "\n----------------------------------" << endl;
    cout << "BAR CHART (Temperature Summary)" << endl;
    cout << "----------------------------------" << endl;
    cout << "Time (h) Temperature(95-108) F" << endl;
    cout << "----------------------------------" << endl;

    for (int i = 0; i < NUM_READINGS; i++) {
        int hour = i * 2;
        cout << setw(2) << hour << " |";
        int bars = static_cast<int>((temperatures[i] - MIN_FAHRENHEIT) / (MAX_FAHRENHEIT - MIN_FAHRENHEIT) * 14);
        for (int j = 0; j < bars; j++) {
            cout << "X";
        }
        cout << endl;
    }

    cout << "----------------------------------" << endl;

    return 0;
}