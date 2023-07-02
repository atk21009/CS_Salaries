# Tkinter CS Salaries

The data set I used comes from [Kaggle](https://www.kaggle.com/). The data set I used is called [Data Science Salaries 2023](https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023) written by [randomarnab](https://www.kaggle.com/arnabchaki). In this data set there are 11 different columns as seen below.

1. work_year: The year the salary was paid.
2. experience_level: The experience level in the job during the year
3. employment_type: The type of employment for the role
4. job_title: The role worked in during the year.
5. salary: The total gross salary amount paid.
6. salary_currency: The currency of the salary paid as an ISO 4217 currency code.
7. salaryinusd: The salary in USD
8. employee_residence: Employee's primary country of residence in during the work year as an ISO 3166 country code.
9. remote_ratio: The overall amount of work done remotely
10. company_location: The country of the employer's main office or contracting branch
11. company_size: The median number of people that worked for the company during the year

The purpose for writing this software was to use data from a dataset and use python to filter out data depending on the inputed filters and display it to the user. The program allows for 10 different filters that the user can choose from.

1. Work Year
2. Experience Level
3. Employment Type
4. Job Title
5. Salary
6. Employee Residence
7. Remote Ratio
8. Company Location
9. Company Size
10. Rows

The intention of making this project was to use tkinter to create and interactable program in which a user can view data and filter out data from a database using provided filters and buttons. The program is designed in a way to give an explanation to the user before they use it and provide the user with a basic understanding. The program is also designed in a way that allows for additional datasets to be added in the future. With a few adjustments to the code the process can be repeated for multiple different datasets.

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

{List the questions and the answers you found by doing this analysis.}

What type of Computer Science jobs provide remote opportunities?

- Using the remote filter we can search which jobs offer remote opportunities.

What type of Computer Science jobs provide the best pay?

- Looking at the salary filter we can quickly find computer science jobs that pay a salary greater than the selected value.

# Development Environment

{Describe the tools that you used to develop the software}
The tools that I used in this application are Tkinter, pandas and pandastables

- Tkinter
  - Tkinter is a tool used to create a GUI for the appliction it renders code and displays the code as an interface. The interface is rendered by a parent class and that parent class houses children assets that add to the parent class
- Pandas
  - Pandas is a tool used for reading, modifying, deleting files. In this project its used to read the contents of a CVS file and display the results to a table located in the Tkinter application
- pandastables
  - Pandastables is a tool used to display a cvs file from pandas to tkinter. It aids in visualizing tables, additional functionality can be added to the pandastables tables however I used a basic table that is only used to display the table.

The primary programming language I used is python the libraries used are seen above. Python is a fast running programming language that can be used in colaboration to many different programming languagues and toolsets.

# Useful Websites

- [Kaggle](https://www.kaggle.com/)
- [Tkinter Docs](https://tkdocs.com/)

# Future Work

- One item that I hope to improve is more datasets. For most of this week a lot of research was done expecially into the tkinter platform I spent a lot longer time trying to connect my tkinter to my python program in hopes of implementing my pandas functions into my tkinter. However, now that I know the basics behind both concepts I hope to add more datasets to the project in the future.
- Improve Design. I found it quite difficult to design the Tkinter framework so in the future I hope to add a better GUI platform that allows for more styling with easier access.
