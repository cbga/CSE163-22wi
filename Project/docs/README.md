# Instructions

## Requirement
You need the following `Python` libraries:
- `os`
- `nltk`
- `pandas`
- `requests`
- `matplotlib`
- `sklearn`

If you don't have any of those libraries, download them directly in Anaconda or over
```bash
pip install <LIBRARY-NAME>
```
## How to run
1. Download `main.py`, `process_visualize.py`, `use_api_preprocess.py`, `settings.py` to your local directory.
2. [Click here](https://covid19.who.int/WHO-COVID-19-global-data.csv) to download `WHO-COVID-19-global-data.csv`. (be sure to download it every new day before you run the `.py` files and replace the old one if you have run this project before)

3. Create a new folder under the same directory as `output` to store the output images.
4. In `use_api_preprocess.py`, scroll down and you will see some lines like this:
    ```python
    # ----------------------------------------
    # CHANGE start_day
    start_day = '2022-03-08'
    # CHANGE end_day
    end_day = '2022-03-13'
    # ----------------------------------------
    ```
    Change `end_day` into the day before you run this project; Change `start_day` into the **5th day** before the `end_day`. Both should be in the format as the sample above In the sample case, the 5th day before `end_day` (Mar 13, 2022) is Mar 8, 2022.
5. Make sure you are connected to internet while running this project.
6. Open and run **`main.py` file*** under the environment with all required libraries. All images generated will be saved in `/output` subdirectory with proper names.

---

## _Optional: Use your own Twitter API_
You may notice that in `main.py`, there is
```python
os.environ['TOKEN'] = <TOKEN>
```
It's using my own token that can authenticate your use of the Application Programming Interface (API). 
- See answers under this link for general explanation for [API token](https://stackoverflow.com/questions/17784908/what-is-an-api-token).

If you want to use your own Twitter API, follow the [procedure from Twitter Developer Platform](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

Creat a new project and copy the `Bearer Token` (if you forgot, click in your own project, under `Keys and tokens` section, you can regenerate a new Bearer Token.)

Replace `<TOKEN>` with your own token and run the project as described above.
