import requests

def get_user_info(handles):
    i=len(handles)
    handle=';'.join(handles)
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url)
    #print(response.text)
    if response.status_code == 200:
        user_data = response.json()
        #print(user_data)
        if user_data['status']=="OK":
            for j in range(0,i):
                user_info= user_data['result'][j]
                if user_info:
                    print(f"Handle: {user_info['handle']}")
                    print(f"Rank: {user_info['rank']}")
                    print(f"Rating: {user_info['rating']}")
                    print("")
                else:
                    print("User not found.")
        else:
            print(user_data['response'])
    else:
        print(response.status_code)

n=int(input("Number of Users? "))
handles=[]
for i in range (0,n):
    new_handle=input(f"Enter the user Number {i+1} ")
    handles.append(new_handle)
user_info = get_user_info(handles)

