import requests

token = input("Token: ")
headers = {"Authorization": token}

response = requests.get("https://discord.com/api/v10/users/@me", headers=headers)

if response.status_code == 401:
    print(f"\033[31m{token} is invalid")
elif response.status_code != 200:
    print("\033[1;31mAn error occured while checking the token")

elif response.status_code == 200:
    print(f"\033[1;32m{token} is valid!\033[0;32m")
    user = response.json()
    info = ""
    nitro_type = ""

    info += f"Username: {user['username']}" 

    if user['discriminator'] != '0':
        info += f"#{user['discriminator']}"
    
    info += "\n"
    
    if user['global_name'] is not None:
        info += f"Global Name: {user['global_name']}\n"
    
    if user['email'] is not None:
        info += f"E-mail: {user['email']}\n"
    
    if user['phone'] is not None:
        info += f"Phone Number: {user['phone']}\n"
    
    if user['premium_type'] != 0:
        if user['premium_type'] == 2:
            nitro_type == "Normal"
        elif user['premium_type'] == 3:
            nitro_type == "Basic"
        elif user['premium_type'] == 1:
            nitro_type == "Classic"

        info += f"Nitro: {nitro_type}\n"

    info += f"MFA: {user['mfa_enabled']}\n"

    if user['bio']:
        info += f"Bio: {user['bio']}"

    print(info)