# Task_03_Descriptive_Stats

This repository contains my submission for Research Task 03 under the Syracuse University OPT research program. The objective was to perform descriptive statistical analysis on three datasets related to the 2024 U.S. presidential election, using three different Python strategies:

- Pure Python (no third-party libraries)
- Pandas
- Polars

Throughout this task, I implemented descriptive statistical analysis using Pure Python, Pandas, and Polars. While all three approaches produced consistent numerical results, minor challenges emerged in formatting and presentation.
All 3 strategies achieved identical results, but the process was a bit challenging, including output formatting, float rounding. Polar displayed many decimal places, pandas used scientific notations. As well as for null values count, each process handled detection and display in different way.
As main challenge was to produce identical results, Pure python, Polars, pandas gave identical numerical results. So, just to overcome the display output problem, I did adjust the decimal places, use scientific notation only whenever necessary. Handled null values manually for numerical cols. 
I find Pandas more easier and more performant because of the intuitive format and built in suggestion function like .describe(), .value_count().
ChatGPT provided a solid starting point for polars strategy as I have not used it since a long time, but using chatgpt sped up the development process.
ChatGPT and Claude are using Pandas when asked for descriptive statistics. Furhther, I agree with these recommendations as I have done most opf my academics and project work on Pandas in Python.
