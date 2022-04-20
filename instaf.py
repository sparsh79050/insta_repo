import requests

def followers(user):
    url="https://www.instagram.com/"+ user
    result=requests.get(url).text
    start='"edge_followed_by":{"count": "end= "}, "followed_by_viewer"'
    result=str(result[result.find(start)+ len(start): result.rfind()])
    return result

if __name__=="__main__":
    user=input("Enter Instagram account: ")
    print(followers(user))
