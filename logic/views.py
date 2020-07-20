from django.shortcuts import render
from . models import vsong,asong,ysong,event,service
from json import dumps
def home(request):
    ysongs=ysong.objects.all()
    single=ysongs[0]
    

    event1=event()
    event1.name="event_name"
    event1.date="event_date"
    event1.venue="event_venue"
    event1.pic="event-1.jpg"
    event2=event()
    event2.name="event2_name"
    event2.date="event2_date"
    event2.venue="event2_venue"
    event2.pic="event-2.jpg"
    events=[event1,event2]
    
    service1=service()
    service1.name="Wedding"
    service1.desc="desc"
    service1.pic="service-1.png"
    service2=service()
    service2.name="Wedding"
    service2.desc="desc"
    service2.pic="service-2.png"
    service3=service()
    service3.name="Wedding"
    service3.desc="desc"
    service3.pic="service-3.png"
    service4=service()
    service4.name="Wedding"
    service4.desc="desc"
    service4.pic="service-4.png"
    
    services=[service1,service2,service3,service4]

   
    asongs=asong.objects.all()
    allsongs={}
    for i in range(len(asongs)):
        allsongs[i]=[asongs[i].name,asongs[i].artist,asongs[i].pic.url,asongs[i].aud.url]
    asongs=asongs[0]
    allsongs=dumps(allsongs)
    return render(request,'index.html',{'single':single,'ysongs':ysongs,'eventsob':events,"servicesob":services,"asong":asongs,'allsongs':allsongs})
def check(request):
    dataDictionary = { 
        'hello': 'World', 
        'geeks': 'forgeeks', 
        'ABC': 123, 
        456: 'abc', 
        14000605: 1, 
        'list': ['geeks', 4, 'geeks'], 
        'dictionary': {'you': 'can', 'send': 'anything', 3: 1} } 
    dataJSON = dumps(dataDictionary) 
    return render(request,'check.html',{'data': dataJSON})