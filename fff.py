student_db = [
 {"first_name": "adam", "last_name": "wong",
"gender": "m", "admin_no": "190001"},
 {"first_name": "betty", "last_name": "tan",
"gender": "f", "admin_no": "190002"}
] 


class Iterable:
    def __init__(self, iterable):
    def __iter__(self):
        return self

def mailing_list(input, gender):
    return list(map(lambda x: f"{x['admin_no']}@mymail.nyp.edu.sg", filter(lambda g: g['gender'] == gender, input )))


print(mailing_list(student_db, 'm'))
interable = range(1,10)
print(Iterable(interable))

print(range(1, 100))