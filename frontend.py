import backend

def get_organization_info(option):
    while True:
        if option == '1':
            orgNames = input("Enter Organization Names separated by commas (or type 'main menu' to return to the main menu): ")
        elif option == '2':
            orgNames = input("Enter Organization Domain Names separated by commas (or type 'main menu' to return to the main menu): ")
        if orgNames.lower() == 'main menu':
            break

        orgList = [org.strip() for org in orgNames.split(",")]

        for org in orgList:
            print(f"\nResults for: {org}")
            if option == '1':
                print(f"{backend.getLinkedinOrg(org, option)}\n")
            elif option == '2':
                print(f"{backend.getLinkedinOrg(org, option)}\n")

def main():
    while True:
        print('Please type in the number corresponding to the option you would like to use: \n')
        print('1. Get LinkedIn Organization Info')
        print('2. Get LinkedIn Profile Info')
        print('3. Exit')

        option = input()

        if (option == '1' or option.lower() == 'get linkedin organization info'):
            print("How would you like to retrieve the organization's LinkedIn profile? \n")
            print('1. By Organization Name')
            print('2. By Organization Domain ex: www.salesql.com')
            option = input()
            if (option == '1' or option == '2'):
                get_organization_info(option)
            
        elif (option == '2' or option.lower() == 'get linkedin profile info'):
            person = input("Please type in the full name of the LinkedIn profile you would like to retrieve: ")
            org = input("Please type in place the person works at: ")
            print(f"\nResults for: {person} at {org}")
            print(backend.getLinkedinProfile(person, org), "\n")
        elif (option == '3' or option.lower() == 'exit'):
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

