from utilities import read_utils

test_invalid_login_data = read_utils.get_excel_as_list("../test_data/Book2.xlsx","Sheet1")
test_valid_login_data = read_utils.get_csv_as_list("../test_data/LoginData.csv")