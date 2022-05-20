from db import query_single_value


def current_study_year() -> int:
    return query_single_value("SELECT current_study_year();")
