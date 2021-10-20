![Project Logo][project_logo]

---

<h4 align="center">Scraping & Analyzing Japanese whisky from <a href="https://www.thewhiskyexchange.com/c/35/japanese-whisky" target="_blank">The Whisky Exchange</a> website with <a href="https://www.beerwulf.com/en-gb/c/all-beers" target="_blank">Python</a> and <a href="https://en.wikipedia.org/wiki/Microsoft_Power_BI" target="_blank">Power BI</a></h4>

<p align='center'>
<img src='06_RESOURCES/built-with-love.svg'>
<img src='06_RESOURCES/powered-by-coffee.svg'>
<img src='06_RESOURCES/cc-nc-sa.svg'>
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#demo">Demo</a> •
  <a href="#support">Support</a> •
  <a href="#license">License</a>
</p>

## Overview

This project focuses on scraping games and their associated metrics from [The Whisky Exchange - Japanese Whisky](https://www.thewhiskyexchange.com/c/35/japanese-whisky), performing exploratory data analysis to generate insights and visualize them with the help of Power BI.

The repository directory structure is as follows:

├───Analyzing-Pokemons<br>
│ ├───01_WEBSCRAPING<br>
│ ├───02_ETL<br>
│ └───06_RESOURCES<br>

The type of content present in the directories is as follows:

**01_WEBSCRAPING**

This directory contains the python script to scrape data from the website along with flat file that has the scraped data.

**02_ETL**

This directory contains the ETL script that takes the scraped dataset as input, transforms it and exports an analysis-ready dataset into the _03_DATA_ directory.

**03_DATA**

This directory contains the data that can be directly used for exploratory data analysis and data visualization purposes.

**04_ANALYSIS**

This directory contains the python notebooks that analyzes the clean dataset to generate insights

**05_DASHBOARD**

This directory contains the python notebook with an embedded Power BI report that visualizes the data. The Power BI dashboard contains slicers, cross-filtering and other advance capabilities that end user can play with to visualize a specific facet of the data or, to get additional insights.

**06_RESOURCES**

This directory contains images, icons, layouts, etc. that are used in this project

## Prerequisites

The major skills that are required as prerequisite to fully understand this project are as follows:

- Basics of Python
- Python libraries: Requests-HTML, Pandas, DateTime, Time, Asycio
- Basics of Python Notebooks
- Basics of Power BI

In order to complete the project, I've used the following applications and libraries

- Python
- Python libraries mentioned in requirements.txt file
- Jupyter Notebook
- Visual Studio Code
- Microsoft Power BI

> The choice of applications & their installation might vary based on individual preferences & system settings.

## Demo

It will contain the architecture and gif of code execution and report with explanation.

## Support

If you have any doubts, queries or, suggestions then, please connect with me in any of the following platforms:

[![Linkedin Badge][linkedinbadge]][linkedin] [![Twitter Badge](https://img.shields.io/badge/-@quantumudit-1ca0f1?style=flat&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/quantumudit)][twitter] [![Skype Badge](https://img.shields.io/badge/-quantumudit-00AFF0?style=flat&labelColor=00AFF0b&logo=skype&logoColor=white)][skype] [![YouTube Badge](https://img.shields.io/badge/-quantumdata-e74c3c?style=flat&labelColor=e74c3c&logo=youtube&logoColor=white)][youtube] [![Mail Badge](https://img.shields.io/badge/-quantumudit@gmail.com-c0392b?style=flat&labelColor=c0392b&logo=gmail&logoColor=white)][gmail]

If you like my work then, you may support me at Patreon:

<a href="https://www.patreon.com/quantumudit" target="_blank">
<img src="06_RESOURCES/become_a_patreon.png" alt="git" width="170" height="50"/>
</a>

## License

<a href = 'https://creativecommons.org/licenses/by-nc-sa/4.0/' target="_blank">
    <img src='06_RESOURCES/by-nc-sa.png' width=88 height=31>
</a>

This license allows reusers to distribute, remix, adapt, and build upon the material in any medium or format for noncommercial purposes only, and only so long as attribution is given to the creator. If you remix, adapt, or build upon the material, you must license the modified material under identical terms.

<!-- Image Links -->

[project_logo]: 06_RESOURCES/japanese_whisky_analysis_logo.png
[build_with]: 06_RESOURCES/built-with-love.svg
[powered_by]: 06_RESOURCES/powered-by-coffee.svg
[license_logo]: 06_RESOURCES/by-nc-sa.png

<!-- External Links -->

[by_nc_sa_license]: https://creativecommons.org/licenses/by-nc-sa/4.0/
[about_python]: https://en.wikipedia.org/wiki/Python_(programming_language)
[about_power_bi]: https://en.wikipedia.org/wiki/Microsoft_Power_BI
[patreon_link]: 06_RESOURCES/become_a_patreon.png

<!-- Profile Links -->

[linkedin]: https://www.linkedin.com/in/uditkumarchatterjee/
[twitter]: https://twitter.com/quantumudit
[data.world]: https://data.world/dataman-udit
[youtube]: https://www.youtube.com/channel/UCKS7gum4_d3zFOFgdL2uLdA
[gmail]: mailto:quantumudit@gmail.com
[skype]: skype:quantumudit?call

<!-- Shields Profile Links -->

[linkedinbadge]: https://img.shields.io/badge/-uditkumarchatterjee-0e76a8?style=flat&labelColor=0e76a8&logo=linkedin&logoColor=white
[twitterbadge]: https://img.shields.io/badge/-@quantumudit-1ca0f1?style=flat&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/quantumudit
[skypebadge]: https://img.shields.io/badge/-quantumudit-00AFF0?style=flat&labelColor=00AFF0b&logo=skype&logoColor=white
[gmailbadge]: https://img.shields.io/badge/-quantumudit-c0392b?style=flat&labelColor=c0392b&logo=gmail&logoColor=white
[youtubebadge]: https://img.shields.io/badge/-quantumdata-e74c3c?style=flat&labelColor=e74c3c&logo=youtube&logoColor=white
