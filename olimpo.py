while True:
        print("Options: [1]User Path [2]Main Path: ")
        choice = int(input(" Choices :"))

        if choice == 1:
                import User
                break

        elif choice == 2:
            import donna
            break

        else:
            print("Invalid input......................")