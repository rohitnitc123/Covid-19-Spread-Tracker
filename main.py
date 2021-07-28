import requests
import bs4
import tkinter as tk
def get_html_data(web_url):
    data=requests.get(web_url)
    return data

def get_covid19_data():
    web_url="https://www.worldometers.info/coronavirus/"
    html_data=get_html_data(web_url)
    soup = bs4.BeautifulSoup(html_data.text,'html.parser')
    information = soup.find("div",class_="content-inner").findAll("div",id="maincounter-wrap")
    all_data=""
    

    for i in range(3):
        text=information[i].find("h1",class_=None).get_text()
        count= information[i].find("span",class_=None).get_text()
        all_data=all_data+text+" "+count +"\n"
        
    return all_data








def reload():
    new_data=get_covid19_data()
    mainLabel['text']=new_data

   

window=tk.Tk()  
window.geometry("1000x800") 
window.title("Covid-19 Spread Tracker")   
f=("puppins",25,"bold")
banner=tk.PhotoImage(file="img2.png")
bannerLabel=tk.Label(window,image=banner)
bannerLabel.pack()


Country_Entry=tk.Entry(window,width=100)
Country_Entry.pack()


def get_country_wise_data()  :
    name=Country_Entry.get() 
    new_web_url= "https://www.worldometers.info/coronavirus/country/"+name
    html_data=get_html_data(new_web_url)
    soup = bs4.BeautifulSoup(html_data.text,'html.parser')
    information = soup.find("div",class_="content-inner").findAll("div",id="maincounter-wrap")
    all_data=""
    # print(information)

    for i in range(3):
        text=information[i].find("h1",class_=None).get_text()
        count= information[i].find("span",class_=None).get_text()
        all_data=all_data+text+" "+count +"\n"
        # print(all_data)
    mainLabel['text']=all_data

# get_covid19_data()





mainLabel=tk.Label(window,text=get_covid19_data(),font=f)
mainLabel.pack()




GetData_Button=tk.Button(window,text="Get Data",font=f,relief='solid',command=get_country_wise_data)
GetData_Button.pack()




reload_Button=tk.Button(window,text="Refresh",font=f,relief='solid',command=reload)
reload_Button.pack()

window.mainloop()



   
