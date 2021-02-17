class userName:

    users = {"u1":"u1@123","u2":"u2@123", "u3":"u3@123" }
    user_profile = {"u1":["sattu", 28, "M", "123"], "u2":["sana", 26, "F", "234"]}

    def __init__(self):
        pass


    def userSignUp(self, userid, password):

        if userid not in self.users.keys():
            self.users[userid] = password
            print("Registration successful !!")
        else:
            print("User already Exists..")


    def userLogin(self,userid,password):
        if (userid in self.users.keys() and self.users.get(userid) == password):
            print("Login  successful !!")
        else:
            print("Invalid username/password. Try again.")

    def CreateProfile(self, id, profile):
        if id not in self.user_profile.keys():
            self.user_profile[id] = [profile]
            print("profile created successfully")
        else:
            print("profile already Exists..")

    def UpdateProfile(self, id, profile):
        if id in self.user_profile.keys():
            self.user_profile.update({id:profile})
            print("profile updated successfully")
        else:
            print("profile does not Exists..")

    def deleteProfile(self, id):
        if id in self.user_profile.keys():
            self.user_profile.pop(id)
            print("profile deleted successfully")
        else:
            print("profile does not Exists..")

    def displayprofile(self, id):

        print("Name: ",(self.user_profile.get(id))[0], "\n"
              "Age: ", (self.user_profile.get(id))[1], "\n"
              "gender:",(self.user_profile.get(id))[2], "\n"
              "number:",(self.user_profile.get(id))[3])

    #def deluser(self):
       # self.users.remove(username)

    def displayusers(self):
        return self.users