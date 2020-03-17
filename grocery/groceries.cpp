#include<iostream>
using std::cout; using std::cin; using std::endl;
#include<string>
using std::string;
#include<sstream>
using std::istringstream;
#include<vector>
using std::vector;
#include<numeric>
#include<iomanip>

void all(vector<char> letters_vec, vector<double> &m,vector<double> &n, vector<double> &e, double cost) {
    m.push_back(cost/3);
    n.push_back(cost/3);
    e.push_back(cost/3);
}

void two(vector<char> letters_vec, vector<double> &m,vector<double> &n, vector<double> &e, double cost) {

    for (auto element : letters_vec) {
        if (element == 'm') {
            m.push_back(cost/2);
        } else if (element == 'n') {
            n.push_back(cost/2);
        } else if (element == 'e') {
            e.push_back(cost/2);
        }
    }
}

void one(vector<char> letters_vec, vector<double> &m,vector<double> &n, vector<double> &e, double cost) {

    for (auto element : letters_vec) {
        if (element == 'm') {
            m.push_back(cost);
        } else if (element == 'n') {
            n.push_back(cost);
        } else if (element == 'e') {
            e.push_back(cost);
        }
    }
}

void split(string to_split,vector<double> &m,vector<double> &n, vector<double> &e, double cost) {
    vector<char> letters_vec;
    string test;
    istringstream iss(to_split);
    for (auto element : to_split) {
        letters_vec.push_back(element);
    }
    if (letters_vec.size() == 2) {
        two(letters_vec,m,n,e,cost);
    } else if (letters_vec.size() == 3) {
        all(letters_vec,m,n,e,cost);
    } else if (letters_vec.size() == 1) {
        for (auto element : letters_vec) {
            if (element == 'a') {
                all(letters_vec,m,n,e,cost);
            } else {
                one(letters_vec,m,n,e,cost);
            }
        }  
    }

}


int main() {
    vector<double> m;
    vector<double> n;
    vector<double> e;
    string dummy_string = " ";
    double m_total = 0.0;
    double n_total = 0.0;
    double e_total = 0.0;
    double tax = 0.0;
    string to_split;

    while (true) {
        double cost = 0.0;
        string to_split;
        cout << "cost: ";
        cin >> cost;
        if (cost == 0) {
            break;
        }
        cout << "how to split?: ";
        cin >> to_split;
        split(to_split, m, n, e, cost);
    }
    m_total = std::accumulate(m.begin(), m.end(), 0.0);
    n_total = std::accumulate(n.begin(), n.end(), 0.0);
    e_total = std::accumulate(e.begin(), e.end(), 0.0);
    cout << "tax: ";
    cin >> tax;
    m_total += tax/3;
    n_total += tax/3;
    e_total += tax/3;
    cout << std::fixed << std::setprecision(2);
    cout << "all values are after tax" << endl;
    cout << "moeez's total: " << m_total << endl;
    cout << "noah's total: " << n_total << endl;
    cout << "eric's total: " << e_total << endl;
    cout << "grand total: " << e_total + n_total + m_total << endl;

}