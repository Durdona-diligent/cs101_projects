#The Scholarship Committee
def select_candidates(names, gpas, volunteering_hours):
    candidate_list = (zip(names, gpas, volunteering_hours))
    eligible = [candidate for candidate in candidate_list if candidate[1] >= 3.8 or (candidate[1] >= 3.5 and candidate[2] > 50)]
    sorted_candidates = sorted(eligible, key=lambda candidate: (-candidate[1], -candidate[2]))
    formatted = [f'{candidate[0]}: {candidate[1]} / {candidate[2]}h' for candidate in sorted_candidates]
    print(formatted)
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
gpas = [3.9, 3.2, 3.6, 3.7, 3.5]
hours = [10, 100, 60, 20, 40]
select_candidates(names, gpas, hours)    