"""
Ryan Siu
Runs imgd with student output against expected output
and produces images showing the pixel differences.
"""
import subprocess
import os

import hw3
import pandas as pd

PLOTS = [
    "line_plot_bachelors.png",
    "bar_chart_high_school.png",
]
IMGD_ARGS = [
    "--pixel-correct-threshold", "0.99",
    "--diff-mode", "always",
    "--correct-colour", "ffffff",
]
EXPECTED_FUNCTIONS = [
    "compare_bachelors_1980",
    "top_2_2000s",
    "line_plot_bachelors",
    "bar_chart_high_school",
    "plot_hispanic_min_degree",
    "fit_and_predict_degrees"
]


def run_imgd(expected, actual, args=IMGD_ARGS):
    """
    Runs imgd of student output against expected.
    Produces diff image only if both student and expected output exist.
    """
    if not os.path.exists(actual):
        print(f"Could not find the file: {actual} after running hw3.py\n")
    elif not os.path.exists(expected):
        print(f"Could not find the file: {expected}\n")
    else:
        print(f"Running image comparison tool on {actual}...")
        output = subprocess.run(["/opt/ed/bin/imgd", expected, actual]
                                + args, capture_output=True)
        output = output.stdout.decode("utf-8")
        if "Your image's" in output:  # dimensions mismatch
            output += ("Be sure that you call sns.set() and are passing"
                       " in bbox_inches='tight' to your savefig call\n")
        else:
            os.rename("diff.png", f"{os.path.splitext(actual)[0]}_diff.png")
        print(output)
        print()


def main():
    data = pd.read_csv('nces-ed-attainment.csv', na_values=['---'])
    print("Checking for all functions:")
    for f in EXPECTED_FUNCTIONS:
        try:
            getattr(hw3, f)(data)
            print("    Found", f)
        except AttributeError:
            print("    ERROR: Missing", f, "in hw3.py")
    print()
    for plot_name in PLOTS:
        run_imgd(f"expected/{plot_name}", plot_name)


if __name__ == "__main__":
    main()
