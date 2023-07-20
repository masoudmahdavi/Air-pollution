import folium
import urllib.request
import json
import webbrowser
#import matplotlib.pyplot as plt


r=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/air_pollution?lat=51.403565&lon=35.723145&appid=c25103faa8e1e86e246b9b4329d342f0')
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
     border:2px solid grey; z-index:9999; font-weight: bold;
     background-color:white; opacity: .85; ont-size:14px;
     
     ">
     &nbsp; 
     {title} 
     {itm_txt1}
     {itm_txt2}
     {itm_txt3}
     {itm_txt4}
     {itm_txt5}
      </div> """.format( title = "راهنما", 
                         itm_txt1= html_itms,
                         itm_txt2=html_itms2,
                         itm_txt3=html_itms3,
                         itm_txt4=html_itms4,
                         itm_txt5=html_itms5
      )
m.get_root().html.add_child(folium.Element( legend_html ))

iframe = folium.IFrame( str(r_load['list'][0]['components']) )

def add_icon(input_color):
    popup = folium.Popup(iframe, min_width=250, max_width=150)
    folium.Marker(
        location=j,
        tooltip=t,
        popup=popup,
        icon=folium.DivIcon(html="""                        
            <div><span  style="background-color:{};padding:4pt 6pt;border-bottom-right-radius: 2pt;
                            border-top-right-radius: 2pt;color:white;
                            font-size: 12px;">Sadegh</span></div>""".format(input_color))   
            #<svg width="60" height="30">
            #    <rect x="0", y="0" width="60" height="25" rx="5" ry="5", fill="{}", opacity=".9">
            #</svg>
        # icon=folium.Icon(color=input_color,icon="info-sign")              
    ).add_to(m)


if r_load['list'][0]['main']['aqi'] == 1:
    add_icon('green')

elif r_load['list'][0]['main']['aqi'] == 2:
    print("im yellow")
    add_icon('yellow')
    
elif r_load['list'][0]['main']['aqi'] == 3:
    add_icon('red')

elif r_load['list'][0]['main']['aqi'] == 4:
    add_icon('purple')

elif r_load['list'][0]['main']['aqi'] == 5:
    add_icon('darkred')
    
m.save('map.html')
webbrowser.open('map.html')
'''
icon=folium.DivIcon(html=f"""
            <div><svg>
                <circle cx="50" cy="50" r="40" fill="#69b3a2" opacity=".4"/>
                <rect x="35", y="35" width="30" height="30", fill="red", opacity=".3" 
            </svg></div>""")    
            '''
