POLITICAL_PARTY = {
    1: "African National Congress (ANC)",
    2: "Democratic Alliance (DA)",
    3: "Economic Freedom Fighters (EFF)",
    4: "Inkatha Freedom Party (IFP)",
    5: "Independent Candidate"
}

def register_candidate():
    """This function registers a leader name who wants to
    participate in the elections.
    It also establishes whether the candidate intends
    running for local or national elections."""
    
    reg_num = int(input("How many candidates are being registered? "))
    for i in range(reg_num):
        print("Enter Candidate Party:")
        print("1.\t African National Congress (ANC)")
        print("2.\t Democratic Alliance (DA)")
        print("3.\t Economic Freedom Fighters (EFF)")
        print("4.\t Inkatha Freedom Party")
        print("5.\t Independent Candidate")
        print()
        user_choice = int(input())
        assert user_choice > 0 and user_choice <= len(POLITICAL_PARTY), "Invalid selection made."
        candidate_party = POLITICAL_PARTY.get(user_choice)
        candidate_name = input("Enter Candidate Name: ")
        print("Is candidate contesting for Local or National elections? ")
        print("1.\t Local Elections")
        print("2.\t National Elections")
        print()
        user_choice = int(input())
        assert user_choice == 1 or user_choice == 2, "Invalid selection made."
        if user_choice == 1:
            contest_district = "Local"
        else:
            contest_district = "National"
        print()
        with open('registered_candidates', 'a') as f:
            f.write(f"{candidate_name} - {candidate_party} - {contest_district}\n")

        print(f"Candidate {i + 1} successfully registered!\n")


def register_voter():
    """This function registers a voter who wants to cast their vote"""

    id_num = int(input("Enter Voter's ID Number: "))
    assert id_num == 0 or len(str(id_num)) == 13, "Invalid ID number given."
    while id_num != 0:
        voter_name = input("Enter Voter Name: ")
        with open('registered_voters', 'a') as f:
            f.write(f"{voter_name} - {id_num}\n")
        print(f"{voter_name} successfully registered as voter!\n")
        id_num = int(input("Enter Voter's ID Number: "))


def cast_vote():
    anc, da, eff, ifp, indie = 0,0,0,0,0
    id_num = int(input("Enter ID number: "))
    with open('registered_voters', 'r') as f:
        contents = f.read()
    if str(id_num) in contents:
        print("Choose from the below options:")
        print("1.\t African National Congress (ANC)")
        print("2.\t Democratic Alliance (DA)")
        print("3.\t Economic Freedom Fighters (EFF)")
        print("4.\t Inkatha Freedom Party (IFP)")
        print("5.\t Independent Candidate")
        print()
        user_choice = int(input())
        if user_choice == 1:
            anc += 1
        elif user_choice == 2:
            da +=1
        elif user_choice == 3:
            eff += 1
        elif user_choice == 4:
            ifp += 1
        elif user_choice == 5:
            indie += 1


def main():
    print("Select Menu Option:")
    print("1.\t Register Candidate")
    print("2.\t Register Voter")
    print("3.\t Cast Vote")
    print()
    user_choice = int(input())
    assert user_choice == 1 or user_choice == 2 or user_choice == 3, "Inavlid selection made"

    if user_choice == 1:
        register_candidate()
    elif user_choice == 2:
        register_voter()
    else:
        cast_vote()


main()