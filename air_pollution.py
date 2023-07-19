import folium
import urllib.request
import json
import webbrowser
#import matplotlib.pyplot as plt


r=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/air_pollution?lat=34.09694&lon=49.69097&appid=c25103faa8e1e86e246b9b4329d342f0')
rr=r.getcode()
r_read=r.read()

r_load=json.loads(r_read)

j=[]
for i in r_load['coord']:
    j.append(r_load['coord'][i])
m=folium.Map(location=j)


t='اطلاعات بیشتر'

item_txt = """<br> &nbsp; {item} &nbsp; <i class="fa fa-map-marker fa-2x" style="color:{col}"></i>"""
html_itms = item_txt.format( item= 'پاک' , col= "green")
html_itms2 = item_txt.format( item= 'قابل قبول' , col= "yellow")
html_itms3 = item_txt.format( item= 'ناسالم ' , col= "red")
html_itms4 = item_txt.format( item= 'بسیار ناسالم' , col= "purple")
html_itms5 = item_txt.format( item= 'خطرناک' , col= "darkred")

legend_html = """
     <div style="
     position: fixed; 
     top: 50px; right: 50px; width: 200px; height: 180px; 
     border:2px solid grey; z-index:9999; 
     
     background-color:white;
     opacity: .85;
     
     font-size:14px;
     font-weight: bold;
     
     ">
     &nbsp; {title} 
     
     {itm_txt1}
     {itm_txt2}
     {itm_txt3}
     {itm_txt4}
     {itm_txt5}
     
     

      </div> """.format( title = "راهنما", itm_txt1= html_itms,
      itm_txt2=html_itms2,
      itm_txt3=html_itms3,
      itm_txt4=html_itms4,
      itm_txt5=html_itms5
      )
m.get_root().html.add_child(folium.Element( legend_html ))

    

iframe = folium.IFrame( str(r_load['list'][0]['components']) )

if r_load['list'][0]['main']['aqi'] == 1:
    popup = folium.Popup(iframe, min_width=250, max_width=150)
    folium.Marker(
        location=j,
        tooltip=t,
        popup=popup,
        
        icon=folium.Icon(color='green',icon="info-sign")
        
                         
    ).add_to(m)

elif r_load['list'][0]['main']['aqi'] == 2:
    popup = folium.Popup(iframe, min_width=250, max_width=150)
    folium.Marker(
        location=j,
        tooltip=t,
        popup=popup,
        
        icon=folium.Icon(color='yellow',icon="info-sign")
        
                        
    ).add_to(m)

elif r_load['list'][0]['main']['aqi'] == 3:
    popup = folium.Popup(iframe, min_width=250, max_width=150)
    folium.Marker(
        location=j,
        tooltip=t,
        popup=popup,
        
        icon=folium.Icon(color='red',icon="info-sign")
        
                        
    ).add_to(m)

elif r_load['list'][0]['main']['aqi'] == 4:
    popup = folium.Popup(iframe, min_width=250, max_width=150)
    folium.Marker(
        location=j,
        tooltip=t,
        popup=popup,
        
        icon=folium.Icon(color='purple',icon="info-sign")
        
                        
    ).add_to(m)

elif r_load['list'][0]['main']['aqi'] == 5:
    popup = folium.Popup(iframe, min_width=250, max_width=150)
    folium.Marker(
        location=j,
        tooltip=t,
        popup=popup,
        
        icon=folium.Icon(color='darkred',icon="info-sign")
        
                        
    ).add_to(m)
    
m.save('map.html')
webbrowser.open('map.html')
