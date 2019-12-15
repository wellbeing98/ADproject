import http
from bs4 import BeautifulSoup
import requests
import ad_dict
service_key = "6b59444444776a64373664556a7644"

class Gettime_station_history:
    def __init__(self, departure_station, arrival_station):

        self.depart= departure_station
        self.arrive= arrival_station
        self.shortindex = 0 #적은 시간이 걸리는 경우의 인덱스
        st = ad_dict.JSONDict[self.depart]
        ar = ad_dict.JSONDict[self.arrive]
        url_3 = "http://ws.bus.go.kr/api/rest/pathinfo/getPathInfoBySubway?ServiceKey=%2BurVX0NS%2FR0gnSJAPplvPe4AKfCzVhZG9UY6LUnSFTQwKmHcbtAsetokdvddXzVVQJ9ThRvwBzGXifojUxm9Ag%3D%3D&startX=" + str(
            st[1]) + "&startY=" + str(st[0]) + "&endX=" + str(ar[1]) + "&endY=" + str(ar[0])
        result2 = requests.get(url_3)
        self.bs_obj2 = BeautifulSoup(result2.content, "html.parser")
        top_right3 = self.bs_obj2.findAll("routenm")
        self.top_list4 =[]
        for top in top_right3:
            self.top_list4.append(str(top.text)[0])
        print(self.top_list4)

        try:
            url_2 = "http://openapi.seoul.go.kr:8088/" + service_key + "/xml/StationNmfpcOrgnThemaNm/1/5/" + top_list4[-1]+ "/" + self.arrive
            self.result = requests.get(url_2)
            self.bs_obj = BeautifulSoup(self.result.content, "html.parser")
            self.top_right = self.bs_obj.find("nmfpc_orgn")
            self.history=str(self.top_right.text)
        except:
            self.history="NO INFORMATION"

    def Gethistory(self):
        return(self.history)
    def GetStation_line(self):
        flist = [i for i, x in enumerate(self.top_list4) if x == self.top_list4[-1]]
        if self.shortindex != 0:
            wantst_line = self.top_list4[flist[self.shortindex - 1] + 1:flist[self.shortindex]+1]
        else:
            wantst_line = self.top_list4[:flist[self.shortindex]+1]
        return (wantst_line)

    def Gettime(self):

        top_right = self.bs_obj2.findAll("time")
        top_list = []
        for top in top_right:
            top_list.append(int(top.text))
        # sorted(top_list)
        for i in range(len(top_list)):
            sm_time = top_list[0]
            if top_list[i] <= sm_time:
                sm_time = top_list[i]
            self.shortindex=top_list.index(sm_time)
        return(sm_time)

    def GetTransit_station(self):
         top_right2 = self.bs_obj2.findAll("tname")
         top_list2 = []
         for top in top_right2:
             top_list2.append(str(top.text))
         flist = [i for i, x in enumerate(top_list2) if x == top_list2[-1]]
         if self.shortindex != 0:
             wantst = top_list2[flist[self.shortindex - 1] + 1:flist[self.shortindex]]
         else:
             wantst = top_list2[:flist[self.shortindex]]
         return(wantst)
if __name__=='__main__':
    c = Gettime_station_history("삼성","태평")
    print(c.Gethistory())
    print(c.Gettime())
    print(c.GetTransit_station())
    print(c.GetStation_line())



