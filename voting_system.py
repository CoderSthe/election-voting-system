def verify_login():
    """This function verifies the username and password of a login attempt."""

    username_list = []
    password_list = []
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open('user.txt') as f:
        for line in f:
            f_username, f_password = line.split(', ')
            f_password = f_password.strip()
            username_list.append(f_username)
            password_list.append(f_password)
    user_data = dict(zip(username_list, password_list))

    while not user_data.get(username) or password != user_data[username]:
        print("Your username or password is incorrect. Please try again\n")
        username = input("Enter username: ")
        password = input("Enter password: ")
    print("1.\t Register Candidate")
    print("2.\t View Provincial Candidates")
    print("3.\t View National Candidates")
    print()
    user_choice = int(input())
    if user_choice == 1:
        register_candidate()
    elif user_choice == 2:
        view_prov_candidates()
    elif user_choice == 3:
        view_nat_candidates()


def display_parties():
    """This function displays to screen all the registered political
    parties participating in the elections."""

    with open('political_parties.txt') as f:
        contents = f.read()
        print(contents)
        print()


def display_ballot_choice():
    """This function displays to screen the ballot options available for voters."""

    print("1.\t Provincial Elections")
    print("2.\t National Elections")
    print()


def check_registration():
    """This function verifies whether a given ID number has registered to vote."""

    voter_name_list = []
    voter_id_list = []
    voter_province_list = []
    id_num = int(input("Enter your ID number: "))
    with open('registered_voters.txt', 'r') as f:
        for line in f:
            voter_name, voter_id, voter_province = line.split(' - ')
            voter_name_list.append(voter_name)
            voter_id_list.append(voter_id)
            voter_province_list.append(voter_province)
    
    for i in range(len(voter_id_list)):
        if str(id_num) == voter_id_list[i]:
            print("You are registred to vote.")
            print(f"Name: {voter_name_list[i]}\nID Number: {voter_id_list[i]}\nProvince: {voter_province_list[i]}")
            quit()
    print(f"ID number {id_num} not registered to vote.")


def register_voter():
    """This function registers a voter who wants to cast their vote"""

    id_num = int(input("Enter your ID number: "))
    assert len(str(id_num)) == 13, "Invalid ID number given."

    voter_name = input("Enter your full name: ")
    print("Select your current province\n")
    with open('provinces.txt') as f:
        print(f.read())

    user_choice = int(input())
    province = PROVINCE.get(user_choice)

    with open('registered_voters.txt', 'a') as f:
        f.write(f"{voter_name} - {id_num} - {province}\n")

    print(f"{voter_name} successfully registered to vote in {province}.")


def register_candidate():
    """This function registers a leader name who wants to
    participate in the elections.
    It also establishes whether the candidate intends
    running for provincial or national elections."""
    
    reg_num = int(input("How many candidates are being registered? "))
    for i in range(reg_num):
        print("Enter candidate party:")
        display_parties()
        user_choice = int(input())
        assert user_choice > 0 and user_choice <= len(POLITICAL_PARTY), "Invalid selection made."

        candidate_party = POLITICAL_PARTY.get(user_choice)
        candidate_name = input("Enter Candidate Name: ")
        print("Is candidate contesting for Provincial or National elections? ")
        display_ballot_choice()
    
        user_choice = int(input())
        assert user_choice == 1 or user_choice == 2, "Invalid selection made."

        if user_choice == 1:
            ballot_contest = "Provincial"
        else:
            ballot_contest = "National"
        print()

        with open('registered_candidates', 'a') as f:
            f.write(f"{candidate_name} - {candidate_party} - {ballot_contest}\n")

        print(f"Candidate {i + 1} successfully registered!\n")


def view_prov_candidates():
    """This function displays to screen a list of registered provincial
    candidates for the elections."""

    with open('registered_candidates.txt') as f:
        for line in f:
            if "Provincial" in line:
                print(line)


def view_nat_candidates():
    """This function displays to screen a list of registered national
    candidates for the elections."""
    
    with open('registered_candidates.txt') as f:
        for line in f:
            if "National" in line:
                print(line)


def cast_vote():
    """This function captures a registered voter's choice and stores
    results in a text file."""

    id_num = int(input("Enter ID number: "))
    with open('registered_voters.txt', 'r') as f:
        voters = f.read()

    if str(id_num) in voters:
        print("Is vote for Provincial or National ballot:")
        display_ballot_choice()
        user_choice = int(input())
        assert user_choice == 1 or user_choice == 2, "Invalid selection made."
        if user_choice == 1:
            ballot_choice = "Provincial"
        else:
            ballot_choice = "National"
        print("Choose political party:")
        display_parties()
        user_choice = int(input())
        voter_choice = POLITICAL_PARTY.get(user_choice)

        with open('cast_votes', 'a') as f:
            f.write(f"{id_num} - {ballot_choice} - {voter_choice}\n")

        print("Vote has been cast!")
    else:
        print("ID number not registered to vote.")
    

def main():
    print("1.\t Internal Employee Login")
    print("2.\t Check my registration status")
    print("3.\t Register to vote")
    print("4.\t Cast my vote")
    print()

    user_choice = int(input())
    if user_choice == 1:
        verify_login()
    elif user_choice == 2:
        check_registration()
    elif user_choice == 3:
        register_voter()
    elif user_choice == 4:
        cast_vote()


POLITICAL_PARTY = {}
with open('political_parties.txt') as f:
    for line in f:
        (key, val) = line.strip().split(' - ')
        POLITICAL_PARTY[int(key)] = val

PROVINCE = {}
with open ('provinces.txt', 'r') as g:
    for line in g:
        (key, val) = line.strip().split(' - ')
        PROVINCE[int(key)] = val



main()