import requests

def fetch_random_user_freeAPI():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    resposnse=requests.get(url)
    data=resposnse.json()
    # print(resposnse)
    # print(data)
    if data["success"] and "data" in data:
        user_data=data["data"]
        username=user_data["login"]["username"]
        country=user_data["location"]["country"]
        return username,country
    else:
        raise Exception("Failed to fetch user data!")

def main():
    try:
        username, country= fetch_random_user_freeAPI()
        print(f"{username} lives in {country}.")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()

