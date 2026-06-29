from datetime import date

def age(year: int) -> int:
    return date.today().year - year

def brand(name: str) -> str:
    return name.iloc[:,0].str.split(' ').str[0].to_frame()