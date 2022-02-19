"""
Ryan Siu
Runs imgd with student output against expected output
and produces images showing the pixel differences.
"""
from PIL import ImageDraw, Image, ImageFont
import subprocess
import os

import hw5

PLOTS = [
    "map.png",
    "population_map.png",
    "county_population_map.png",
    "county_food_access.png",
    "low_access.png"
]
IMGD_ARGS = [
    "--pixel-correct-threshold", "0.985",
    "--diff-mode", "always",
    "--correct-colour", "ffffff",
]


def no_diffs():
    """
    Replaces a blank generated diff image with one that has
    "No Differences Found" written on it
    """
    msg = "No Differences Found"
    ttf = "LiberationSans-Bold.ttf"

    image = Image.open("diff.png")
    width, height = image.size

    fontsize = 1
    font = ImageFont.truetype(ttf, fontsize)
    fraction = 0.5

    while font.getsize(msg)[0] < fraction * width:
        # iterate until the text size is just larger
        #    than the criteria
        fontsize += 1
        font = ImageFont.truetype(ttf, fontsize)

    ImageDraw.Draw(image).text((width / 4, height / 2),
                               msg, font=font, fill=(0, 0, 0))
    image.save("diff.png")


def run_imgd(expected, actual, args=IMGD_ARGS):
    """
    Runs imgd of student output against expected.
    Produces diff image only if both student and expected output exist.
    """
    if not os.path.exists(actual):
        print(f"Could not find: {actual}. Be sure you're calling all plot"
              " functions in main\n")
    elif not os.path.exists(expected):
        print(f"Could not find: {expected}\n")
    else:
        print(f"Running image comparison tool on {actual}...")
        output = subprocess.run(["/opt/ed/bin/imgd", expected, actual]
                                + args, capture_output=True)
        output = output.stdout.decode("utf-8")
        if "100.00%" in output:  # full match
            no_diffs()
        if "Your image's" not in output:  # !dimensions mismatch
            os.rename("diff.png", f"{os.path.splitext(actual)[0]}_diff.png")
        print(output)
    print()


def main():
    print("Running all functions in your main method."
          " This may take a minute or so:")
    hw5.main()
    print()
    for plot_name in PLOTS:
        run_imgd(f"expected/{plot_name}", plot_name)


if __name__ == "__main__":
    main()
