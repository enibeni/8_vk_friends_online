import vk
from getpass import getpass


APP_ID = 6350031


def get_user_login():
    login = input("Enter your login:\n")
    return login


def get_user_password():
    password = getpass("Enter your password:\n")
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    api = vk.API(session)
    friend_ids = api.friends.getOnline()
    friends_online = api.users.get(
        user_ids=friend_ids,
        fields="first_name,last_name",
    )
    return friends_online


def output_friends_to_console(friends_online):
    print("Friends online:\n")
    for friend in friends_online:
        print("{} {}".format(friend["first_name"], friend["last_name"]))

if __name__ == "__main__":
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)


