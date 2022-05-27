# inefficient way to do it
def anyFunc():
    if (wifi):
        if (login):
            if (admin):
                seeAdminPanel()
            else:
                print("not an admin")
        else:
            print("not logged in")
    else:
        print("not connected")

# Correct way to do it
def anyFunc():
    if(not wifi):
        print("not connected")
        return
    if(not login):
        print("not logged in")
        return
    if(admin):
        seeAdminPanel()
    else:
        print("not an admin")
        return