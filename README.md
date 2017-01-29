Lonpos solving using Python
===========================

This project is a reimplementation of the Lonpos solving script
written a couple years back in the language [PHP](https://github.com/wimulkeman/PHP_Lonpos_solver).

It uses a more bare bone usage of bit comparing.

The PHP script was able to calculate the 21.200 solutions
for the 9x9 board in around 45 minutes. The goal is to
decrease the calculation time with this project in Python.

Possible ways to achieve that are:
- The usage of a better bit comparing than used within
the PHP project.
- A faster return when a examined solution is incorrect.
- Possible introducing to multithreading.