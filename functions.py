import pandas as pd

cols = [
    "work_year",
    "experience_level",
    "employment_type",
    "job_title",
    "salary_in_usd",
    "employee_residence",
    "remote_ratio",
    "company_location",
    "company_size",
]


def main(filename, year, el, et, jt, s, er, rr, cl, cs, rows):
    iter_csv = pd.read_csv(filename)

    WorkYear = parse_data(iter_csv, year, 0)
    ExperienceLevel = parse_data(iter_csv, el, 1)
    EmploymentType = parse_data(iter_csv, et, 2)
    JobTitle = parse_data(iter_csv, jt, 3)
    Salary = parse_salary(iter_csv, s, 4)
    EmployeeResidence = parse_data(iter_csv, er, 5)
    RemoteRatio = parse_data(iter_csv, rr, 6)
    CompanyLocation = parse_data(iter_csv, cl, 7)
    CompanySize = parse_data(iter_csv, cs, 8)

    result = pd.concat(
        [
            WorkYear,
            ExperienceLevel,
            EmploymentType,
            JobTitle,
            Salary,
            EmployeeResidence,
            RemoteRatio,
            CompanyLocation,
            CompanySize,
        ],
        axis=1,
        join="inner",
    )

    result = result.loc[:, ~result.columns.duplicated()]
    result = result[:rows]

    return result


def parse_data(file, element_filter, element):
    col = cols[element]
    if element_filter:
        filter = file[col].isin(element_filter)
        filter_res = file[filter]

        return filter_res
    else:
        return file


def parse_salary(file, element_filter, element):
    col = cols[element]
    if element_filter:
        filter = file[col] > int(element_filter[0])
        filter_res = file[filter]

        return filter_res
    else:
        return file


main(
    "./datasets/ds_salaries.csv",
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    10,
)
